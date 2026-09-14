import streamlit as st

st.set_page_config(page_title="Technical Fusion", layout="wide")
st.title("⚙️ Technical Algorithms & Fusion Matrix")
st.markdown("### Bridging Human Psychology with ICT Anomalies")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("The Technical Module (40%)")
    st.markdown("""
    The FBIH connects via API to the bank's Enterprise Resource Planning (ERP) system (e.g., Sage, Oracle). It continuously scans transaction logs for **Means** and **Opportunity** indicators without interrupting daily operations.
    
    **Core ICT Metrics Measured:**
    *   **Unusual Transfers:** Massive reversals, bypassing verification workflows, or interacting with flagged vendor accounts. (Weighted heavier due to direct asset risk).
    *   **Access Anomalies:** System logins occurring between 11:00 PM and 4:00 AM, or unauthorized access attempts to restricted customer data.
    """)

with col2:
    st.subheader("Mathematical Fusion")
    st.markdown("The final risk category is calculated using a weighted predictive algorithm that fuses both data streams.")
    
    st.markdown("**The FBIH Algorithm:**")
    st.latex(r"Risk_{FBIH} = (W_{b} \times Score_{UBII}) + (W_{t} \times Score_{ICT})")
    
    st.markdown("**Where:**")
    st.markdown("""
    *   $W_{b}$ = Behavioral Weight (0.60)
    *   $W_{t}$ = Technical Weight (0.40)
    """)

st.divider()

st.subheader("Risk Thresholds & Human-in-the-Loop")
st.markdown("""
The system does not automatically terminate employees. It categorizes risk to trigger specific, human-led interventions:
""")

st.error("**CRITICAL (80-100):** Immediate system access restriction and manual forensic audit.")
st.warning("**HIGH (60-79):** Increased digital monitoring and supportive HR wellness interview.")
st.info("**MEDIUM (40-59):** Standard internal control review by branch supervisor.")
st.success("**LOW (0-39):** Normal operations and routine quarterly psychometric reassessments.")
