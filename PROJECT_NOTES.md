# Project Notes

## Purpose

This repository demonstrates a governed pharmacy product and assortment analytics workflow using deterministic synthetic SKU-level data.

## Core design choices

1. **Synthetic-first publication** — all product, supplier, manufacturer and commercial values are generated and non-production.
2. **Single governed analytical grain** — one synthetic SKU per row.
3. **Cross-tool consistency** — Python, Excel, SQL and HTML use the same public KPI definitions.
4. **Explicit implementation boundaries** — Power BI is a design blueprint, not a claimed runtime artifact.
5. **Reproducibility** — fixed seed `20260826` plus deterministic output regeneration.
6. **Conservative financial interpretation** — Inventory Risk is a retail-value analytical proxy, not a write-off.
7. **Category-aware ranking** — Top-N logic is performed within Category rather than globally.
8. **Supplier concentration review** — single-supplier flags are decision-support signals, not automatic sourcing actions.

## Implemented layers

- deterministic synthetic data generation;
- Python validation and output generation;
- Excel analytical workbook;
- SQL Server implementation artifacts;
- interactive HTML dashboard;
- automated GitHub Actions validation;
- Power BI design reference.

## Current evidence boundary

The cross-tool validation checklist still records SQL, Power BI and HTML comparison status as pending. The repository therefore does not claim full fresh runtime reconciliation across every tool.

## Scaling path

A larger production-style version would typically move from the flat SKU-grain clean master into governed product, supplier, category, inventory and sales facts/dimensions with explicit time grain and incremental refresh.
