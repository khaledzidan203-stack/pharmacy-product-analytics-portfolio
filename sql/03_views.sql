USE PharmacyPortfolioDB;
GO
CREATE OR ALTER VIEW dbo.vw_kpi_summary AS
SELECT
    COUNT(*) AS Total_SKUs,
    SUM(CASE WHEN Status='Active' THEN 1 ELSE 0 END) AS Active_SKUs,
    SUM(CASE WHEN Status='Blocked' THEN 1 ELSE 0 END) AS Blocked_SKUs,
    CAST(100.0*SUM(CASE WHEN Status='Active' THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0) AS decimal(6,2)) AS Active_Pct,
    SUM(Sales_Qty) AS Total_Sales_Qty,
    SUM(Sales_Value) AS Total_Sales_Value,
    SUM(Profit_Value) AS Total_Profit_Value,
    AVG(CASE WHEN Status='Active' THEN TGM_Pct END) AS Avg_Active_TGM_Pct,
    SUM(CASE WHEN Zero_Sales_Flag='Active Zero Sales' THEN 1 ELSE 0 END) AS Zero_Sales_Active_SKUs,
    SUM(Inventory_Risk_Value) AS Inventory_Financial_Risk
FROM dbo.PharmacyProducts;
GO
CREATE OR ALTER VIEW dbo.vw_category_overview AS
SELECT Category, COUNT(*) Total_SKUs,
       SUM(CASE WHEN Status='Active' THEN 1 ELSE 0 END) Active_SKUs,
       SUM(Sales_Qty) Sales_Qty, SUM(Sales_Value) Sales_Value,
       SUM(Profit_Value) Profit_Value, SUM(Inventory_Risk_Value) Inventory_Risk_Value
FROM dbo.PharmacyProducts GROUP BY Category;
GO
CREATE OR ALTER VIEW dbo.vw_tgm_by_category AS
SELECT Category, AVG(TGM_Pct) Avg_Active_TGM_Pct
FROM dbo.PharmacyProducts WHERE Status='Active' GROUP BY Category;
GO
CREATE OR ALTER VIEW dbo.vw_zero_sales_risk AS
SELECT SKU, Item_Name, Category, Sub_Category, Supplier_Name, RSP, SOH,
       Inventory_Value, Inventory_Risk_Value, Price_Range
FROM dbo.PharmacyProducts WHERE Status='Active' AND Sales_Qty=0;
GO
CREATE OR ALTER VIEW dbo.vw_supplier_analysis AS
SELECT Supplier_Name,
       SUM(CASE WHEN Status='Active' THEN 1 ELSE 0 END) Active_SKUs,
       SUM(Sales_Qty) Sales_Qty, SUM(Sales_Value) Sales_Value,
       SUM(Profit_Value) Profit_Value, SUM(Inventory_Risk_Value) Inventory_Risk_Value
FROM dbo.PharmacyProducts GROUP BY Supplier_Name;
GO
CREATE OR ALTER VIEW dbo.vw_single_supplier_dependency AS
WITH x AS (
    SELECT Sub_Category, COUNT(DISTINCT Supplier_Name) Supplier_Count,
           COUNT(*) Active_SKUs, SUM(Sales_Qty) Sales_Qty
    FROM dbo.PharmacyProducts WHERE Status='Active'
    GROUP BY Sub_Category
)
SELECT p.Sub_Category, x.Active_SKUs, x.Supplier_Count, MIN(p.Supplier_Name) Supplier_Name, x.Sales_Qty
FROM x JOIN dbo.PharmacyProducts p ON p.Sub_Category=x.Sub_Category AND p.Status='Active'
WHERE x.Supplier_Count=1
GROUP BY p.Sub_Category,x.Active_SKUs,x.Supplier_Count,x.Sales_Qty;
GO
