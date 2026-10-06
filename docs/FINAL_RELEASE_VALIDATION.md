# Final Release Validation

## Release scope

This release strengthens reproducibility, evidence boundaries and public presentation without changing the committed 1,500-row dataset, KPI formulas, SQL analytical logic, Excel workbook or retained analytical baseline.

## Fresh automated validation

GitHub Actions verifies:

- expected CSV schema;
- exactly 1,500 SKU rows;
- unique SKU;
- valid Status domain;
- Sales Value formula;
- Profit Value formula;
- Inventory Value formula;
- Active zero-sales flag logic;
- secret-pattern scan;
- retained KPI baseline;
- required presentation/evidence artifacts;
- deterministic regeneration of the committed CSV;
- deterministic regeneration of checked-in analytical outputs;
- Python source compilation.

## Current KPI baseline

- Total SKUs: 1,500
- Active SKUs: 1,225
- Blocked SKUs: 275
- Total Sales Quantity: 37,488
- Total Sales Value: SAR 3,722,472.10
- Total Profit Value: SAR 1,249,396.70
- Average Active TGM: 33.51%
- Active Zero-Sales SKUs: 129
- Inventory Financial Risk proxy: SAR 406,473.61

## Runtime boundaries

Python validation/reproducibility is executed in CI.

SQL Server is not provisioned in CI.

Excel workbook recalculation is not executed in CI.

The HTML dashboard is implemented and retained, but browser visual-regression testing is not part of CI.

Power BI is design-only and no runtime validation is claimed.

The cross-tool comparison file currently records non-Python comparisons as pending and is preserved as such.
