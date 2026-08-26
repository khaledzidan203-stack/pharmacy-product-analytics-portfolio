USE PharmacyPortfolioDB;
GO
IF OBJECT_ID('dbo.PharmacyProducts','U') IS NOT NULL DROP TABLE dbo.PharmacyProducts;
GO
CREATE TABLE dbo.PharmacyProducts (
    SKU varchar(20) NOT NULL PRIMARY KEY,
    Item_Name nvarchar(120) NOT NULL,
    Status varchar(10) NOT NULL CHECK (Status IN ('Active','Blocked')),
    Creation_Month char(7) NULL,
    RSP decimal(12,2) NOT NULL,
    TGM_Pct decimal(8,4) NULL,
    Category nvarchar(80) NOT NULL,
    Sub_Category nvarchar(80) NOT NULL,
    Manufacturer_Code varchar(20) NULL,
    Manufacturer_Name nvarchar(100) NULL,
    Supplier_Code varchar(20) NULL,
    Supplier_Name nvarchar(100) NULL,
    Regulatory_Code varchar(30) NULL,
    Scientific_Name nvarchar(120) NULL,
    Legal_Status nvarchar(40) NULL,
    Purchase_Qty int NOT NULL,
    Sales_Qty int NOT NULL,
    SOH int NOT NULL,
    Sales_Value decimal(18,2) NOT NULL,
    Profit_Value decimal(18,2) NOT NULL,
    Inventory_Value decimal(18,2) NOT NULL,
    Zero_Sales_Flag varchar(30) NOT NULL,
    Inventory_Risk_Value decimal(18,2) NOT NULL,
    Price_Range varchar(30) NOT NULL,
    Is_Active bit NOT NULL
);
GO
/* Import data/sample_pharmacy_products.csv with SSMS Import Flat File or your preferred ETL tool. */
