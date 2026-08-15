# Business Problem and Approach

The business problem is that important information is fragmented across SAP, LIMS, manufacturing systems, and SharePoint. For this project I used **Synthetic Demonstration Data **and built a enzyme-production intelligence platform to demonstrate how I would approach.

I used a common batch ID to connect SAP material and supplier data, LIMS enzyme activity and HPLC results, fermentation variables such as pH, temperature, dissolved oxygen and feed rate, and SharePoint-style SOPs and deviation reports.

I then created a unified analytical layer and demonstrated five use cases: predicting enzyme yield, predicting quality risk, detecting unusual fermentation conditions, supporting root-cause investigations, and retrieving relevant technical knowledge.

The key design principle is to establish trusted, harmonized data before adding AI. In production, I would replace the synthetic CSVs with governed connectors, add master-data management, lineage and validation, and use an enterprise vector database and approved LLM for the knowledge assistant.

This project connects my biotechnology background in fermentation and enzyme production with data engineering, machine learning, GenAI, and quality operations.

Workflow for this project:
Step 1
Create synthetic datasets in Jupyter
        ↓
Step 2
Perform EDA
        ↓
Step 3
Harmonize SAP + LIMS + Manufacturing data
        ↓
Step 4
Train and evaluate ML models
        ↓
Step 5
Save cleaned/scored data and model
        ↓
Step 6
Build app.py
        ↓
Step 7
Run with Streamlit
        ↓
Step 8
Push to GitHub
        ↓
Step 9
Deploy on Streamlit Community Cloud
