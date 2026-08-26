#!/usr/bin/env python3
"""Generate the public synthetic Clean Master Dataset deterministically.

No production or proprietary data is read. Running this script recreates
`data/sample_pharmacy_products.csv` from a fixed random seed.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data' / 'sample_pharmacy_products.csv'
SEED = 20260826
N = 1500

CATEGORIES = {
    'OTC & Wellness': ['Pain Relief','Cold & Allergy','Digestive Care','Vitamins'],
    'Personal Care': ['Skin Care','Hair Care','Oral Care','Hygiene'],
    'Medical Devices': ['Home Diagnostics','First Aid','Mobility Aids','Monitoring Supplies'],
    'Nutrition': ['Adult Nutrition','Sports Nutrition','Healthy Snacks','Hydration'],
    'General Merchandise': ['Baby Essentials','Travel Health','Seasonal Care','Accessories'],
}
SINGLE_SUPPLIER = {
    'Home Diagnostics': ('SUP003','Supplier 003'),
    'Mobility Aids': ('SUP011','Supplier 011'),
    'Travel Health': ('SUP019','Supplier 019'),
}

def money2(x):
    return float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def main():
    random.seed(SEED)
    suppliers=[(f'SUP{i:03d}',f'Supplier {i:03d}') for i in range(1,31)]
    manufacturers=[(f'MFG{i:03d}',f'Manufacturer {i:03d}') for i in range(1,21)]
    legal=['General Sale','Pharmacy Only','Restricted Sale']
    cats=list(CATEGORIES)
    rows=[]
    for i in range(1,N+1):
        sku=f'SKU{i:05d}'
        cat=random.choices(cats,weights=[25,22,18,18,17],k=1)[0]
        sub=random.choice(CATEGORIES[cat])
        scode,sname=SINGLE_SUPPLIER[sub] if sub in SINGLE_SUPPLIER else random.choice(suppliers)
        mcode,mname=random.choice(manufacturers)
        status='Active' if random.random()<0.82 else 'Blocked'
        band=random.choices(['Low','Medium','High','Premium'],weights=[30,40,24,6],k=1)[0]
        if band=='Low': rsp=round(random.uniform(4,24.75),2)
        elif band=='Medium': rsp=round(random.uniform(25,99.75),2)
        elif band=='High': rsp=round(random.uniform(100,299.75),2)
        else: rsp=round(random.uniform(300,650),2)
        base={'OTC & Wellness':0.33,'Personal Care':0.39,'Medical Devices':0.28,'Nutrition':0.31,'General Merchandise':0.35}[cat]
        tgm=round(max(0.08,min(0.62,random.gauss(base,0.07))),3)
        if status=='Blocked':
            sales_qty=0 if random.random()<0.75 else random.randint(1,35)
            soh=0 if random.random()<0.8 else random.randint(1,18)
        else:
            if random.random()<0.13:
                sales_qty=0; soh=random.randint(0,65)
            else:
                sales_qty=min(max(1,int(random.lognormvariate(3.2,0.8))),350)
                soh=max(0,int(random.gauss(max(6,sales_qty*0.35),12)))
        purchase_qty=max(0,sales_qty+soh+random.randint(-10,50))
        sales_value=money2(Decimal(str(rsp))*sales_qty)
        profit_value=money2(Decimal(str(sales_value))*Decimal(str(tgm)))
        inventory_value=money2(Decimal(str(rsp))*soh)
        zero='Active Zero Sales' if status=='Active' and sales_qty==0 else 'Not Zero Sales'
        risk=inventory_value if zero=='Active Zero Sales' else 0.0
        price='Low < 25' if rsp<25 else 'Medium 25-99' if rsp<100 else 'High 100-299' if rsp<300 else 'Premium 300+'
        rows.append({
            'SKU':sku,'Item_Name':f'Sample Product {i:05d}','Status':status,
            'Creation_Month':f'2026-{random.randint(1,6):02d}','RSP':rsp,'TGM_Pct':tgm,
            'Category':cat,'Sub_Category':sub,'Manufacturer_Code':mcode,'Manufacturer_Name':mname,
            'Supplier_Code':scode,'Supplier_Name':sname,'Regulatory_Code':f'REG-{random.randint(100000,999999)}',
            'Scientific_Name':f'Generic Ingredient {random.randint(1,180):03d}',
            'Legal_Status':random.choices(legal,weights=[75,22,3],k=1)[0],
            'Purchase_Qty':purchase_qty,'Sales_Qty':sales_qty,'SOH':soh,'Sales_Value':sales_value,
            'Profit_Value':profit_value,'Inventory_Value':inventory_value,'Zero_Sales_Flag':zero,
            'Inventory_Risk_Value':risk,'Price_Range':price,'Is_Active':1 if status=='Active' else 0
        })
    with OUT.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f'Generated {len(rows)} synthetic rows at {OUT}')

if __name__=='__main__': main()
