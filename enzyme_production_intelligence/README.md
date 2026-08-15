# Enzyme Production Intelligence Platform
## Business problem
In industrial enzyme production, important information is often distributed across different systems:

LIMS: enzyme assay results, sample information, HPLC results, purity, activity

SAP: raw materials, batch numbers, inventory, suppliers, production orders, quality status

SharePoint: SOPs, specifications, deviation reports, investigations, technical reports

Laboratory instruments: HPLC, UV-Vis, plate readers, spectroscopy

Manufacturing systems: fermentation temperature, pH, agitation, dissolved oxygen, feed rate, airflow, fermentation time

Because the information is fragmented, scientists and quality teams may spend considerable time manually combining data before they can answer questions such as: 
1) Why did Batch 145 have 20% lower enzyme yield?
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
**Replace CSVs with governed system connectors:** 
the production system would connect directly to real systems such as LIMS, SAP, SharePoint, manufacturing historians, or instrument databases using approved APIs, database connectors, or integration tools.
**add master-data management:** MDM creates a consistent definition for important business entities across systems.
Example: the same enzyme product may have different names or IDs in SAP, LIMS, and SharePoint. MDM creates one trusted mapping:
ENZ-001 = SAP material 4500123 = LIMS product ENZYME_A.
This prevents duplicate or mismatched records.
**unit harmonization:** Different systems may store the same measurement using different units. Before analysis, they must be converted to a common standard.
Example: one lab reports enzyme concentration as mg/mL, another as g/L. These need to be standardized before combining the datasets.
The same applies to temperature, pressure, activity units, flow rates, and concentrations.
**data lineage:** Data lineage tells you exactly where a value came from and what transformations were applied to it.
Example: if the dashboard shows enzyme activity = 850 U/mL, lineage should allow you to trace it back to the LIMS record, original instrument result, batch ID, transformation step, and load timestamp.
This is especially important for quality and regulated environments.
**RBAC:** RBAC controls who can see or change what.
Example: a scientist may view laboratory results, a quality manager may approve investigations, and an administrator may manage system configuration.
Not every user should have access to every dataset or AI function.
**audit logs:** Audit logs record important system activity.
Example: who changed a batch status, who accessed a deviation report, when a model prediction was generated, or who approved an AI-generated summary.
This helps with traceability, compliance, and investigations.
**validation**: Validation means proving that the data pipeline, model, or application works as intended.
For data, this could include checking missing values, duplicates, ranges, units, and relationships.
Example: every LIMS sample must link to a valid SAP batch.
For an AI system, validation would include checking whether outputs are accurate, reproducible, and appropriate for the intended use.
**model monitoring:** A machine-learning model cannot simply be deployed and forgotten. Its performance must be monitored over time.
Example: your enzyme-quality model may originally have ROC-AUC 0.90, but after a process change or new raw-material supplier, its performance may fall.
Monitoring tracks prediction quality, data drift, model drift, error rates, and changes in input distributions.
**embeddings/vector DB:** Embeddings convert text into numerical vectors that represent meaning.
Example: an SOP discussing “low dissolved oxygen during fermentation” can be converted into an embedding so the system can find it even if the user asks, “What happens when oxygen falls during enzyme production?”
The wording is different, but the meaning is similar.
**Vector database**:A vector database stores embeddings and allows fast semantic search.
Examples include FAISS, Pinecone, Chroma, Azure AI Search, or similar systems.
In your project, SharePoint SOPs, deviation reports, and technical documents could be embedded and stored in a vector database so the AI system can retrieve the most relevant documents.
**Enterprise LLM**:An enterprise LLM is a large language model deployed in a controlled organizational environment with security, access controls, governance, and approved data handling.
Instead of sending sensitive company data to an uncontrolled public chatbot, the organization might use an approved Azure OpenAI, OpenAI Enterprise, or another internally governed model.
In your project, the LLM would summarize retrieved SOPs, deviations, and batch information.
**Citations**:Citations show the user where the AI got its information.
Example:
Low dissolved oxygen was observed in three historical deviations. Source: Deviation Report DEV-104, SOP-FERM-002.
This is critical for scientific and quality workflows because users need to verify the AI output rather than blindly trust it.
**Human approval / Human-in-the-loop**:AI should support decisions, not automatically make critical quality decisions without oversight.
Example: the AI may identify that Batch B145 has an 82% quality-risk score and draft a root-cause summary, but a quality scientist reviews and approves the final conclusion.
This is especially important in regulated or high-impact scientific environments.
