import streamlit as st
import pandas as pd, numpy as np, json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Enzyme Production Intelligence", layout="wide")
BASE=Path(__file__).parent
DATA=BASE/"data"

@st.cache_data
def load_data():
    u=pd.read_csv(DATA/"unified_batch_scored.csv")
    ts=pd.read_csv(DATA/"manufacturing_timeseries.csv")
    docs=pd.read_csv(DATA/"sharepoint_documents.csv")
    fi=pd.read_csv(DATA/"yield_feature_importance.csv")
    with open(DATA/"model_metrics.json") as f:
        metrics=json.load(f)
    return u,ts,docs,fi,metrics

u,ts,docs,fi,metrics=load_data()

st.title("Enzyme Production Intelligence Platform")
st.caption("Synthetic IFF-style demo integrating SAP, LIMS, manufacturing process data, and SharePoint technical knowledge.")

tabs=st.tabs(["Executive Overview","Batch Explorer","Predictive Analytics","Quality & Root Cause","Knowledge Assistant"])

with tabs[0]:
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Batches",len(u))
    c2.metric("Average Yield",f"{u.yield_pct.mean():.1f}%")
    c3.metric("Released",f"{(u.qc_status=='Released').mean()*100:.1f}%")
    c4.metric("High Risk",int((u.predicted_quality_risk>=.60).sum()))
    st.subheader("Average Yield by Site")
    st.bar_chart(u.groupby("site")["yield_pct"].mean())
    st.subheader("Quality Status")
    st.bar_chart(u["qc_status"].value_counts())

with tabs[1]:
    batch=st.selectbox("Select batch",u.batch_id.tolist())
    r=u[u.batch_id==batch].iloc[0]
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Yield",f"{r.yield_pct:.1f}%")
    c2.metric("Activity",f"{r.enzyme_activity_U_mL:.0f} U/mL")
    c3.metric("Purity",f"{r.purity_pct:.1f}%")
    c4.metric("Predicted Quality Risk",f"{r.predicted_quality_risk*100:.0f}%")
    sub=ts[ts.batch_id==batch]
    st.subheader("Fermentation Trend")
    st.line_chart(sub.set_index("hour")[["pH","temperature_C","dissolved_oxygen_pct","feed_rate_L_hr"]])
    st.subheader("Unified Batch Record")
    st.dataframe(r.to_frame("value"),use_container_width=True)

with tabs[2]:
    st.subheader("Use Case 1: Enzyme Yield Prediction")
    c1,c2=st.columns(2)
    c1.metric("MAE",f"{metrics['yield_model']['MAE']:.2f} yield points")
    c2.metric("R²",f"{metrics['yield_model']['R2']:.2f}")
    st.bar_chart(fi.set_index("feature")["importance"])
    st.dataframe(fi,use_container_width=True,hide_index=True)

    st.subheader("Use Case 2: Quality-Risk Prediction")
    cols=st.columns(4)
    for col,(k,v) in zip(cols,metrics["quality_risk_model"].items()):
        col.metric(k,f"{v:.2f}")

with tabs[3]:
    st.subheader("Use Case 3: Anomaly Detection")
    high=u[(u.predicted_quality_risk>=.60)|(u.anomaly_flag==1)].copy()
    st.dataframe(high[["batch_id","site","supplier","yield_pct","enzyme_activity_U_mL","purity_pct",
                       "predicted_quality_risk","anomaly_flag","qc_status"]].sort_values("predicted_quality_risk",ascending=False),
                 use_container_width=True,hide_index=True)

    st.subheader("Use Case 4: Root-Cause Support")
    choices=high.batch_id.tolist() if len(high) else u.batch_id.tolist()
    batch2=st.selectbox("Choose a high-risk batch",choices,key="rootcause")
    r=u[u.batch_id==batch2].iloc[0]
    baseline=u[u.qc_status=="Released"]
    metrics_list=["temperature_C_avg","pH_avg","dissolved_oxygen_pct_avg","feed_rate_L_hr_avg",
                  "fermentation_time_hr","yield_pct"]
    comp=pd.DataFrame({
        "metric":metrics_list,
        "selected_batch":[r[x] for x in metrics_list],
        "released_batch_median":[baseline[x].median() for x in metrics_list]
    })
    comp["difference"]=comp["selected_batch"]-comp["released_batch_median"]
    st.dataframe(comp,use_container_width=True,hide_index=True)

with tabs[4]:
    st.subheader("Use Case 5: RAG-Ready Knowledge Assistant")
    st.info("Prototype retrieval uses TF-IDF on synthetic SharePoint documents. Production design would use embeddings, vector DB, governed LLM, citations, access controls, and human review.")
    q=st.text_input("Question","What evidence links low dissolved oxygen to reduced enzyme yield?")
    if q:
        vec=TfidfVectorizer(stop_words="english")
        M=vec.fit_transform(docs["content"].fillna("").tolist()+[q])
        sims=cosine_similarity(M[-1],M[:-1]).flatten()
        top=np.argsort(sims)[::-1][:5]
        out=docs.iloc[top].copy()
        out["relevance"]=np.round(sims[top],3)
        st.dataframe(out[["document_id","document_type","title","approval_status","relevance","content"]],
                     use_container_width=True,hide_index=True)

st.sidebar.header("Unified Architecture")
st.sidebar.markdown("""
**Sources**
- SAP: batches, materials, suppliers
- LIMS: samples, assays, HPLC, QC
- Manufacturing: fermentation + time series
- SharePoint: SOPs, deviations, reports

**Common key:** `batch_id`

**Analytics**
1. Yield prediction
2. Quality-risk prediction
3. Anomaly detection
4. Root-cause support
5. RAG-ready retrieval
""")
