# Power BI Build Guide

This repository does **not** include a fabricated `.pbix` binary. Build the report in Power BI Desktop from the reproducible synthetic CSV.

Recommended pages:
1. **Executive Overview** — KPI cards, Active vs Blocked, category sales, overall risk.
2. **Category & TGM Analysis** — category distribution and average Active TGM%.
3. **Zero Sales & Inventory Risk** — zero-sales SKUs by category, supplier, and price range.
4. **Top 20 Performers** — Top 20 by Sales Quantity and Profit Value, with category slicer.
5. **Supplier Dependency** — Active SKUs and Sales by supplier; single-supplier sub-category table.

Use `measures.dax`, `power_query_m.md`, and `Pharmacy_Portfolio_Theme.json`. The expected KPI values for validation are in `outputs/kpi_summary.csv`.
