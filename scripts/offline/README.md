# Pure geometry transform contracts

The previously delivered suite restored 19 existing cases and six additional cases against the actual checkout, with no production source changes. Round4 adds three distinct geometry/registry cases; the current cumulative suite is 28 cases. Tests import the real `cartesius/transforms.py` and real Shapely; no production implementation is copied or replaced.

## Reproduce

```sh
python3.12 -m venv /absolute/path/to/offline-venv
/absolute/path/to/offline-venv/bin/python -m pip install -r scripts/offline/requirements.lock
/absolute/path/to/offline-venv/bin/python scripts/offline/run.py --output /absolute/path/to/evidence
```

The original package initializer eagerly imports torch/lightning training components. The explicit `pure_cartesius` plugin registers only a namespace package to skip that initializer. Every selected transform and supporting Shapely implementation remains real. This does **not** verify package bootstrap, model/tokenizer/training code or inference. No heavy training dependency, external API/database, deployment or production operation is needed.

Original cases check normalization bounds/area/length. Added exact-value cases check a polygon hole and original geometry preservation, anchor/aspect ratio/area scaling, a degenerate point, a vertical line, a shared static scale factor for two shapes, and the base transform's NotImplementedError. These synthetic geometry expectations do not establish model quality or real-world design compliance. The original test file is byte-identical to the pinned base.

`snapshot.json` pins `2ec94c3f8fb76bd553b1c7b3b813b4b195c8fdbc` on main and records equality of all 46 audited blobs. `source-fixes.json` is empty. `original-test-integrity.json` verifies the original file. `test-identities.json` maps every observed JUnit case to the previous selected suite; `verified-result.json` records actual results/source execution. Positive imports/definitions, function-body execution and asserted behavior are distinct, and no whole-repository or archive coverage percentage is claimed.

The runner disables plugin auto-loading and explicitly enables pytest-mock plus namespace isolation. Its child environment is minimal, and an offline audit hook rejects socket access. It records command/environment, JUnit, subprocess/coverage exit codes, logs, coverage JSON, source/blob hashes, positive execution lines and artifact hashes. Failed tests or failed coverage export return failure. Output belongs outside the repository. Complete raw evidence is under `/home/josh/code-asset-test-improvement-20261029/evidence/cartesius/combined` on this machine; re-run for independent evidence.

The previously delivered aggregate was a local test-only commit; the round4 follow-up is uncommitted in its independent clone and is supplied as a cumulative patch. No push/PR, production write or expected-value relaxation is included.

## Round4 transform boundary extension

The cumulative runner passes 28/28: the prior 25 unique IDs and three new contracts. The additions verify position translation across disjoint 3D MultiPolygon components while preserving a hole, Z coordinates and input geometry; scale normalization's shared XY factor while preserving 3D line Z values; and all supported public `TRANSFORMS` registry names. These extend the single actually-covered production module, `cartesius/transforms.py`, without changing code or prior expectations.

The comparison runtime is the existing read-only Python3.12.3 environment with Shapely2.1.2, NumPy2.2.6, pytest9.2.0 and coverage7.17.0 from the pinned `requirements.lock`; no dependency changes were needed. Current JUnit, stdout/stderr and coverage evidence are in the round4 lane logs, while `verified-result.json` and `test-identities.json` record the cumulative 28-case run.
