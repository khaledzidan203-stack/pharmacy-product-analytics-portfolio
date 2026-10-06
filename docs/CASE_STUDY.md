# Case Study — Pharmacy Product & Assortment Intelligence

## Context

Product and category teams need to manage assortment breadth, sales contribution, margin quality, non-moving stock and supplier concentration at the same time.

This project implements those questions on a deterministic synthetic pharmacy product master containing 1,500 SKU-level records.

## Analytical challenge

The model answers:

1. Which SKUs are Active versus Blocked?
2. Which categories generate the most Sales Value and Profit Value?
3. Which Active categories have the strongest average TGM?
4. Which Active SKUs have zero sales and still carry stock?
5. What retail-value inventory-risk proxy is associated with those SKUs?
6. Which products rank highest within each Category?
7. Which Sub-Categories rely on only one Active supplier?

## Data design

One row represents one synthetic SKU with aggregated demonstration-period fields.

The flat analytical master intentionally supports easy reconciliation between Python, Excel, SQL and HTML. It is not presented as a star schema.

## Governed formulas

- Sales Value = RSP × Sales Quantity
- Profit Value = Sales Value × TGM %
- Inventory Value = RSP × SOH
- Active Zero Sales = Active AND Sales Quantity = 0
- Inventory Risk Value = Inventory Value for Active zero-sales SKUs

Inventory Risk is explicitly a **retail-value proxy**, not a write-off or accounting loss.

## Current baseline

The deterministic sample produces:

- 1,500 SKUs
- 1,225 Active SKUs
- 275 Blocked SKUs
- 37,488 units sold
- SAR 3,722,472.10 Sales Value
- SAR 1,249,396.70 Profit Value
- 33.51% Average Active TGM
- 129 Active zero-sales SKUs
- SAR 406,473.61 inventory-risk proxy
- 3 single-supplier dependencies

## Category findings

Personal Care leads Sales Value, Profit Value and Average Active TGM in the current sample.

Medical Devices carries the highest category-level Active zero-sales inventory-risk proxy.

These are synthetic observations only.

## Cross-tool architecture

Python creates the baseline and reproducibility contract.

Excel provides a formula-driven analytical workbook.

SQL Server provides data-quality checks, views, window-function Top-N ranking and analysis queries.

HTML provides the implemented interactive dashboard.

Power BI is documented as a design blueprint only.

## Validation hardening

The release now verifies that:

- the fixed-seed generator recreates the committed CSV byte-for-byte;
- the checked-in analytical outputs rebuild deterministically;
- KPI baselines remain unchanged;
- presentation files do not overstate Power BI or cross-tool runtime evidence.

## Outcome

The project demonstrates a governed assortment-analysis pattern:

**SKU status → commercial performance → margin quality → zero-sales risk → ranking → supplier concentration → action review.**
