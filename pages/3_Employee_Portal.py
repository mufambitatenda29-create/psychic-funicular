import streamlit as st
import time

st.set_page_config(page_title="Employee Assessment", layout="centered")

st.title("🏛️ Employee Psychometric Portal")
st.markdown("### Ubuntu Behavioral Integrity Index (UBII) Assessment")
st.info("Welcome. Please complete the following routine assessment. Your responses are encrypted and securely transmitted directly to the Human Resources Compliance Hub.")
st.divider()

with st.form("employee_assessment_form"):
    st.markdown("#### Part 1: Workplace Perspectives")
    st.markdown("*Please indicate your level of agreement with the following statements.*")
    
    q1 = st.slider(
        "1. My duty to protect customer data outweighs my duty to help a relative in a financial dispute.",
        min_value=1, max_value=5, value=3
    )
    
    q2 = st.slider(
        "2. The bank makes millions in profit; bypassing a minor rule to help my community is justified.",
        min_value=1, max_value=5, value=3
    )
    
    st.divider()
    
    st.markdown("#### Part 2: Situational Judgment")
    st.markdown("*Select the most likely behavioral response to the following scenario.*")
    
    st.caption("**Scenario:** Your branch manager, a respected community elder, orders you to approve a loan for their friend who does not meet the credit requirements.")
    q3 = st.radio(
        "How do you respond?",
        options=[
            "Approve the loan; the manager bears the ultimate responsibility.",
            "Respectfully decline to process it, citing credit policy.",
            "Approve the loan but document that you were forced.",
            "Call in sick tomorrow to avoid having to process it."
        ],
        index=None
    )
    
    st.divider()

    # The submit button
    submitted = st.form_submit_button("Submit Confidential Assessment", type="primary")

if submitted:
    if q3 is None:
        st.error("⚠️ Please complete all sections before submitting.")
    else:
        # Show a loading spinner to simulate data transmission
        with st.spinner("Encrypting and transmitting responses to HR Hub..."):
            time.sleep(2.5) # Pauses for 2.5 seconds
            
        # The Blind Success Message (No Scores Shown!)
        st.success("✅ **Assessment Submitted Successfully.**")
        st.markdown("Thank you for completing your routine UBII evaluation. Your responses have been securely logged. You may now close this window and return to your duties.")
