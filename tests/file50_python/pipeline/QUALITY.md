# Cartesius label-row conversion contracts

Run `python tests/file50_python/pipeline/run_quality.py --coverage --output /path/to/private/evidence` using an existing Python environment with pytest and optional coverage. No dependencies are installed by this runner.

The exact quality_scope.json selects three assertions in wave12/test_label_row_conversion.py. They execute the unchanged kaggle_convert_labels definition selected from the current cartesius/utils.py AST: scalar task rows, vector component order and stateless repeated/empty calls. Exact source/AST provenance is recorded; application startup, tensors, model inference and training are outside this isolated selection. A python -S control also passed all three bodies with site packages absent.

The selected definition uses Python builtins and has no network calls. This quality runner does not add scripts/offline to its child PYTHONPATH, so the scripts/offline/sitecustomize.py socket guard is not automatically loaded here. The separate full offline runner does load its existing guard. This corrects the earlier copied claim; it does not introduce a new gate or claim live-service verification.

Only explicit selected paths execute; empty selection fails before discovery. Previous known evidence files are archived, unrelated caller files remain, and child/coverage failure exits propagate. Original expectations and genuine source failures are preserved.
