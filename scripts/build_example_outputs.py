#!/usr/bin/env python3
"""Rebuild all checked-in example outputs from the synthetic CSV."""
from pathlib import Path
from collections import defaultdict
import csv

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'sample_pharmacy_products.csv'
OUT=ROOT/'outputs'

def load():
    with DATA.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    for r in rows:
        for c in ['RSP','TGM_Pct','Sales_Value','Profit_Value','Inventory_Value','Inventory_Risk_Value']:
            r[c]=float(r[c])
        for c in ['Purchase_Qty','Sales_Qty','SOH','Is_Active']:
            r[c]=int(float(r[c]))
    return rows

def write(name,rows,fields=None):
    if fields is None: fields=list(rows[0]) if rows else []
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

def main():
    rows=load(); active=[r for r in rows if r['Status']=='Active']; blocked=[r for r in rows if r['Status']=='Blocked']; zero=[r for r in active if r['Sales_Qty']==0]
    sf=lambda rs,k: round(sum(r[k] for r in rs),2)
    metrics={'Total SKUs':len(rows),'Active SKUs':len(active),'Blocked SKUs':len(blocked),
             'Active %':round(len(active)/len(rows)*100,2),'Blocked %':round(len(blocked)/len(rows)*100,2),
             'Total Sales Quantity':sum(r['Sales_Qty'] for r in rows),'Total Sales Value':sf(rows,'Sales_Value'),
             'Total Profit Value':sf(rows,'Profit_Value'),'Average TGM% (Active)':round(sum(r['TGM_Pct'] for r in active)/len(active)*100,2),
             'Zero Sales Active SKUs':len(zero),'Inventory Financial Risk':sf(zero,'Inventory_Risk_Value')}
    write('kpi_summary.csv',[{'Metric':k,'Value':v} for k,v in metrics.items()])
    def group(key):
        g=defaultdict(list)
        for r in rows:g[r[key]].append(r)
        out=[]
        for name,rs in sorted(g.items()):
            a=[r for r in rs if r['Status']=='Active']; z=[r for r in rs if r['Sales_Qty']==0 and r['Status']=='Active']
            out.append({key:name,'Total_SKUs':len(rs),'Active_SKUs':len(a),'Blocked_SKUs':len(rs)-len(a),'Sales_Qty':sum(r['Sales_Qty'] for r in rs),
                        'Sales_Value':sf(rs,'Sales_Value'),'Profit_Value':sf(rs,'Profit_Value'),'Avg_Active_TGM_Pct':round(sum(r['TGM_Pct'] for r in a)/len(a)*100,2) if a else 0,
                        'Zero_Sales_Active_SKUs':len(z),'Inventory_Risk_Value':sf(z,'Inventory_Risk_Value')})
        return out
    write('category_analysis.csv',group('Category')); write('supplier_analysis.csv',group('Supplier_Name'))
    deps=[]; sg=defaultdict(list)
    for r in active: sg[r['Sub_Category']].append(r)
    for sub,rs in sorted(sg.items()):
        suppliers=sorted({r['Supplier_Name'] for r in rs})
        if len(suppliers)==1: deps.append({'Sub_Category':sub,'Active_SKUs':len(rs),'Supplier_Count':1,'Supplier_Name':suppliers[0],'Sales_Qty':sum(r['Sales_Qty'] for r in rs)})
    write('single_supplier_dependency.csv',deps)
    write('zero_sales_risk.csv',[{k:r[k] for k in ['SKU','Item_Name','Category','Sub_Category','Supplier_Name','RSP','SOH','Inventory_Value','Inventory_Risk_Value','Price_Range']} for r in zero])
    cats=['OTC & Wellness','Personal Care','Medical Devices','Nutrition','General Merchandise']; ts=[]; tp=[]
    for c in cats:
        cr=[r for r in rows if r['Category']==c]
        for rank,r in enumerate(sorted(cr,key=lambda x:(x['Sales_Qty'],x['Sales_Value']),reverse=True)[:20],1):
            ts.append({'Category':c,'Rank':rank,'SKU':r['SKU'],'Item_Name':r['Item_Name'],'Sales_Qty':r['Sales_Qty'],'Sales_Value':r['Sales_Value'],'Profit_Value':r['Profit_Value']})
        for rank,r in enumerate(sorted(cr,key=lambda x:(x['Profit_Value'],x['Sales_Value']),reverse=True)[:20],1):
            tp.append({'Category':c,'Rank':rank,'SKU':r['SKU'],'Item_Name':r['Item_Name'],'Profit_Value':r['Profit_Value'],'Sales_Qty':r['Sales_Qty'],'Sales_Value':r['Sales_Value']})
    write('top20_by_sales_qty.csv',ts); write('top20_by_profit.csv',tp)
    write('validation_summary.csv',[{'Metric':k,'CSV_Python':v,'SQL_Expected':'Recalculate after import','Power_BI_Expected':'Recalculate after model load','HTML_Expected':'Calculated in browser','Match':'Pending cross-tool run'} for k,v in metrics.items()])
    print('Rebuilt all example outputs.')

if __name__=='__main__': main()
