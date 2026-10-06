# Technical Walkthrough — 60–90 Seconds

**0–10 seconds — Scope**

This project analyzes 1,500 deterministic synthetic pharmacy SKUs for assortment status, sales, profit, margin quality, zero-sales inventory risk and supplier dependency.

**10–25 seconds — Data grain**

The central analytical table is one row per SKU. The same clean-master dataset feeds Python, Excel, SQL Server and the HTML dashboard.

**25–45 seconds — Derived logic**

The model derives Sales Value, Profit Value, Inventory Value, Active Zero-Sales flags, a retail-value Inventory Risk proxy and Price Range. Repository validation checks those formulas row by row.

**45–60 seconds — Analytical methods**

Category analysis compares sales, profit and Average Active TGM. Top-N analysis ranks products within Category. Supplier concentration flags Sub-Categories with exactly one supplier among Active SKUs.

**60–75 seconds — Reproducibility**

The generator uses fixed seed `20260826`. CI regenerates the synthetic CSV and checked-in example outputs and verifies that they remain identical to the committed artifacts.

**75–90 seconds — Tool boundary**

Excel, SQL Server and HTML artifacts are implemented and retained. Power BI includes DAX, Power Query, a theme and build guide, but no committed runtime report, so it is presented as a blueprint only.
