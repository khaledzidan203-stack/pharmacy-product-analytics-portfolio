# Cross-Tool Validation

Use `outputs/validation_summary.csv` as the checklist. For each metric:
1. calculate from the public CSV/Python baseline;
2. calculate from `vw_kpi_summary` in SQL Server;
3. calculate with the DAX measures in Power BI;
4. confirm the HTML dashboard card;
5. mark `Match? = Yes` only when the same definition and rounding are used.

Recommended comparison columns: `Metric | CSV/Python | SQL Server | Power BI | HTML | Match?`.

Do not force a match by manually editing values; resolve calculation/filter-context differences instead.
