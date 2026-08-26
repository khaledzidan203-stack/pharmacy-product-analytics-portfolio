/* Portfolio-safe SQL Server setup. Run with sufficient permissions. */
IF DB_ID('PharmacyPortfolioDB') IS NULL
    CREATE DATABASE PharmacyPortfolioDB;
GO
USE PharmacyPortfolioDB;
GO
