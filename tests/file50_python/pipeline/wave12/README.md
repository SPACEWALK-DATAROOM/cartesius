# Pure label and deal-data source contracts

Only the new wave12 directory was targeted. Cartesius executes only the original label-to-row conversion function; no torch, tokenizer, native geometry, model, learned parameters or training is imported/executed. re_price_index executes only original DataLoader dtype/region/unit-price/building-group transformations and local synthetic CSV/pickle serialization; DB manager connect and pandas SQL reads are external I/O boundaries. No model, matrix, fit, inference, stabilization or credential lookup occurs.

The re_price_index utility-test candidate duplicated selected baseline boolean/pickle contracts and is excluded from patch/counts. Its complete candidate file, original failing XML/log and exclusion memo remain outside the patch. The selected JUnit is an explicitly documented subset of actual recorded DataLoader testcases, not a new execution.
