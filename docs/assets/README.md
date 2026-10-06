# Presentation Assets

This directory contains presentation-only visual assets for the Pharmacy Product & Assortment Analytics project.

## Intended use

The primary overview image stored here is used by the repository README to summarize the analytical workflow at a glance.

Recommended filename:

`pharmacy_product_assortment_analytics_overview.png`

The overview should represent only repository-supported claims, including:

- fully synthetic SKU-level pharmacy product data;
- 1,500 SKUs at product-master grain;
- Active vs Blocked assortment analysis;
- Sales Quantity, Sales Value, Profit Value, and Average Active TGM%;
- Active zero-sales SKU identification;
- inventory-risk proxy based on retail value;
- Top 20 ranking within Category;
- supplier concentration and single-supplier dependency analysis;
- deterministic Python data generation and repository validation;
- reproducible example outputs;
- Excel analytical workbook;
- SQL Server schema, quality checks, views, and analytical queries;
- interactive HTML/CSS/JavaScript dashboard;
- Power BI DAX / Power Query / theme as a design blueprint only.

## Evidence boundary

Assets in this directory are presentation summaries only. They are not source data, runtime validation evidence, SQL execution evidence, Excel formula evidence, or Power BI runtime evidence.

Authoritative claims remain defined by the committed synthetic CSV, Python generator and validators, checked-in example outputs, SQL scripts, Excel workbook, HTML dashboard, KPI/methodology documentation, and GitHub Actions workflow.
