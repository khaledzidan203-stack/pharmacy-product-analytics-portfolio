# Business Requirements

## Business problem
A pharmacy-category team needs a repeatable way to understand assortment status, sales performance, gross-margin quality, non-moving active items, inventory exposure, top-performing items, and supplier concentration.

## Functional requirements
- Count Total, Active, and Blocked SKUs.
- Show distribution across five product categories.
- Calculate average TGM% by Category for Active products only.
- Identify Active SKUs with zero sales.
- Segment zero-sales exposure by Category, Supplier, and Price Range.
- Estimate an Inventory Financial Risk proxy for Active zero-sales stock.
- Rank products by Sales Quantity and Profit Value.
- Return Top 20 items per Category for both rankings.
- Analyze Active SKUs and Sales by Supplier.
- Flag Sub-Categories supplied by only one supplier among Active items.
- Validate results across CSV/Python, SQL Server, Power BI, and HTML.

## Non-functional requirements
- No proprietary production data in the public repository.
- Reproducible synthetic sample data.
- Clear KPI definitions and calculation rules.
- Recruiter-friendly documentation and self-contained HTML demo.
