USE PharmacyPortfolioDB;
GO
-- Row count
SELECT COUNT(*) AS Row_Count FROM dbo.PharmacyProducts;
-- Duplicate SKU check (should return zero rows)
SELECT SKU, COUNT(*) AS Duplicate_Count
FROM dbo.PharmacyProducts GROUP BY SKU HAVING COUNT(*) > 1;
-- Null checks for analytical keys
SELECT
    SUM(CASE WHEN SKU IS NULL OR LTRIM(RTRIM(SKU))='' THEN 1 ELSE 0 END) AS Missing_SKU,
    SUM(CASE WHEN Category IS NULL OR LTRIM(RTRIM(Category))='' THEN 1 ELSE 0 END) AS Missing_Category,
    SUM(CASE WHEN Supplier_Name IS NULL OR LTRIM(RTRIM(Supplier_Name))='' THEN 1 ELSE 0 END) AS Missing_Supplier
FROM dbo.PharmacyProducts;
-- Invalid status
SELECT Status, COUNT(*) AS Rows FROM dbo.PharmacyProducts
GROUP BY Status HAVING Status NOT IN ('Active','Blocked');
-- Derived-field validation
SELECT TOP (100) SKU, Sales_Value, RSP * Sales_Qty AS Expected_Sales_Value
FROM dbo.PharmacyProducts
WHERE ABS(Sales_Value - (RSP * Sales_Qty)) > 0.01;
GO
