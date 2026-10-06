#!/usr/bin/env python3
"""Repository validation: schema, row-level formulas, IDs, and secret-pattern scan."""
from pathlib import Path
import csv, re, sys
from decimal import Decimal, ROUND_HALF_UP

ROOT=Path(__file__).resolve().parents[1]
CSV_PATH=ROOT/"data"/"sample_pharmacy_products.csv"
REQUIRED=["SKU","Item_Name","Status","Creation_Month","RSP","TGM_Pct","Category","Sub_Category","Manufacturer_Code","Manufacturer_Name","Supplier_Code","Supplier_Name","Regulatory_Code","Scientific_Name","Legal_Status","Purchase_Qty","Sales_Qty","SOH","Sales_Value","Profit_Value","Inventory_Value","Zero_Sales_Flag","Inventory_Risk_Value","Price_Range","Is_Active"]
TEXT_EXT={'.md','.txt','.sql','.py','.html','.js','.css','.json','.yml','.yaml','.csv','.gitignore'}
SECRET_PATTERNS=[
    re.compile(r'(?i)(api[_ -]?key|secret[_ -]?key|password|connection[_ -]?string)\s*[:=]\s*[^\s<]{8,}'),
    re.compile(r'(?i)server\s*=\s*[^;\n]+;.*database\s*='),
]

def fail(msg): print('ERROR:',msg); return 1

def main():
    errors=0
    with CSV_PATH.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if list(rows[0].keys())!=REQUIRED: errors+=fail('Unexpected CSV schema')
    if len(rows)!=1500: errors+=fail(f'Expected 1500 sample rows, got {len(rows)}')
    if len({r['SKU'] for r in rows})!=len(rows): errors+=fail('Duplicate SKU detected')
    for i,r in enumerate(rows,2):
        if r['Status'] not in {'Active','Blocked'}: errors+=fail(f'Invalid status row {i}'); break
        rsp=float(r['RSP']); qty=int(float(r['Sales_Qty'])); soh=int(float(r['SOH'])); tgm=float(r['TGM_Pct'])
        if abs(float(r['Sales_Value'])-round(rsp*qty,2))>0.011: errors+=fail(f'Sales formula row {i}'); break
        expected_profit=float((Decimal(str(r['Sales_Value']))*Decimal(str(r['TGM_Pct']))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        if abs(float(r['Profit_Value'])-expected_profit)>0.011: errors+=fail(f'Profit formula row {i}'); break
        if abs(float(r['Inventory_Value'])-round(rsp*soh,2))>0.011: errors+=fail(f'Inventory formula row {i}'); break
        expected='Active Zero Sales' if r['Status']=='Active' and qty==0 else 'Not Zero Sales'
        if r['Zero_Sales_Flag']!=expected: errors+=fail(f'Zero-sales flag row {i}'); break
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXT: continue
        txt=p.read_text(encoding='utf-8',errors='ignore')
        for pat in SECRET_PATTERNS:
            if pat.search(txt): errors+=fail(f'Potential secret-like pattern in {p.relative_to(ROOT)}')
    # Retained KPI baseline contract
    kpi_path=ROOT/'outputs'/'kpi_summary.csv'
    with kpi_path.open(encoding='utf-8',newline='') as f:
        kpis={r['Metric']:r['Value'] for r in csv.DictReader(f)}
    expected_kpis={
        'Total SKUs':'1500',
        'Active SKUs':'1225',
        'Blocked SKUs':'275',
        'Active %':'81.67',
        'Blocked %':'18.33',
        'Total Sales Quantity':'37488',
        'Total Sales Value':'3722472.1',
        'Total Profit Value':'1249396.7',
        'Average TGM% (Active)':'33.51',
        'Zero Sales Active SKUs':'129',
        'Inventory Financial Risk':'406473.61',
    }
    for k,v in expected_kpis.items():
        if kpis.get(k)!=v:
            errors+=fail(f'KPI baseline changed for {k}: {kpis.get(k)} != {v}')

    # Presentation / implementation boundary contract
    required=[
        ROOT/'README.md',
        ROOT/'PROJECT_NOTES.md',
        ROOT/'docs'/'PROJECT_INDEX.md',
        ROOT/'docs'/'CASE_STUDY.md',
        ROOT/'docs'/'TECHNICAL_WALKTHROUGH.md',
        ROOT/'docs'/'PROJECT_EVIDENCE_MAP.md',
        ROOT/'docs'/'FINAL_RELEASE_VALIDATION.md',
        ROOT/'docs'/'assets'/'Pharmacy Analytics Dashboard Overview.png',
        ROOT/'excel'/'Pharmacy_Assessment_Excel_Analysis.xlsx',
        ROOT/'sql'/'Pharmacy_Assessment_SQL_Outputs.xlsx',
    ]
    for p in required:
        if not p.exists():
            errors+=fail(f'Missing required project artifact: {p.relative_to(ROOT)}')

    index=(ROOT/'index.html').read_text(encoding='utf-8')
    for old in ['Portfolio demonstration','Developed by Khaled Zidan','Public portfolio demo']:
        if old in index:
            errors+=fail(f'Old presentation wording remains in index.html: {old}')

    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    if 'Pharmacy%20Analytics%20Dashboard%20Overview.png' not in readme:
        errors+=fail('README hero image link missing')
    if 'Power BI is therefore a **design blueprint**' not in readme:
        errors+=fail('Power BI implementation boundary missing from README')

    if errors: sys.exit(1)
    print('PASS | schema and row formulas')
    print('PASS | unique SKU and status rules')
    print('PASS | retained KPI baseline')
    print('PASS | presentation / evidence boundary')
    print('PASS | secret-pattern scan')
    print('REPOSITORY VALIDATION PASS')

if __name__=='__main__': main()
