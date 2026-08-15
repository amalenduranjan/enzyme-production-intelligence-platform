# Enzyme Production Intelligence Platform

Synthetic data-based platform for an use case.

## Scenario
Industrial *Aspergillus niger* enzyme fermentation. A common `batch_id` harmonizes:
- SAP batch/material/supplier records
- LIMS sample, HPLC, activity, purity, and QC results
- Manufacturing fermentation summaries and time-series data
- SharePoint-style SOPs, deviation investigations, and technical reports

## Use cases
1. Enzyme yield prediction
2. Quality-risk prediction
3. Fermentation anomaly detection
4. Root-cause investigation support
5. RAG-ready scientific/quality knowledge retrieval

## Synthetic model results
Yield model: MAE 2.93, R² 0.35
Quality-risk model: ROC-AUC 0.94, Precision 0.86, Recall 0.83, F1 0.84

## Run the dashboard
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Architecture
SAP + LIMS + Manufacturing + SharePoint
→ ingestion
→ standardization and validation
→ common batch model
→ curated unified data
→ analytics / ML / GenAI

## Production extensions
Replace CSVs with governed system connectors; add master-data management, unit harmonization, data lineage, RBAC, audit logs, validation, model monitoring, embeddings/vector DB, enterprise LLM, citations, and human approval.
