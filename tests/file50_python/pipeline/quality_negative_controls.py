"""In-memory negative controls: no production file is changed."""
import importlib
import json
from pathlib import Path
import sys
import types
from unittest.mock import patch

def main():
    base=Path(__file__).parent
    controls=json.loads(base.joinpath('quality_negative_controls.json').read_text())
    results=[]
    for index,control in enumerate(controls):
        target=base/control['test']
        package='quality_negative_'+str(index)
        mod=types.ModuleType(package);mod.__path__=[str(target.parent)];sys.modules[package]=mod
        test=importlib.import_module(package+'.'+target.stem)
        actual_load=test.load
        def altered(*args,**kwargs):
            ns=actual_load(*args,**kwargs)
            name=control['definition']
            if name in ns:
                if control.get('method'):
                    setattr(ns[name],control['method'],lambda *a,**kw:control['replacement'])
                else: ns[name]=lambda *a,**kw:control['replacement']
            return ns
        detected=False
        with patch.object(test,'load',side_effect=altered):
            try:getattr(test,control['case'])()
            except AssertionError:detected=True
        results.append({'test':control['test'],'case':control['case'],'mutation':'in-memory changed result for '+control['definition'],'detected':detected})
    print(json.dumps(results,indent=2))
    return 0 if all(r['detected'] for r in results) else 1
if __name__=='__main__':raise SystemExit(main())
