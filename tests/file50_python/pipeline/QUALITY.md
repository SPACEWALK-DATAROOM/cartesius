# Reviewed isolated Python contracts

Run from a checkout using an existing Python environment with pytest, coverage (if requested), pandas, NumPy and python-dateutil. Additional actual dependencies depend on the repository: beautifulsoup4/lxml for XML and HTML; requests; de-ds-common (`deds.verifier`) for schema validation; psycopg2-binary for database exception/cursor types; pydantic 1.10 for service schemas. de-catalog uses its checked-in pypika source. Python 3.9 with pandas 1.3.5 is the historic compatibility environment except road-address--silver, which requires its prepared Python 3.12/pandas 2.2.3 environment. No dependencies are installed by the runner.

```sh
# Set only when dependencies are supplied from separate read-only checkouts/directories:
export PIPELINE_EXTRA_PYTHONPATH="/path/to/actual/dependency/source:/path/to/private/deps"
python tests/file50_python/pipeline/run_quality.py --coverage --output /path/to/evidence
```

The runner uses the current interpreter and runs only paths in quality_scope.json; it does not discover old20 or other lanes' tests. It records argv, dependency paths, full runtime output, JUnit, exit code and optional source coverage outside the checkout.

These tests execute unchanged selected function/class definitions and explicitly supply real Python dependency objects. Startup imports are omitted and only Prefect task decorators are removed: this checks isolated transformations, parsers, request construction and state, not Prefect scheduling, SDK integration, DB SQL execution, browsers, services, native geometry or models. Static SQL assertions demonstrate generated strings only. Annotation compiler flags follow the original source, source order is retained, exact selection is checked and source/AST hashes are exposed as __source_provenance__. Extracted methods do not reconstruct their enclosing class or prove its private-name/super/import behavior. External I/O alone is replaced by mocks. Socket audit hooks reject real network connects and DNS requests. Genuine source failures remain failing tests and are detailed in the quality delivery.
