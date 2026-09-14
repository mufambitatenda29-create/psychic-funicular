import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. DATA GENERATION & SCORING ENGINE
@st.cache_data
def load_and_score_data():
    np.random.seed(42) 
    num_employees = 250
    
    employee_ids = [f"EMP_{str(i).zfill(4)}" for i in range(1, num_employees + 1)]
    roles = np.random.choice(["Bank Teller", "Loan Officer", "IT Admin", "Branch Manager"], num_employees, p=[0.5, 0.3, 0.1, 0.1])
    is_threat = np.random.choice([0, 1], num_employees, p=[0.95, 0.05]) 
    
    after_hours_logins = np.where(is_threat == 1, np.random.randint(5, 20, num_employees), np.random.randint(0, 3, num_employees))
    unusual_file_transfers = np.where(is_threat == 1, np.random.randint(2, 10, num_employees), np.random.randint(0, 2, num_employees))
    
    org_loyalty = np.where(is_threat == 1, np.random.normal(40, 10, num_employees), np.random.normal(85, 10, num_employees))
    corruption_res = np.where(is_threat == 1, np.random.normal(35, 15, num_employees), np.random.normal(90, 8, num_employees))
    communal_acc = np.where(is_threat == 1, np.random.normal(50, 12, num_employees), np.random.normal(80, 10, num_employees))
    ethical_courage = np.where(is_threat == 1, np.random.normal(45, 10, num_employees), np.random.normal(75, 12, num_employees))
    moral_disengage = np.where(is_threat == 1, np.random.normal(80, 10, num_employees), np.random.normal(20, 10, num_employees)) 
    
    hr_flags = np.where(is_threat == 1, np.random.choice(["High Debt", "Written Warning", "None"], num_employees, p=[0.4, 0.4, 0.2]), 
                                        np.random.choice(["High Debt", "Written Warning", "None"], num_employees, p=[0.1, 0.05, 0.85]))
    
    df = pd.DataFrame({
        "Employee_ID": employee_ids, "Role": roles, "After_Hours_Logins": after_hours_logins,
        "Unusual_Transfers": unusual_file_transfers, "UBII_Org_Loyalty": np.clip(org_loyalty, 0, 100).astype(int),
        "UBII_Corruption_Res": np.clip(corruption_res, 0, 100).astype(int), "UBII_Communal_Acc": np.clip(communal_acc, 0, 100).astype(int),
        "UBII_Ethical_Courage": np.clip(ethical_courage, 0, 100).astype(int), "UBII_Moral_Disengage": np.clip(moral_disengage, 0, 100).astype(int),
        "HR_Stressor_Flag": hr_flags, "Actual_Threat": is_threat
    })

    def calculate_scores(row):
        b_base = (((100 - row['UBII_Org_Loyalty']) * 0.15) + ((100 - row['UBII_Corruption_Res']) * 0.20) + 
                  ((100 - row['UBII_Communal_Acc']) * 0.10) + ((100 - row['UBII_Ethical_Courage']) * 0.15) + 
                  (row['UBII_Moral_Disengage'] * 0.25))
        if row['HR_Stressor_Flag'] == 'High Debt': b_base += 15
        elif row['HR_Stressor_Flag'] == 'Written Warning': b_base += 10
        b_score = min(b_base, 100)
        
        t_score = 0
        if row['After_Hours_Logins'] > 3: t_score += min((row['After_Hours_Logins'] * 5), 40)
        if row['Unusual_Transfers'] > 1: t_score += min((row['Unusual_Transfers'] * 15), 60)
        t_score = min(t_score, 100)
        
        integrated = (b_score * 0.60) + (t_score * 0.40)
        return pd.Series([round(b_score, 1), round(t_score, 1), round(integrated, 1)])

    df[['Behavioral_Score', 'Technical_Score', 'Integrated_Score']] = df.apply(calculate_scores, axis=1)
    
    def cat_risk(score):
        if score >= 80: return "CRITICAL"
        elif score >= 60: return "HIGH"
        elif score >= 40: return "MEDIUM"
        else: return "LOW"
        
    df['Risk_Category'] = df['Integrated_Score'].apply(cat_risk)
    return df

df = load_and_score_data()

# 2. DASHBOARD USER INTERFACE
st.set_page_config(page_title="FBIH Prototype", layout="wide")
st.title("🏦 Forensic Behavioral Intelligence Hub (FBIH)")
st.markdown("### Predictive Insider Fraud Detection via Bi-Modular Scoring")
st.divider()

st.sidebar.header("🔍 Entity Selection")
selected_emp = st.sidebar.selectbox("Select Employee ID to Audit:", df['Employee_ID'].tolist())
emp_data = df[df['Employee_ID'] == selected_emp].iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Employee ID", emp_data['Employee_ID'])
col2.metric("Role", emp_data['Role'])
col3.metric("HR Stressor", emp_data['HR_Stressor_Flag'])
col4.metric("Risk Category", emp_data['Risk_Category'])

st.divider()

st.markdown("### 📊 Bi-Modular Risk Assessment")
g_col1, g_col2, g_col3 = st.columns(3)

def create_gauge(value, title, color):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 60], 'color': "lightyellow"},
                {'range': [60, 80], 'color': "orange"},
                {'range': [80, 100], 'color': "red"}],
        }))
    fig.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
    return fig

with g_col1:
    st.plotly_chart(create_gauge(emp_data['Behavioral_Score'], "Behavioral Score (60%)", "darkblue"), use_container_width=True)
with g_col2:
    st.plotly_chart(create_gauge(emp_data['Technical_Score'], "Technical Score (40%)", "darkblue"), use_container_width=True)
with g_col3:
    st.plotly_chart(create_gauge(emp_data['Integrated_Score'], "INTEGRATED SCORE", "black"), use_container_width=True)

st.divider()
st.markdown("### 🧠 Algorithmic Transparency & Action Protocol")
e_col1, e_col2 = st.columns([2, 1])

with e_col1:
    st.markdown("**Risk Contributors (Why was this score generated?)**")
    fig = go.Figure(go.Waterfall(
        orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = ["Base Risk", "Behavioral Factors", "Technical Anomalies", "Final Score"],
        y = [0, emp_data['Behavioral_Score'] * 0.6, emp_data['Technical_Score'] * 0.4, emp_data['Integrated_Score']],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

with e_col2:
    st.markdown("**Human-in-the-Loop Directives**")
    if emp_data['Risk_Category'] == "CRITICAL":
        st.error("🚨 **CRITICAL ALERT**\n\nImmediate system access restriction. Escalate to Chief Risk Officer.")
    elif emp_data['Risk_Category'] == "HIGH":
        st.warning("⚠️ **HIGH RISK**\n\nIncrease digital monitoring frequency. Schedule supportive HR interview.")
    elif emp_data['Risk_Category'] == "MEDIUM":
        st.info("🟡 **MEDIUM RISK**\n\nStandard internal control review.")
    else:
        st.success("🟢 **LOW RISK**\n\nNormal operations.")

    st.markdown("**Raw Data Audit Trail**")
    st.caption(f"Unusual Transfers: {emp_data['Unusual_Transfers']} | After-Hours Logins: {emp_data['After_Hours_Logins']}")
    st.caption(f"UBII Moral Disengagement: {emp_data['UBII_Moral_Disengage']}/100")