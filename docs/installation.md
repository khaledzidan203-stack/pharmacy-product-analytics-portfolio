# Installation / Setup

## HTML dashboard
1. Clone or download the repository.
2. From the repository root run `python -m http.server 8000`.
3. Open `http://localhost:8000` in a browser.

## Python validation
Requires Python 3.10+ and no third-party packages.
- Run `python scripts/validate_repository.py`.
- Run `python scripts/build_example_outputs.py` to rebuild the KPI summary.

## Excel
Open `excel/Pharmacy_Assessment_Excel_Analysis.xlsx`. All sheets are based on the public synthetic dataset.

## SQL Server
1. Run `sql/00_create_database.sql`.
2. Run `sql/01_create_schema.sql`.
3. Import `data/sample_pharmacy_products.csv` into `dbo.PharmacyProducts` using SSMS Import Flat File or your preferred ETL method.
4. Run quality checks, then views, then analytical queries.

## Power BI Desktop
Load the sample CSV, follow `powerbi/power_query_m.md`, add `powerbi/measures.dax`, apply the theme JSON, and build pages using `powerbi/README.md`.
