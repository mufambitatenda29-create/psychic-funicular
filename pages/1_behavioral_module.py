import streamlit as st
import pandas as pd

st.set_page_config(page_title="Behavioral Module", layout="wide")
st.title("🧠 The Behavioral Module (UBII)")
st.markdown("### Ubuntu Behavioral Integrity Index & HR Integration")
st.divider()

st.markdown("""
This module generates **60%** of the Integrated Predictive Risk Score. It replaces traditional physical surveillance with scientifically validated psychometric testing and documented Human Resources (HR) stressors.
""")

st.subheader("1. Psychometric Assessment (The UBII)")
st.markdown("Employees undergo the **120-item UBII psychometric assessment**. The test is calibrated to Zimbabwean banking realities, measuring five core constructs:")

# Creating a clean table for the UI
trait_data = {
    "Dimension": ["Moral Disengagement", "Corruption Resistance", "Ethical Courage", "Organizational Loyalty", "Communal Accountability"],
    "Weight in Module": ["25%", "20%", "15%", "15%", "10%"],
    "Measurement Focus": [
        "Cognitive rationalization of unethical acts",
        "Susceptibility to bribery and kickbacks",
        "Willingness to blow the whistle on superiors",
        "Strict adherence to banking policy over communal pressure",
        "Shared responsibility for branch ethical health"
    ]
}
st.table(pd.DataFrame(trait_data))

st.subheader("2. HR Stressor Integration")
st.markdown("""
To capture dynamic behavioral shifts without invasive observation, the FBIH integrates directly with standard HR documentation. 
If an employee is flagged for a life stressor, penalty points are added to their behavioral baseline:
*   **High Debt / Wage Garnishment:** +15 Risk Points
*   **Official Disciplinary Warning:** +10 Risk Points
""")

st.info("💡 **Methodological Note:** No physical surveillance (e.g., cameras, keystroke loggers) is utilized to generate the behavioral score, ensuring strict adherence to workplace privacy ethics.")
