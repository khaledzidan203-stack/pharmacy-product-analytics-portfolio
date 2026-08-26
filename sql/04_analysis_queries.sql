USE PharmacyPortfolioDB;
GO
SELECT * FROM dbo.vw_kpi_summary;
SELECT * FROM dbo.vw_category_overview ORDER BY Sales_Value DESC;
SELECT * FROM dbo.vw_tgm_by_category ORDER BY Avg_Active_TGM_Pct DESC;
SELECT * FROM dbo.vw_zero_sales_risk ORDER BY Inventory_Risk_Value DESC;
SELECT * FROM dbo.vw_supplier_analysis ORDER BY Sales_Value DESC;
SELECT * FROM dbo.vw_single_supplier_dependency ORDER BY Active_SKUs DESC;

-- Top 20 items per category by Sales Quantity
WITH ranked AS (
    SELECT Category, SKU, Item_Name, Sales_Qty, Sales_Value, Profit_Value,
           ROW_NUMBER() OVER(PARTITION BY Category ORDER BY Sales_Qty DESC, Sales_Value DESC) AS rn
    FROM dbo.PharmacyProducts
)
SELECT * FROM ranked WHERE rn<=20 ORDER BY Category,rn;

-- Top 20 items per category by Profit Value
WITH ranked AS (
    SELECT Category, SKU, Item_Name, Profit_Value, Sales_Qty, Sales_Value,
           ROW_NUMBER() OVER(PARTITION BY Category ORDER BY Profit_Value DESC, Sales_Value DESC) AS rn
    FROM dbo.PharmacyProducts
)
SELECT * FROM ranked WHERE rn<=20 ORDER BY Category,rn;
GO
