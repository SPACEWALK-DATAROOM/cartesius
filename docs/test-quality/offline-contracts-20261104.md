# Offline contract quality publication: cartesius

## Problem and resulting behavior

Publish the selected firstparty assertion bodies and the immutable ready Python quality delta. The quality harness selects actual repository definitions, preserves source order/annotation policy and records exact source provenance. Production source bytes are preserved (7 selected source files verified).

## Original criteria

User authorized real PR and squash merge of frozen50 plus ready quality packets, requires strict current HEAD Codex-only review, complete nonfailing CI, no expectation weakening/skip/xfail, no new product source edits, and no operational database/API/S3/ECR/deployment or credential execution. Historical cumulative patches remain immutable. Cross-lane intake index was inspected; the receipt lists applied packet paths and SHA256.

## Scope and fidelity

See repository test READMEs for isolated source and dependency boundaries.

Selected pre-campaign and campaign firstparty tests, required support/fixtures/dependencies and application locks remain present. This validation reruns the new quality packet scope only; retained earlier tests are not represented as freshly passing. Static, mock and isolated definition checks do not establish live DB/API behavior, framework startup, deployment, model training or full native compilation.

## Independent checkout execution

```sh
/home/josh/code-asset-test-improvement-20261029/venvs/de-ds-common-original-s3/bin/python tests/file50_python/pipeline/run_quality.py --coverage --output <evidence-directory>
```

Exit `0`; cases `3`, passed `3`, failed `0`, errors `0`, skipped `0`. The interpreter/dependency paths exactly reuse the packet's prepared read-only runtime; no global installation. Full command, JUnit, coverage and runtime output remain in the private publication receipt's evidence directory. All actual quality manifest test/source paths exist. No broad root or guessed JSON manifest was substituted.

### Preserved source failures

No failures in this packet.

Original expectations and original execution evidence remain in the immutable delivery; failure assertions remain active. No product bug is hidden by weakening expected values.

### Existing runner review

The existing offline runner now archives previous invocation artifacts and rejects empty/missing path selections. Actual stale-evidence negative control exit: 0. Old success evidence is retained separately; the new failed invocation returns 7 without stale counts.

## Publication and operational boundary


The detailed receipt records clone, selected pin/base HEAD, applied patch SHA256, source SHA preservation, exact publication exclusions, execution logs, reviews/fixes/CI, PR URL and merge SHA. Review status and actual MERGED state will be checked independently before a completed claim.

## Current invocation evidence and review corrections

The manifest runner now archives only its known evidence filenames before launch. Unrelated caller source files and scope manifests remain in place. An actual shadow coverage child exited77 after previous successful JUnit/coverage/exit evidence was seeded: the runner returned77, wrote a fresh failure exit record and left no current stale JUnit/coverage. Archived original bytes were checked. The exact original quality scope was then rerun: {'total': 3, 'failed': 0, 'errors': 0, 'skipped': 0, 'passed': 3}, exit0; case identity and each original pass/failure status are unchanged. Empty manifest tests are rejected before pytest can discover unrelated tests. Coverage export failures propagate and do not retain old success evidence.

Full reproducible command (prepared interpreter and dependency paths, no installation):

```sh
PIPELINE_EXTRA_PYTHONPATH='/home/josh/scratch/code-asset-parallel-20261101/docx-target20-20261103/file20-python-execution/continuation/orchestration/deps:/home/josh/scratch/code-asset-parallel-20261101/docx-target20-20261103/file20-python-execution/common/repo:/home/josh/scratch/code-asset-parallel-20261101/docx-target20-20261103/file50-python-execution/pipeline/wave3/deps' /home/josh/code-asset-test-improvement-20261029/venvs/de-ds-common-original-s3/bin/python tests/file50_python/pipeline/run_quality.py --coverage --output <evidence-directory>
```

Fresh positive evidence: `/home/josh/scratch/code-asset-parallel-20261101/docx-target20-20261103/test-quality-20261104/publication-python/evidence/cartesius/freshness-quality`. Actual subprocess negative evidence: `/home/josh/scratch/code-asset-parallel-20261101/docx-target20-20261103/test-quality-20261104/publication-python/evidence/cartesius/freshness-negative.log`. Original tests/expectations/logs remain preserved, and production source SHA checks still match. The output paths shown are lane-private evidence; independent users may choose any private directory.

## Approved trigger isolation (2026-11-04)

The user explicitly approved the exact trigger-only filter patch `5d3a8b0ba80e8262e78c05bc9803290bfd44fc98e72d26f6302a7bfd3835c515` from combined57. The previous operational publication hold is superseded only for this approved change. Actual default and local workflow bytes were compared with captured SHA values before applying the immutable patch with `git apply --unidiff-zero`.

Changed workflows:

- `.github/workflows/pytest.yml`

Approved ignored paths:

- `tests/**`
- `scripts/offline/**`
- `**/*.md`
- `docs/**`
- `.github/workflows/pytest.yml`

The cumulative outgoing paths, including these workflow files and this document, are ignored by the automatic operational branch/PR triggers. Production-path negative controls retain their original triggering behavior. Jobs, steps, commands, tag filters, manual events and all other workflow structure remain unchanged. No deployment, credential access, image/tag publication or business integration was executed. The existing functional results and genuine failures above are reused; the workflow change did not rerun healthy source suites.

Original criteria: publish first-party contracts and required support; preserve original assertions, approved source bytes and genuine failures; use actual Codex-only review and completed non-failing current-head CI. Skipped workflows are not proof that a required check succeeded. Required pending/failing checks continue to block normal merge. Undo: revert the resulting isolated squash commit. Criteria loosened: no.

## Review 1 fix: existing formatter contract

The new campaign Python files are formatted with the repository's existing `.isort.cfg` and `.style.yapf`, using prepared isort 9.0.2 and YAPF 0.43.0. Before formatting, both checks exited 1 on the outgoing files; after formatting, `isort --check-only .` and `yapf --recursive --diff .` both exit 0. Only new campaign files changed: every pre-existing Python file, source body and test expectation remains unchanged. A normalized AST comparison confirms all non-import syntax is preserved. The original bytes and failing checks remain in private evidence.

After formatting, the documented quality runner with prepared dependency paths still exits 0 with 3 passing cases. The prepared offline command `python scripts/offline/run.py --output "$RESULTS_DIR"` exits 0 with 28 passing cases. The previous HEAD's real isort CI failure is retained; only new-HEAD CI may satisfy merge, and no CI retry or bypass is used. The baseline Shapely 2 MultiPolygon compatibility failure observed by review remains product debt and was not changed.

## Review 2 fix: bind only dependencies used by this source contract

The wave12 loader no longer imports pandas, NumPy, dateutil or a generic bank of unused standard-library bindings. The selected original `kaggle_convert_labels` definition uses Python builtins only; its original AST selection, declaration order, annotation/future policy and provenance hash logic remain. The loader namespace retains file/name and explicit caller bindings. The redundant loader network audit is removed; the quality runner still loads the existing sitecustomize network guard.

A real `python -S -B` control (site packages disabled) now runs all 3 unchanged test bodies against the actual source definition while pandas, NumPy and dateutil are absent. Before this cut, that command failed during import. The documented quality command still exits 0 with 3/3 cases and coverage export success. The unrelated 28-case geometry result is preserved from the prior fix rather than repeated. All original source/test/lock bytes and assertions are unchanged. Existing pylint CI configuration/runtime failure remains recorded and is not reported as successful.

## Approved CI repair publication (2026-11-05)

The user approved the concrete29-repository CI repair and15-workflow auto-tag isolation proposal with “추가승인할께 머지해”; the later explicit SHA-bound shared-reader approval records the exact workflow bytes while preserving original checks. This repository applies approved additive patch SHA256 `032c57b6fcc51f4352fa3d1570d48de46822de89aeea5de3a183f6eb9f4b6f7e` and the pre-existing cumulative runner/report corrections where present. Product source, original assertions, application locks, checker commands and genuine failures remain unchanged. No operational workflow, tag/image publication, external service, credential, manual dispatch or CI rerun is executed.

Only actual current-head Sol review and completed nonfailing reported CI may permit normal merge. Historical local functional results above are reused; they are not a claim that the new remote runner passed. Undo: normal revert PR for the resulting squash commit. No quality criterion is loosened.


## Canonical lint and equivalent coordinate collection repair
Canonical setup.py:11 declares pylint~=2.11; CI alone installed unpinned4.1.3. Install exactly the declared supported range without disabling checks. R1721 still reproduced under canonical2.17.7; remove redundant coordinate comprehension via list(zip(xs,ys)). Fifteen actual _gen_poly behavior comparisons across1/2/3/7/20vertices and3seeds preserve byte-identical geometryWKB. Canonical pylint product/tests10.00 exit0. This explicit semantic-equivalent small product cleanup is within delegated quality-repair authority. Original tests/locks unchanged; no training/model/GPU.


## Native functional CI runtime repair
Actual setup-python@v1 on ubuntu-latest could only locate cached3.11+; use ubuntu22.04/setup-python@v5 with supported3.9, and validate runtime changes through this existing CPU-only workflow by removing only its own workflow path from ignore. Test/docs isolation and all cases remain. The complete original tests/test_modeling.py is a synthetic8x32 CPU tensor/ScoreHead forward and one backward gradient-existence assertion. It has no optimizer, parameter update, training loop, pretrained checkpoint or GPU use. The user explicitly permits this finite CPU autodiff functional contract; it is not training. Native tests CI now uses supported Python3.9 for original torch/lightning ranges, keeps all original test collection/assertions/dependency ranges, and changes no test selection. setup.py has no secret-authenticated package references, so existing GH_PAT environment is not consumed by dependency declarations. Existing lint passed and original failures remain mandatory holds.
