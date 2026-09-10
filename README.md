# Retail Sales Data Cleaning (Superstore Dataset)

End-to-end data cleaning pipeline for a Superstore sales dataset — built in Python (Pandas, NumPy, Matplotlib) as part of a data analytics internship task.

## What This Project Does

- Cleans irregular column names (spaces, casing, punctuation)
- Fixes data types for dates and numeric fields
- Handles missing values (median imputation for numeric, "unknown" for categorical)
- Removes duplicate rows
- Detects and removes outliers using the IQR method
- Generates exploratory visualizations
- Exports a final, analysis-ready CSV

## Key Result

Started with a raw, inconsistent Superstore export and produced a clean dataset ready for dashboards, EDA, or ML — with reproducible, documented steps (see `summary_changes.md` for the full before/after log).

## Project Structure

```
Superstore-Task-1/
├── data/
│   ├── raw/            # original unprocessed data
│   └── processed/      # cleaned_superstore.csv (output)
├── src/
│   └── clean.py        # main cleaning script
├── visuals/
│   ├── sales_distribution.png
│   └── profit_by_category.png
├── requirements.txt
└── summary_changes.md  # detailed changelog of cleaning steps
```

## Tech Stack

Python 3 · Pandas · NumPy · Matplotlib

## How to Run

```bash
pip install -r requirements.txt
python src/clean.py
```

This generates:
- `data/processed/cleaned_superstore.csv` — the cleaned dataset
- `visuals/sales_distribution.png` — sales histogram
- `visuals/profit_by_category.png` — profit by category bar chart

## Visuals

**Sales Distribution** — shows sales values are heavily right-skewed, with most transactions under $200 and a long tail of high-value outliers.

**Profit by Category** — aggregates total profit per product category to spot which categories drive (or drag down) profitability.

## Notes

All cleaning logic was written manually in Python (no automated cleaning tools), so every transformation is traceable and explainable. See `summary_changes.md` for the step-by-step log of exactly what changed and why.
