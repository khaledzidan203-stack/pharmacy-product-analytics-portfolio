# Environment Baseline

## Python

Repository scripts use Python standard-library functionality only.

Declared baseline:

- Python 3.10+
- GitHub Actions currently validates with Python 3.12

No third-party Python dependency installation is required.

## Synthetic generation

- fixed seed: `20260826`
- expected rows: 1,500
- output: `data/sample_pharmacy_products.csv`

## Excel

The analytical workbook is retained as:

`excel/Pharmacy_Assessment_Excel_Analysis.xlsx`

Excel recalculation is not part of GitHub Actions.

## SQL Server

The repository contains T-SQL DDL, quality checks, views and analysis queries. SQL Server runtime execution is not part of GitHub Actions.

## HTML

The dashboard is static HTML/CSS/JavaScript and can be served through a simple local HTTP server.

## Power BI

Power BI files are design/reference assets only. No Desktop runtime implementation is committed.
