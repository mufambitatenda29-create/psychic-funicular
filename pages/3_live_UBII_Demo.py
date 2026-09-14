import streamlit as st
import time

st.set_page_config(page_title="UBII Assessment Demo", layout="wide")

# Use a clean, modern UI for the form
st.title("📝 UBII Psychometric Assessment Portal")
st.markdown("### Secure Employee Evaluation Environment")
st.caption("This is a live demonstration of how banking personnel interact with the Ubuntu Behavioral Integrity Index.")
st.divider()

# Create a form so the page doesn't refresh until the user clicks submit
with st.form("ubii_assessment_form"):
    st.markdown("#### Part 1: Likert Scale Evaluation")
    st.markdown("*Please indicate your level of agreement with the following statements.*")
    
    # Q1: Organizational Loyalty (Positively Worded)
    q1 = st.slider(
        "1. My duty to protect customer data outweighs my duty to help a relative in a financial dispute.",
        min_value=1, max_value=5, value=3, 
        help="1 = Strongly Disagree | 5 = Strongly Agree"
    )
    
    # Q2: Moral Disengagement (Reverse-Scored concept)
    q2 = st.slider(
        "2. The bank makes millions in profit; bypassing a minor rule to help my community is justified.",
        min_value=1, max_value=5, value=3,
        help="1 = Strongly Disagree | 5 = Strongly Agree"
    )
    
    st.divider()
    
    st.markdown("#### Part 2: Situational Judgment Test (SJT)")
    st.markdown("*Select the most likely behavioral response to the following scenario.*")
    
    # Q3: Ethical Courage SJT
    st.info("**Scenario:** Your branch manager, a respected community elder, orders you to approve a loan for their friend who does not meet the credit requirements.")
    q3 = st.radio(
        "How do you respond?",
        options=[
            "Approve the loan; the manager bears the ultimate responsibility.",
            "Respectfully decline to process it, citing credit policy, and document the interaction.",
            "Approve the loan but write a secret note in the file that you were forced.",
            "Call in sick tomorrow to avoid having to process it."
        ],
        index=None # Forces the user to make a choice
    )
    
    st.divider()
    
    st.markdown("#### Part 3: HR Integration (Simulated Data Pull)")
    st.markdown("*In production, this data is pulled automatically via API. Select an option to simulate HR flags.*")
    hr_status = st.selectbox("Current HR Flag Status", ["None", "Written Warning", "High Debt / Wage Garnishment"])

    # The submit button
    submitted = st.form_submit_button("Submit Assessment & Calculate Risk Baseline", type="primary")

# ---------------------------------------------------------
# SCORING LOGIC (Triggers only after clicking submit)
# ---------------------------------------------------------
if submitted:
    if q3 is None:
        st.error("⚠️ Please complete the Situational Judgment Test before submitting.")
    else:
        with st.spinner("Encrypting responses and running psychometric evaluation..."):
            time.sleep(2) # Simulates processing time for dramatic effect during a demo
            
            # Very basic scoring logic for the demo
            # Q1: Higher is better (Max 5 points)
            # Q2: Lower is better (Reverse scored: 6 - answer) (Max 5 points)
            q2_score = 6 - q2 
            
            # Q3 SJT Scoring (Max 10 points)
            sjt_score = 0
            if "Respectfully decline" in q3:
                sjt_score = 10 # Best answer
            elif "secret note" in q3 or "Call in sick" in q3:
                sjt_score = 4 # Avoidance/passive
            else:
                sjt_score = 1 # Compliance with unethical order
                
            # Base Behavioral Score out of 100
            total_raw = q1 + q2_score + sjt_score # Max 20 raw points
            base_score = (total_raw / 20) * 100
            
            # Apply HR Penalties
            penalty = 0
            if hr_status == "High Debt / Wage Garnishment":
                penalty = 15
            elif hr_status == "Written Warning":
                penalty = 10
                
            final_behavioral_score = min(100, (100 - base_score) + penalty) # Invert so higher = worse risk
            
            st.success("✅ Assessment successfully processed and logged to the FBIH central hub.")
            
            st.markdown("### 📊 Generated Behavioral Risk Baseline")
            
            # Display results in columns
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                # We use metric delta to show the penalty impact
                if penalty > 0:
                    st.metric(label="Behavioral Risk Score", value=f"{final_behavioral_score:.1f} / 100", delta=f"+{penalty} HR Penalty Points", delta_color="inverse")
                else:
                    st.metric(label="Behavioral Risk Score", value=f"{final_behavioral_score:.1f} / 100", delta="Clean HR Record", delta_color="normal")
            
            with res_col2:
                if final_behavioral_score >= 60:
                    st.error("**Status:** Elevated Behavioral Risk. System awaiting technical ICT validation to generate final Integrated Score.")
                else:
                    st.success("**Status:** Normal Baseline. System monitoring ICT logs routinely.")
