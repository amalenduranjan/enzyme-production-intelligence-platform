# Enzyme Production Intelligence Platform
## Business problem
In industrial enzyme production, important information is often distributed across different systems:

LIMS: enzyme assay results, sample information, HPLC results, purity, activity

SAP: raw materials, batch numbers, inventory, suppliers, production orders, quality status

SharePoint: SOPs, specifications, deviation reports, investigations, technical reports

Laboratory instruments: HPLC, UV-Vis, plate readers, spectroscopy

Manufacturing systems: fermentation temperature, pH, agitation, dissolved oxygen, feed rate, airflow, fermentation time

Because the information is fragmented, scientists and quality teams may spend considerable time manually combining data before they can answer questions such as: 
1) Why did Batch A have 20% lower enzyme yield?
2) Which fermentation variables are most strongly associated with enzyme activity and purity?

The goal of the project would be to create one trusted analytical layer connecting all these sources and answer these questions.

## Synthetic data-based platform for these use cases.

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

## Architecture
SAP + LIMS + Manufacturing + SharePoint
→ ingestion
→ standardization and validation
→ common batch model
→ curated unified data
→ analytics / ML / GenAI

## Architecture Diagram for GitHub and streamlit
Synthetic SAP / LIMS / Manufacturing Data
                ↓
        Jupyter Notebook
         Data Exploration
                ↓
        Data Harmonization
                ↓
         Feature Engineering
                ↓
           ML Modeling
                ↓
        Model Evaluation
                ↓
       Save Model / Results
                ↓
             app.py
                ↓
           Streamlit UI
                ↓
      GitHub + Cloud Deployment

## Dashboard screenshot
<img width="1263" height="542" alt="Screenshot Enzyme production intelligence" src="https://github.com/user-attachments/assets/86c527b6-9ce8-403e-bddf-0fb009147114" />

## Production extensions
**Replace CSVs with governed system connectors:** 
the production system would connect directly to real systems such as LIMS, SAP, SharePoint, manufacturing historians, or instrument databases using approved APIs, database connectors, or integration tools.
**add master-data management:** 
**unit harmonization:** 
**data lineage:** 
**RBAC:** 
**audit logs:** 
**validation**: 
**model monitoring:** 
**embeddings/vector DB:** 
**Vector database**:
**Citations**:
**Human approval / Human-in-the-loop**:
