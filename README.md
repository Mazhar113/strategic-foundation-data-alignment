# Strategic Foundation — Project Package
Generated: 2025-11-23T07:59:26.977688 UTC

## Contents
- `streamlit_app.py` — Streamlit dashboard (dark theme)
- `data/` — CSV sample datasets (250,000 rows per file)
- `sql_kpis.sql` — SQL scripts & views for KPIs
- `notebook.ipynb` — Jupyter notebook for EDA and KPI calculations
- `README.md` — this file

## How to run locally (recommended)
1. Create Python venv and install dependencies:
```
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

2. Run Streamlit app:
```
streamlit run streamlit_app.py
```

Data is large (250k rows per file). The app reads from `/data` directory.

## Notes
- For production, load CSVs into a data warehouse and update the app to query the DB.
- Materialized views and scheduled refresh are recommended for heavy loads.

