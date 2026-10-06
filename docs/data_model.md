# Data Model

The project uses one denormalized analytical table named `PharmacyProducts`.

## Grain

One row = one synthetic SKU/product-master record with aggregated quantity/value fields for the demonstration period.

This intentionally follows a clean-master analytical pattern suitable for cross-tool comparison. It is **not** presented as a dimensional star schema.

## Core dimensions

- SKU
- Item_Name
- Status
- Category
- Sub_Category
- Supplier
- Manufacturer
- Price_Range
- Creation_Month
- Legal_Status

## Core facts / analytical fields

- Sales_Qty
- Sales_Value
- Profit_Value
- SOH
- Inventory_Value
- Inventory_Risk_Value
- TGM_Pct

## Derived rules

- `Sales_Value = RSP × Sales_Qty`
- `Profit_Value = Sales_Value × TGM_Pct`
- `Inventory_Value = RSP × SOH`
- `Zero_Sales_Flag = Active Zero Sales` only when `Status = Active` and `Sales_Qty = 0`
- `Inventory_Risk_Value = Inventory_Value` for Active zero-sales SKUs, otherwise 0
- `Price_Range`: Low `<25`, Medium `25–99`, High `100–299`, Premium `300+`

## Interpretation boundary

Inventory Value uses retail selling price as a demonstration value proxy.

Inventory Risk Value is an analytical retail-value exposure proxy, not an accounting valuation, impairment or write-off estimate.
