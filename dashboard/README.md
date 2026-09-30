# Menstrual Cycle Pattern Dashboard

This folder contains the supplementary Streamlit dashboard developed as part of the master's thesis:

**A Data-driven Analysis of Menstrual Cycle Patterns Using Cycle-Based Indicators**

The dashboard provides an interactive visual presentation of the finalized analytical results. It is intended as a supplementary visualization of the analysis rather than as an additional analytical or clinical tool.

## Dashboard Contents

The dashboard presents four main sections:

- **Overview** — provides a summary of the dataset, finalized analytical workflow, and key results.
- **Cycle Patterns** — presents the three identified menstrual-cycle patterns and their main characteristics.
- **Clustering Evaluation** — presents the clustering sensitivity analysis, silhouette score, and stability assessment.
- **Longitudinal Patterns** — presents transitions between cycle-pattern clusters across consecutive cycles.

## Files

- `app.py` — Streamlit application used to run the dashboard.
- `final_cluster_data.csv` — finalized cycle observations and cluster assignments used for visualization.
- `sensitivity_results.csv` — clustering sensitivity results across feature sets and numbers of clusters.
- `transition_percentages.csv` — finalized percentages of transitions between consecutive cycle-pattern clusters.

## Running the Dashboard

The dashboard can be run locally using Streamlit:

```bash
streamlit run app.py
