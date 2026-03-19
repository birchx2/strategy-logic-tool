import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Strategic Logic Stress Test", page_icon="⚖️", layout="centered")

# --- HEADER ---
st.title("25+ Year Strategic Logic Engine")
st.subheader("Identify your 'Overhead Trap' and find the 'Third Question'.")
st.markdown("---")

# --- STEP 1: INITIAL DISCOVERY ---
st.header("Step 1: The Foundation")
col1, col2 = st.columns(2)

with col1:
    is_marketable = st.radio("Is your product/service currently marketable?", ("Yes", "No"))
with col2:
    has_plan = st.radio("Do you have a documented execution plan?", ("Yes", "No"))

# --- STEP 2: THE INTUITION VS. LOGIC TEST ---
st.header("Step 2: The Scalability Stress Test")
st.info("The 'Overhead Trap' occurs when growth requires a 1:1 increase in headcount.")

gut_feeling = st.checkbox("My 'Gut' says we just need more people to scale.")
data_proof = st.checkbox("I have data proof that my current team is 100% efficient.")

# --- STEP 3: SECTOR ANALYSIS ---
st.header("Step 3: Sector Specifics")
sector = st.selectbox("Select your primary sector:", 
                      ["Automotive", "Manufacturing / Logistics", "Global B2B", "Other"])

# --- THE RESULTS ENGINE ---
if st.button("RUN DIAGNOSIS"):
    st.markdown("---")
    
    # Logic Logic
    if is_marketable == "Yes" and has_plan == "Yes":
        if gut_feeling and not data_proof:
            st.error("⚠️ DIAGNOSIS: THE OVERHEAD TRAP")
            st.write("Your intuition is leaning toward hiring, but your lack of data efficiency proof suggests you are scaling a bottleneck. Scaling now will decrease your margin.")
        elif gut_feeling and data_proof:
            st.success("✅ DIAGNOSIS: READY FOR ACCELERATION")
            st.write("Your logic and data are aligned. You are ready to scale your headcount.")
        else:
            st.warning("🧐 DIAGNOSIS: ARCHITECTURE REVIEW REQUIRED")
            st.write("Foundation is solid, but the scalability logic is still undefined.")
    else:
        st.error("🚫 STOP: FOUNDATIONAL PILLAR MISSING")
        st.write("Do not attempt to scale. Your business lacks either market fit or a documented plan.")

    # The Third Question (The Payoff)
    st.subheader("The 'Third Question' You Should Be Asking:")
    if sector == "Automotive":
        st.info("Q3: Is your floorplan interest alignment matching your 30-day turn logic?")
    elif sector == "Manufacturing / Logistics":
        st.info("Q3: Where is the manual data latency in your 'last-mile' reporting?")
    elif sector == "Global B2B":
        st.info("Q3: How does your cross-border regulatory friction affect your margin per unit?")
    else:
        st.info("Q3: What is the one metric you are tracking that you don't actually trust?")

st.markdown("---")
st.caption("Based on 25+ Years of Proven Business Logic and Operational Architecture.")
