# Power Query M reference

Use **Get Data → Text/CSV** and point to `data/sample_pharmacy_products.csv`, then set the following types. Replace the placeholder path with your local clone path.

```powerquery
let
    Source = Csv.Document(File.Contents("<REPO_PATH>\\data\\sample_pharmacy_products.csv"),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(PromotedHeaders,{
        {"SKU", type text}, {"Item_Name", type text}, {"Status", type text},
        {"Creation_Month", type text}, {"RSP", Currency.Type}, {"TGM_Pct", Percentage.Type},
        {"Category", type text}, {"Sub_Category", type text}, {"Supplier_Name", type text},
        {"Purchase_Qty", Int64.Type}, {"Sales_Qty", Int64.Type}, {"SOH", Int64.Type},
        {"Sales_Value", Currency.Type}, {"Profit_Value", Currency.Type},
        {"Inventory_Value", Currency.Type}, {"Inventory_Risk_Value", Currency.Type},
        {"Is_Active", Int64.Type}
    })
in
    Types
```
