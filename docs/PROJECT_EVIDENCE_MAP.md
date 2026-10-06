# Project Evidence Map

| Claim | Primary evidence | Evidence type |
|---|---|---|
| 1,500 synthetic SKUs | `data/sample_pharmacy_products.csv`, validator | Data + automated check |
| Fixed seed 20260826 | `scripts/generate_synthetic_data.py` | Source |
| 1,225 Active / 275 Blocked | `outputs/kpi_summary.csv` | Retained output |
| 37,488 sales units | `outputs/kpi_summary.csv` | Retained output |
| SAR 3,722,472.10 Sales Value | KPI output + formula validator | Output + validation |
| SAR 1,249,396.70 Profit Value | KPI output + formula validator | Output + validation |
| 33.51% Average Active TGM | KPI output | Retained output |
| 129 Active zero-sales SKUs | KPI output + zero-sales rule validation | Output + validation |
| SAR 406,473.61 inventory-risk proxy | KPI output | Retained output |
| 3 single-supplier dependencies | `single_supplier_dependency.csv` | Retained output |
| Personal Care leads Sales Value | `category_analysis.csv` | Retained output |
| Medical Devices highest risk proxy | `category_analysis.csv` | Retained output |
| Top 20 within Category | `sql/03_views.sql`, retained Top-20 outputs | SQL + output |
| Excel analytical workbook exists | `excel/Pharmacy_Assessment_Excel_Analysis.xlsx` | Artifact |
| SQL Server implementation exists | `sql/*.sql` + SQL output workbook | Source + artifact |
| HTML dashboard implemented | `index.html`, `src/dashboard.js`, screenshot | Runtime artifact |
| Power BI runtime implementation | No PBIP/PBIR/TMDL/PBIX committed | **Not claimed** |
| Full fresh cross-tool runtime reconciliation | `validation_summary.csv` says Pending cross-tool run | **Not claimed** |

## Evidence rule

Presentation images summarize the system but are not runtime proof. Claims are tied to committed data, executable source, retained outputs or implementation artifacts.
