# Presentation Assets

This directory contains presentation-only visual assets for the Pharmacy Product & Assortment Analytics project.

## Current overview

`Pharmacy Analytics Dashboard Overview.png`

The root README uses this image as a high-level visual summary.

## Evidence-supported scope

The repository supports:

- 1,500 deterministic synthetic SKU records;
- Active / Blocked assortment analysis;
- Sales Quantity, Sales Value and Profit Value;
- arithmetic Average Active TGM%;
- Active zero-sales SKU analysis;
- retail-value inventory-risk proxy;
- category-level performance;
- Top-N product ranking;
- single-supplier Sub-Category dependency analysis;
- deterministic Python generation and validation;
- Excel analytical workbook;
- SQL Server implementation artifacts;
- interactive HTML dashboard;
- Power BI design/reference files.

## Evidence boundary

The infographic is a **presentation schematic**, not a literal screenshot of every implemented feature.

Exact tool status is governed by the repository:

- Python: implemented and executed in CI.
- Excel: workbook artifact retained.
- SQL Server: scripts and exported example output workbook retained; SQL runtime is not executed in CI.
- HTML: implemented dashboard.
- Power BI: design blueprint only; no PBIP/PBIR/TMDL/PBIX runtime implementation is committed.
- GitHub Pages: implemented through `.github/workflows/pages.yml`; deployment has completed successfully.

Any labels, counts or UI concepts shown in the graphic that are not explicitly supported by repository evidence should be treated as illustrative rather than authoritative.
