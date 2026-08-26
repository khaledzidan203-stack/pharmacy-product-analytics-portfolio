# Analytical Methodology

1. **Schema inspection** — verify row grain, keys, analytical fields, and data types.
2. **Data quality** — check duplicates, nulls, invalid Status values, and formula consistency.
3. **Clean master logic** — standardize Status and derive Sales, Profit, Inventory, Zero Sales, Risk, and Price Range fields.
4. **Descriptive analysis** — quantify SKU status, Category distribution, TGM, sales, profit, and suppliers.
5. **Risk analysis** — isolate Active zero-sales SKUs and size the associated inventory-value proxy.
6. **Ranking** — rank SKU performance by Sales Quantity and Profit Value within Category.
7. **Concentration analysis** — detect Sub-Categories with one Active supplier.
8. **Cross-tool validation** — compare the same KPI definitions in SQL Server, Power BI, HTML, and the checked-in example outputs.
9. **Business interpretation** — pair each finding with an action such as assortment review, stock rebalancing, supplier diversification, or margin review.
