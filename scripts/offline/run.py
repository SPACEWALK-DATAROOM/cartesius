"""Run only inspected, offline contracts against the actual checkout."""
import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=True)
# Preserve old invocation artifacts without treating them as current evidence.
previous = [path for path in out.iterdir() if path.is_file() and path.name in ('.coverage', '.coverage-journal', '.coverage-shm', '.coverage-wal', 'boundary.json', 'command.json', 'coverage-export.log', 'coverage-report.txt', 'coverage.json', 'deds-runtime-imports.json', 'exit-code.json', 'junit.xml', 'result.json', 'runtime.log', 'stderr.txt', 'stdout.txt')]
if previous:
    archive = Path(tempfile.mkdtemp(prefix='previous-', dir=out))
    for artifact in previous:
        shutil.move(str(artifact), str(archive / artifact.name))
env = {
    'PATH': '/usr/bin:/bin',
    'PYTHONPATH': str(ROOT / 'scripts/offline') + os.pathsep + str(ROOT),
    'PYTEST_DISABLE_PLUGIN_AUTOLOAD': '1',
    'COVERAGE_FILE': str(out / '.coverage'),
    'AWS_EC2_METADATA_DISABLED': 'true',
}
snapshot = json.loads((ROOT / 'scripts/offline/snapshot.json').read_text())
base_commit = snapshot['base_commit']
selection = json.loads((ROOT / 'scripts/offline/selection.json').read_text())
if not selection or any(not isinstance(path, str) or not (ROOT / path.split('::', 1)[0]).exists() for path in selection):
    parser.error('selection must name existing contract paths')
cmd = [sys.executable, '-m', 'coverage', 'run', '--branch', '--source=cartesius', '-m', 'pytest', '-c', '/dev/null', '--rootdir=' + str(ROOT),
       '-p', 'pytest_mock', '-p', 'pure_cartesius', '--import-mode=importlib', '-q',
       '--junitxml=' + str(out / 'junit.xml'), *selection]
start = time.monotonic()
run = subprocess.run(cmd, cwd=ROOT, env=env, text=True, capture_output=True)
(out / 'stdout.txt').write_text(run.stdout)
(out / 'stderr.txt').write_text(run.stderr)
report = subprocess.run([sys.executable, '-m', 'coverage', 'json', '-o', str(out / 'coverage.json')],
                        cwd=ROOT, env=env, text=True, capture_output=True)
(out / 'coverage-report.txt').write_text(report.stdout + report.stderr)
result = {'command': cmd, 'cwd': str(ROOT), 'environment': env,
          'returncode': run.returncode, 'coverage_returncode': report.returncode,
          'seconds': time.monotonic() - start,
          'base_commit': base_commit}
if (out / 'junit.xml').exists():
    cases = ET.parse(out / 'junit.xml').findall('.//testcase')
    result['tests'] = [{'classname': c.get('classname'), 'name': c.get('name'),
                        'origin': 'added' if 'offline_contracts' in c.get('classname', '') else 'original',
                        'status': 'failed' if c.find('failure') is not None else 'error' if c.find('error') is not None else 'skipped' if c.find('skipped') is not None else 'passed'} for c in cases]
    result['counts'] = {'cases': len(cases), **{k: sum(c['status'] == k for c in result['tests']) for k in ['passed', 'failed', 'error', 'skipped']},
                        **{k: sum(c['origin'] == k for c in result['tests']) for k in ['original', 'added']}}
if (out / 'coverage.json').exists():
    files = json.loads((out / 'coverage.json').read_text())['files']
    result['production_files'] = []
    for path, data in files.items():
        if not data['executed_lines']:
            continue
        source = ROOT / path
        result['production_files'].append({'path': path, 'tested_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                                           'original_blob_sha': subprocess.check_output(['git', 'rev-parse', base_commit + ':' + path], cwd=ROOT, text=True).strip(),
                                           'executed_lines': data['executed_lines']})
for name in ['junit.xml', 'coverage.json', 'stdout.txt', 'stderr.txt']:
    if (out / name).exists():
        result.setdefault('artifact_sha256', {})[name] = hashlib.sha256((out / name).read_bytes()).hexdigest()
(out / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['returncode', 'coverage_returncode', 'counts'] if k in result}))
print('Evidence:', out)
raise SystemExit(run.returncode or report.returncode)
