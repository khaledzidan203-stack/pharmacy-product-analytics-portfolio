# PORTFOLIO_NOTES

## What I personally built
I designed the end-to-end analytical workflow represented in this repository: data-cleaning logic, KPI definitions, risk segmentation, Top-20 ranking logic, supplier dependency analysis, SQL view structure, Power BI measure/report specification, cross-tool validation approach, and the interactive HTML dashboard. The public repository intentionally recreates the analytical capability using synthetic data rather than publishing any proprietary dataset.

## Analytical skills demonstrated
- Data profiling and quality-control design.
- Clean Master Dataset design and derived-field logic.
- KPI calculation and metric-definition governance.
- Category, margin, sales, profit, and inventory-risk analysis.
- Zero-sales segmentation by Category, Supplier, and Price Range.
- Window-function ranking for Top 20 items per Category.
- Supplier concentration and dependency analysis.
- Cross-tool validation across SQL, Power BI, HTML, and a reproducible CSV baseline.

## Business problems solved
- Distinguish Active versus Blocked assortment.
- Identify Active items that are not selling.
- Size the inventory-value exposure associated with non-moving Active stock.
- Find product/category leaders using Sales Quantity and Profit Value.
- Compare category margin quality using Active-only TGM%.
- Identify Sub-Categories that depend entirely on one supplier.
- Convert analysis into executive-friendly dashboards and action-oriented findings.

## Technologies used
Excel/Power Query methodology, SQL Server, Power BI/DAX, HTML/CSS/JavaScript, Python standard library, GitHub Actions, and Git/GitHub.

## Interview points I can discuss
- Why a Clean Master Dataset is useful for cross-tool consistency.
- Why Average TGM% is filtered to Active SKUs only.
- How I defined and validated Active Zero Sales.
- Why inventory risk is explicitly labeled a **proxy** rather than an accounting write-off.
- How `ROW_NUMBER() OVER (PARTITION BY Category ...)` solves Top-20-per-Category ranking.
- How I detect single-supplier dependency with `COUNT(DISTINCT Supplier)`.
- How I would scale this from a flat analytical table to a star schema.
- How I prevent confidential source data and credentials from entering a public portfolio repository.
- How I reconcile metric differences caused by filter context, data types, or rounding across analytical tools.

## Demonstrable sample results
For the included synthetic dataset only: Total SKUs = 1,500, Active SKUs = 1,225, Active zero-sales SKUs = 129, and the inventory-risk proxy = SAR 406,474. These values can be independently reproduced from `data/sample_pharmacy_products.csv`.
