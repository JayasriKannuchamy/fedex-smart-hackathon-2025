import streamlit as st
import pandas as pd
from pipeline.assign_dca import assign_dca

st.title("FedEx DCA Prioritization System")

uploaded_file = st.file_uploader("Upload Overdue Invoice CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    priorities = []
    dcas = []

    for _, row in df.iterrows():
        priority, dca = assign_dca(row["amount"], row["overdue_days"])
        priorities.append(priority)
        dcas.append(dca)

    df["Priority"] = priorities
    df["Assigned DCA"] = dcas

    st.dataframe(df)
