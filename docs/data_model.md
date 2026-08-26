# Data Model

The public portfolio uses a single denormalized analytical table named `PharmacyProducts`. This intentionally mirrors a clean-master-dataset approach suitable for cross-tool validation.

## Grain
One row = one synthetic SKU/product master record with aggregated quantity/value fields for the demonstration period.

## Core dimensions
`SKU`, `Item_Name`, `Status`, `Category`, `Sub_Category`, `Supplier`, `Manufacturer`, `Price_Range`, and `Creation_Month`.

## Core facts
`Sales_Qty`, `Sales_Value`, `Profit_Value`, `SOH`, `Inventory_Value`, `Inventory_Risk_Value`, and `TGM_Pct`.

## Derived rules
- `Sales_Value = RSP × Sales_Qty`
- `Profit_Value = Sales_Value × TGM_Pct`
- `Inventory_Value = RSP × SOH` (retail-value demonstration proxy)
- `Zero_Sales_Flag = Active Zero Sales` only when `Status = Active` and `Sales_Qty = 0`
- `Inventory_Risk_Value = Inventory_Value` for Active zero-sales SKUs, otherwise 0
- `Price_Range`: Low `<25`, Medium `25–99`, High `100–299`, Premium `300+`

The risk calculation is a portfolio demonstration metric, not an accounting valuation or write-off estimate.
