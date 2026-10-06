# Cross-Tool Validation Framework

This project defines a shared KPI contract so equivalent calculations can be compared across analytical tools.

## Current evidence state

`outputs/validation_summary.csv` records:

- CSV / Python — baseline values available;
- SQL Server — `Recalculate after import`;
- Power BI — `Recalculate after model load`;
- HTML — `Calculated in browser`;
- Match — `Pending cross-tool run`.

Therefore this repository currently provides a **cross-tool validation framework**, not proof that every tool has been freshly runtime-reconciled.

## Recommended validation procedure

For each KPI:

1. calculate the committed CSV/Python baseline;
2. import the synthetic CSV into SQL Server and calculate the equivalent metric;
3. if a Power BI runtime model is built, calculate the DAX measure;
4. inspect the HTML dashboard under equivalent filters;
5. compare the same definition and rounding;
6. mark Match = Yes only when evidence exists.

Recommended comparison columns:

`Metric | CSV/Python | SQL Server | Power BI | HTML | Match`

Do not force agreement by manually editing values. Differences should be resolved through source grain, filters, data types, business definitions or rounding.
