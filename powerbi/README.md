# Power BI Design Blueprint

> **Implementation status — design/reference only.** This repository does not include a committed PBIP, PBIR, TMDL or PBIX runtime implementation.

The files in this directory describe how the synthetic SKU-grain analytical model could be reproduced in Power BI Desktop.

## Included design artifacts

- `measures.dax` — proposed KPI measures
- `power_query_m.md` — proposed Power Query preparation
- `Pharmacy_Portfolio_Theme.json` — report theme
- this build guide

## Recommended pages

1. Executive Overview
2. Category & TGM Analysis
3. Zero Sales & Inventory Risk
4. Top 20 Performers
5. Supplier Dependency

## Validation baseline

Expected synthetic KPI values are stored in:

`../outputs/kpi_summary.csv`

The cross-tool checklist is stored in:

`../outputs/validation_summary.csv`

That checklist currently marks Power BI as **Pending cross-tool run**. Therefore these design files must not be interpreted as evidence that a Power BI model was built, refreshed or reconciled in Desktop.

## Future implementation rule

If a PBIP/PBIR/TMDL implementation is added later, it should reconcile the saved DAX results to the Python/CSV baseline before runtime validation is claimed.
