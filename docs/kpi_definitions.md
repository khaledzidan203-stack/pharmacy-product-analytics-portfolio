# KPI Definitions

| KPI | Definition |
|---|---|
| Total SKUs | Distinct count of SKU. |
| Active SKUs | Distinct SKUs where Status = Active. |
| Blocked SKUs | Distinct SKUs where Status = Blocked. |
| Active % | Active SKUs / Total SKUs. |
| Total Sales Quantity | Sum of Sales_Qty. |
| Total Sales Value | Sum of Sales_Value. |
| Total Profit Value | Sum of Profit_Value. |
| Average TGM% (Active) | Average TGM_Pct filtered to Active SKUs only. |
| Zero Sales Active SKUs | Active SKUs where Sales_Qty = 0. |
| Inventory Financial Risk | Sum of Inventory_Risk_Value for Active zero-sales SKUs. This is a retail-value risk proxy for the demo. |
| Supplier Dependency | Sub-Category has exactly one distinct Supplier among Active SKUs. |
| Top 20 by Sales Qty | `ROW_NUMBER()` within Category ordered by Sales_Qty descending. |
| Top 20 by Profit | `ROW_NUMBER()` within Category ordered by Profit_Value descending. |
