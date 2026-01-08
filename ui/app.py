import streamlit as st
import pandas as pd
from pipeline.assign_dca import assign_dca

st.set_page_config(
    page_title="FedEx DCA Prioritization System",
    layout="wide"
)

st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #F4F6F9;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #0B5ED7;
    margin-bottom: 5px;
}

/* Subtitle */
.sub-text {
    font-size: 17px;
    color: #555;
    margin-bottom: 25px;
}

/* Highlight text */
.highlight {
    color: #16A34A;
    font-weight: 600;
}

/* Section container with border */
.section-box {
    border: 1px solid #CBD5E1;
    border-radius: 10px;
    padding: 15px;
    background-color: #FFFFFF;
    margin-bottom: 25px;
}

/* Expander header styling */
details > summary {
    font-size: 22px;
    font-weight: 600;
    color: #1F2937;
    cursor: pointer;
    list-style: none;
}

details > summary::-webkit-details-marker {
    display: none;
}

/* KPI cards */
.card {
    background: linear-gradient(135deg, #ffffff, #f1f5f9);
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.card h2 {
    margin-top: 10px;
    color: #0B5ED7;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #2563EB, #0B5ED7);
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px 26px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1E40AF, #1D4ED8);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>FedEx DCA Prioritization System</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-text'>Adaptive DCA Intelligence Engine for performance-aware debt recovery</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<span class='highlight'>Decision intelligence that dynamically assigns the most suitable DCA based on priority, performance, and workload.</span>",
    unsafe_allow_html=True
)

st.markdown("<div class='section-box'>", unsafe_allow_html=True)
with st.expander("Upload Overdue Invoice Data", expanded=True):
    uploaded_file = st.file_uploader(
        "Select a CSV file containing overdue invoices",
        type="csv"
    )
    process = st.button("Run DCA Allocation")
st.markdown("</div>", unsafe_allow_html=True)
if uploaded_file and process:
    df = pd.read_csv(uploaded_file)

    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    with st.expander("Input Data Preview", expanded=True):
        st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    priorities = []
    dcas = []

    for _, row in df.iterrows():
        priority, dca = assign_dca(
            row["amount"],
            row["overdue_days"]
        )
        priorities.append(priority)
        dcas.append(dca)

    df["Priority"] = priorities
    df["Assigned DCA"] = dcas

    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    with st.expander("AI Allocation Output", expanded=True):
        st.dataframe(
            df[["amount", "overdue_days", "Priority", "Assigned DCA"]],
            use_container_width=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    with st.expander("Key Insights", expanded=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"<div class='card'><b>Total Invoices</b><h2>{len(df)}</h2></div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div class='card'><b>Total Overdue Amount</b><h2>₹ {df['amount'].sum()}</h2></div>",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"<div class='card'><b>High Priority Cases</b><h2>{len(df[df['Priority']=='High'])}</h2></div>",
                unsafe_allow_html=True
            )
    st.markdown("</div>", unsafe_allow_html=True)
