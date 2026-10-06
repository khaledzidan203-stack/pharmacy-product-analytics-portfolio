# Pharmacy Product & Assortment Analytics

## SKU Performance, Zero-Sales Risk, Margin Quality & Supplier Dependency

[![Repository Validation](https://github.com/khaledzidan203-stack/pharmacy-product-analytics-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/khaledzidan203-stack/pharmacy-product-analytics-portfolio/actions/workflows/validate.yml)
[![Deploy static dashboard to GitHub Pages](https://github.com/khaledzidan203-stack/pharmacy-product-analytics-portfolio/actions/workflows/pages.yml/badge.svg)](https://github.com/khaledzidan203-stack/pharmacy-product-analytics-portfolio/actions/workflows/pages.yml)

**Live dashboard:** https://khaledzidan203-stack.github.io/pharmacy-product-analytics-portfolio/

Pharmacy Product & Assortment Analytics is a synthetic, SKU-level analytical implementation for evaluating assortment status, sales, profit, margin quality, zero-sales inventory risk, top performers and supplier concentration across multiple analytical tools.

> **Data boundary:** every SKU, product name, supplier, manufacturer, regulatory code, quantity and financial value in this repository is synthetic. No proprietary pharmacy master data, customer data, patient data, prescription data, credentials or internal business-system data is included.

<img src="docs/assets/Pharmacy%20Analytics%20Dashboard%20Overview.png" alt="Pharmacy Product and Assortment Analytics overview" width="100%">

> **Visual evidence note:** the infographic is a presentation schematic. Exact KPI values, tool boundaries and implementation status are governed by the source files, checked-in outputs and validation documentation below.

**Start here:** [Case study](docs/CASE_STUDY.md) · [Technical walkthrough](docs/TECHNICAL_WALKTHROUGH.md) · [Evidence map](docs/PROJECT_EVIDENCE_MAP.md) · [Project index](docs/PROJECT_INDEX.md) · [Final validation](docs/FINAL_RELEASE_VALIDATION.md)

## Project at a glance

| Area | Current implementation |
|---|---|
| Analytical grain | One synthetic SKU per row |
| Synthetic dataset | 1,500 SKUs generated with fixed seed `20260826` |
| Active assortment | 1,225 SKUs (81.67%) |
| Blocked assortment | 275 SKUs (18.33%) |
| Sales quantity | 37,488 units |
| Sales value | SAR 3,722,472.10 |
| Profit value | SAR 1,249,396.70 |
| Average Active TGM% | 33.51% arithmetic average across Active SKUs |
| Active zero-sales SKUs | 129 |
| Inventory-risk proxy | SAR 406,473.61 |
| Supplier dependency | 3 sub-categories with one Active supplier |
| Python | deterministic data generator, output builder and repository validation |
| Excel | checked-in analytical workbook |
| SQL Server | schema, quality checks, views, analysis queries + example output workbook |
| HTML | interactive filterable dashboard |
| Power BI | DAX / Power Query / theme / build guide only; no PBIP/PBIR/TMDL/PBIX runtime artifact |
| CI | automated schema/formula/privacy/reproducibility checks |
| Deployment | GitHub Pages static dashboard deployment |

## Business problem

A product or category team needs to understand more than total sales. Assortment decisions require a consistent view of:

- which SKUs are Active versus Blocked;
- which categories drive Sales Value and Profit Value;
- where margin quality is strongest or weakest;
- which Active products have zero sales while still carrying stock;
- which SKUs rank highest within their categories;
- where supplier concentration creates dependency;
- which findings merit assortment, replenishment, transfer, supplier or margin review.

This repository implements those questions from one public synthetic clean-master dataset.

## End-to-end analytical flow

```text
Deterministic Synthetic SKU Master
        ↓
Schema + Data Quality Validation
        ↓
Derived Commercial Metrics
Sales · Profit · Inventory Value · Zero-Sales Flag · Risk Proxy · Price Band
        ↓
Product / Category Analytics
        ↓
Top-N Ranking + Supplier Dependency
        ↓
┌────────────┬────────────┬────────────┬────────────┐
│   Python   │   Excel    │ SQL Server │    HTML    │
│ baseline   │ workbook   │ reference  │ dashboard  │
└────────────┴────────────┴────────────┴────────────┘
        ↓
Power BI Design Blueprint
        ↓
Business Findings & Action Review
```

The checked-in CSV is the public analytical source-of-truth for reproducible sample results.

## Data model

The project intentionally uses a single denormalized analytical table, `PharmacyProducts`, at **SKU grain**.

This is not presented as a dimensional star schema. The flat clean-master structure is deliberate because it keeps business rules easy to reconcile across Python, SQL, Excel, HTML and the Power BI design reference.

### Core dimensions

- SKU
- Item Name
- Status
- Category / Sub-Category
- Supplier
- Manufacturer
- Creation Month
- Price Range
- Legal Status

### Core measures

- Sales Quantity
- Sales Value
- Profit Value
- Stock on Hand
- Inventory Value
- Inventory Risk Value
- TGM %

## Governed derived rules

The public model uses the following generalized rules:

```text
Sales Value      = RSP × Sales Quantity
Profit Value     = Sales Value × TGM %
Inventory Value  = RSP × SOH
Zero-Sales Flag  = Active AND Sales Quantity = 0
Inventory Risk   = Inventory Value for Active zero-sales SKUs; otherwise 0
```

**Inventory Risk Value is a retail-value analytical proxy. It is not an accounting write-off, impairment estimate or confirmed loss.**

## KPI framework

| KPI | Definition |
|---|---|
| Total SKUs | Distinct SKU count |
| Active SKUs | SKUs where Status = Active |
| Active % | Active SKUs / Total SKUs |
| Total Sales Quantity | Sum of Sales_Qty |
| Total Sales Value | Sum of Sales_Value |
| Total Profit Value | Sum of Profit_Value |
| Average Active TGM% | Arithmetic average of TGM_Pct across Active SKUs |
| Active Zero-Sales SKUs | Active SKUs where Sales_Qty = 0 |
| Inventory Financial Risk | Sum of Inventory_Risk_Value for Active zero-sales SKUs |
| Supplier Dependency | Sub-Category has exactly one distinct supplier among Active SKUs |

The Average Active TGM% is **not sales-weighted**.

## Current synthetic findings

The retained reproducible sample demonstrates:

- **1,500** total SKUs;
- **1,225 Active** and **275 Blocked** SKUs;
- **37,488** units sold;
- **SAR 3,722,472.10** Sales Value;
- **SAR 1,249,396.70** Profit Value;
- **33.51%** Average Active TGM%;
- **129** Active zero-sales SKUs;
- **SAR 406,473.61** inventory-risk proxy;
- **3** single-supplier sub-category dependencies.

### Category examples

Personal Care currently leads the synthetic sample in:

- Sales Value: **SAR 1,042,231.43**
- Profit Value: **SAR 401,035.70**
- Average Active TGM%: **38.68%**

Medical Devices has the highest category-level Active zero-sales inventory-risk proxy at **SAR 112,798.82**.

These are synthetic sample observations only.

## Top-N ranking

The SQL implementation uses window-function ranking within Category so each category can return its own Top 20 rather than using one global ranking.

Conceptually:

```sql
ROW_NUMBER() OVER (
    PARTITION BY Category
    ORDER BY Sales_Qty DESC
)
```

A parallel ranking is produced for Profit Value.

## Supplier dependency

A sub-category is flagged when its Active assortment has exactly one distinct supplier.

The current synthetic sample contains:

- Home Diagnostics → Supplier 003
- Mobility Aids → Supplier 011
- Travel Health → Supplier 019

This is a concentration signal for review, not an automatic sourcing decision.

## Implemented analytical layers

### Python

Python standard-library scripts provide:

- deterministic synthetic generation;
- schema/formula/privacy validation;
- checked-in example-output generation;
- reproducibility verification.

### Excel

`excel/Pharmacy_Assessment_Excel_Analysis.xlsx` is a checked-in analytical workbook covering clean data, KPIs, category/TGM analysis, zero-sales risk, Top 20, suppliers, findings and dashboard-oriented outputs.

### SQL Server

`sql/` contains:

1. database creation;
2. analytical table schema;
3. quality checks;
4. views;
5. analytical queries.

`sql/Pharmacy_Assessment_SQL_Outputs.xlsx` contains example exported result sets from the same synthetic analytical design.

### HTML / JavaScript

The root `index.html` and `src/dashboard.js` implement a filterable browser dashboard with:

- Status filter;
- Category filter;
- Supplier filter;
- Price Range filter;
- compatible CSV upload;
- KPI cards;
- category sales and TGM analysis;
- zero-sales risk;
- Top Items;
- supplier-dependency analysis;
- dynamic findings.

### Power BI boundary

`powerbi/` contains:

- `measures.dax`
- `power_query_m.md`
- theme JSON
- build guide

There is currently **no committed PBIP, PBIR, TMDL or PBIX implementation**.

Power BI is therefore a **design blueprint**, not runtime evidence.

## Cross-tool validation boundary

The project defines a cross-tool validation framework, but `outputs/validation_summary.csv` currently records SQL, Power BI and HTML comparison as **Pending cross-tool run**.

Therefore the repository does **not** claim that all tools have been freshly runtime-reconciled.

Current evidence supports:

- Python/CSV baseline generation;
- SQL implementation artifacts and example exported outputs;
- Excel workbook artifact;
- implemented HTML dashboard;
- Power BI design specifications.

See [Cross-Tool Validation](docs/cross_tool_validation.md).

## Automated validation

GitHub Actions now checks:

- exact 1,500-row dataset contract;
- unique SKU;
- expected schema;
- row-level commercial formulas;
- Active zero-sales flag logic;
- secret-like patterns;
- fixed synthetic-data seed;
- deterministic regeneration of the committed CSV;
- deterministic regeneration of checked-in analytical output files;
- retained KPI baselines;
- required project/evidence files;
- Python compilation.

## Dashboard

![Dashboard overview](screenshots/dashboard_overview.png)

This screenshot is evidence of the implemented synthetic-data HTML dashboard.

## Quick Start

### Run the browser dashboard

```bash
python -m http.server 8000
```

Then open:

`http://localhost:8000`

### Validate the repository

```bash
python scripts/validate_repository.py
python scripts/check_reproducibility.py
```

No third-party Python packages are required.

### Rebuild example outputs

```bash
python scripts/build_example_outputs.py
```

## Repository structure

```text
data/                 synthetic clean-master dataset + data dictionary
scripts/              generation, validation and output-building logic
outputs/              retained analytical outputs
excel/                analytical workbook
sql/                  SQL Server implementation + example exports
src/                  HTML dashboard JavaScript/CSS
powerbi/              Power BI design blueprint
screenshots/          implemented dashboard evidence
docs/                 methodology, contracts and release evidence
docs/assets/          presentation assets
.github/workflows/    automated repository validation
```

## Documentation

- [Project Index](docs/PROJECT_INDEX.md)
- [Case Study](docs/CASE_STUDY.md)
- [Technical Walkthrough](docs/TECHNICAL_WALKTHROUGH.md)
- [Project Evidence Map](docs/PROJECT_EVIDENCE_MAP.md)
- [Architecture](docs/architecture.md)
- [Analytical Methodology](docs/analytical_methodology.md)
- [Data Model](docs/data_model.md)
- [KPI Definitions](docs/kpi_definitions.md)
- [Cross-Tool Validation](docs/cross_tool_validation.md)
- [Data Privacy](docs/data_privacy.md)
- [Final Release Validation](docs/FINAL_RELEASE_VALIDATION.md)

## Limitations

- All data is synthetic.
- The analytical model is flat and SKU-grained, not a star schema.
- The sample has no time-series sales fact, so trend/seasonality claims are not supported.
- Average Active TGM% is not weighted by sales.
- Inventory Risk Value is a retail-value proxy.
- SQL example outputs are retained artifacts rather than CI-executed SQL Server tests.
- Excel runtime formula recalc is not executed in GitHub Actions.
- Power BI is design-only.
- Full SQL/Power BI/HTML cross-tool runtime reconciliation is currently pending.

Licensed under the [MIT License](LICENSE).
