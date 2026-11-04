"""Run only the owned reviewed contracts using the selected Python environment."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True,help='Output directory for logs and machine-readable evidence')
    parser.add_argument('--coverage',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[3]
    output=args.output.resolve();output.mkdir(parents=True,exist_ok=True)
    scope=json.loads((Path(__file__).with_name('quality_scope.json')).read_text())
    paths=scope['tests']
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
    extra=env.get('PIPELINE_EXTRA_PYTHONPATH','')
    env['PYTHONPATH']=os.pathsep.join([str(root)]+([extra] if extra else []))
    cmd=[sys.executable,'-m']
    if args.coverage:
        env['COVERAGE_FILE']=str(output/'.coverage')
        cmd+=['coverage','run','--source='+','.join(scope['source_roots']),'-m']
    cmd+=['pytest','-c','/dev/null','--rootdir='+str(root),'-q','--tb=short',*paths,'--junitxml='+str(output/'junit.xml')]
    (output/'command.json').write_text(json.dumps({'argv':cmd,'cwd':str(root),'extra_pythonpath':extra},indent=2)+'\n')
    with (output/'runtime.log').open('w') as log:
        result=subprocess.run(cmd,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
    if args.coverage:
        with (output/'coverage-export.log').open('w') as log:
            exported=subprocess.run([sys.executable,'-m','coverage','json','-o',str(output/'coverage.json')],cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
        if exported.returncode: return exported.returncode
    (output/'exit-code.json').write_text(json.dumps({'exit_code':result.returncode})+'\n')
    return result.returncode
if __name__=='__main__':raise SystemExit(main())
