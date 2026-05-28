import streamlit as st
import pandas as pd
import numpy as np
import os 

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Credit Risk Project | Brillian Gultom",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS KHUSUS UNTUK MEMUSATKAN GAMBAR SECARA STABIL (ANTI-GETAR)
st.markdown("""
    <style>
    [data-testid="stImage"] {
        margin: 0 auto;
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MEMBUAT SIDEBAR NAVIGASI
page = st.sidebar.radio(
    "Select a Phase:",
    [
        "1. Project Overview & Dataset",
        "2. Data Extraction (PostgreSQL)",
        "3. EDA & Risk Modeling (Python)",
        "4. Business Insights & Power BI"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Portofolio Owner:** Brillian Jordi Faster Gultom")
st.sidebar.markdown("**Role:** Risk Data Analyst")
st.sidebar.markdown("**Tech Stack:** PostgreSQL, Python (NumPy/Pandas), Power BI, Streamlit")

# 4. LOGIKA HALAMAN 1 (OVERVIEW)
if page == "1. Project Overview & Dataset":
    st.title("Credit Risk Analytics Portfolio")
    
    st.markdown("### Executive Summary")
    st.info("""
    This project simulates a real-world scenario 
    in a Fintech lending company. The primary objective is to analyze historical borrower data, 
    identify high-risk segments, and build a credit scoring mechanism to reduce the Non-Performing Loan (NPL) rate.
    """)
    
    st.markdown("### Analytical Tasks & Objectives")
    st.markdown("""
    In this project, I act as a Risk Data Analyst tasked with mitigating financial risks from bad loans. The core instructions and pipeline include:
    1. **Data Extraction (SQL):** Query the relational database to identify which specific borrower segments (by Loan Grade and Intent) contribute the most to the default volume.
    2. **Risk Modeling (Python/NumPy):** Develop a baseline Rule-Based Credit Scoring model using high-performance matrix operations to automatically filter and reject high-risk applications based on metrics like Loan-to-Income (LTI) ratio, interest rates, and annual income.
    3. **Business Strategy (Power BI):** Translate raw data into an interactive dashboard and formulate actionable risk mitigation recommendations for the Credit Management team.
    """)
    
    st.markdown("### Dataset Preview")
    st.write("The raw data consists of realistic records containing applicant demographics, loan intents, and historical default statuses (0 = Good, 1 = Default).")
    
    try:
        df = pd.read_csv("projects/credit_risk/credit_risk_dataset.csv")
        st.dataframe(df.head(15), use_container_width=True)
        st.success(f"Successfully loaded raw dataset containing {df.shape[0]} rows and {df.shape[1]} columns.")
    except Exception as e:
        st.error("Dataset missing atau gagal dimuat.")
        st.code(f"Error Log: {e}")

# 5. LOGIKA HALAMAN 2 (SQL EXTRACTION)
elif page == "2. Data Extraction (PostgreSQL)":
    st.title("Database Setup & SQL Extraction")
    st.markdown("""
    In enterprise environments, data environments require analysts to query directly from relational databases. 
    Below is the documentation of the PostgreSQL schema creation and the ad-hoc analysis query used to investigate NPL spikes.
    """)
    
    st.markdown("#### 📁 1. Table Creation Schema (DDL)")
    st.code("""
CREATE TABLE credit_risk_data (
    person_age INT,
    person_income NUMERIC,
    person_home_ownership VARCHAR(50),
    person_emp_length FLOAT,
    loan_intent VARCHAR(50),
    loan_grade VARCHAR(5),
    loan_amnt NUMERIC,
    loan_int_rate FLOAT,
    loan_status INT,
    loan_percent_income FLOAT,
    cb_person_default_on_file VARCHAR(5),
    cb_person_cred_hist_length INT
);
    """, language="sql")
        
    st.markdown("#### 📁 2. Ad-Hoc Business Query (Investigating NPL in Grade D)")
    
    st.info("""
    **Business Context & Storytelling:**
    During the initial reporting phase, management noticed an alarming spike in defaults originating specifically from the **Grade D** risk tier. The pressing business question was: *"What are these high-risk borrowers primarily using the funds for?"*
    
    To investigate this anomaly, I performed an ad-hoc SQL extraction. The query isolates all defaulting borrowers (`loan_status = 1`) within the Grade D segment, groups them by their stated loan intent, and calculates both the volume of defaults and the average loan exposure.
    """)
    
    st.code("""
SELECT 
    loan_intent, 
    COUNT(*) AS jumlah_nasabah_macet, 
    ROUND(AVG(loan_amnt), 2) AS rata_rata_pinjaman
FROM 
    credit_risk_data
WHERE 
    loan_status = 1 
    AND loan_grade = 'D'
GROUP BY 
    loan_intent
ORDER BY 
    jumlah_nasabah_macet DESC;
    """, language="sql")
        
    st.markdown("**Resulting Output:**")
    st.write("The output clearly highlights that 'MEDICAL' loans are the primary driver of defaults in this high-risk segment, revealing a critical blindspot in the current underwriting process.")
    
    sql_output = pd.DataFrame({
        "loan_intent": ["MEDICAL", "EDUCATION", "PERSONAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"],
        "jumlah_nasabah_macet": [577, 432, 389, 210, 150, 148],
        "rata_rata_pinjaman": [10849.39, 9540.20, 8900.50, 12050.00, 11200.75, 13500.00]
    })
    st.dataframe(sql_output, hide_index=True)

# 6. LOGIKA HALAMAN 3 (PYTHON)
elif page == "3. EDA & Risk Modeling (Python)":
    st.title("Exploratory Data Analysis & Modeling")
    st.markdown("""
    In this phase, we leverage **NumPy** for high-performance array calculations. 
    Instead of iterating through rows using slow loops, we use matrix operations to instantly calculate the Non-Performing Loan (NPL) rate 
    and build a baseline rule-based credit scoring model.
    """)
    
    st.markdown("#### Python & NumPy Code")
    st.code("""
# Calculate NPL Rate
loan_status = data_array[:, 4]
total_borrowers = len(loan_status)
default_borrowers = np.sum(loan_status == 1)
npl_rate = (default_borrowers / total_borrowers) * 100

# Rule-Based Credit Scoring
risk_scores = np.full(total_borrowers, 100)
loan_to_income = data_array[:, 2] / data_array[:, 1]
risk_scores = np.where(loan_to_income > 0.30, risk_scores - 30, risk_scores)
risk_scores = np.where(data_array[:, 3] > 13.0, risk_scores - 20, risk_scores)
risk_scores = np.where(data_array[:, 1] < 30000, risk_scores - 10, risk_scores)

approve_reject = np.where(risk_scores < 70, "REJECT", "APPROVE")
    """, language="python")
        
    st.markdown("### Model Evaluation Results")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Current NPL Rate", value="21.94%", delta="High Risk", delta_color="inverse")
    col2.metric(label="Model Approval Rate", value="93.53%", delta="Baseline Model", delta_color="off")
    col3.metric(label="Rejected Applications", value="1,906", delta="Avoided Defaults", delta_color="normal")

# 7. LOGIKA HALAMAN 4 (POWER BI)
elif page == "4. Business Insights & Power BI":
    st.title("Dashboard & Actionable Insights")
    st.markdown("""
    In this final phase, data is visualized dynamically using Power BI.
    The findings are translated into strategic recommendations for the management team.
    """)
    
    st.markdown("### Power BI Dashboard Snapshot")
    
    img_path = "projects/credit_risk/Dashboard.png" 
    
    if os.path.exists(img_path):
        # FIX FINAL: Tanpa kolom, dengan ukuran lebar tetap (width=850), tanpa caption. 
        # Otomatis ditarik ke tengah oleh instruksi CSS di atas!
        st.image(img_path, width=850)
    else:
        st.error("🚨 ALERT: File gambar dashboard tidak ditemukan oleh server Hugging Face!")
        st.warning(f"Server secara spesifik mencari file di jalur mutlak ini:\n`{os.path.abspath(img_path)}`")
        st.info("""
        **PANDUAN TROUBLESHOOTING:**
        1. Buka kembali tab 'Files' di Hugging Face.
        2. Periksa apakah ekstensi filemu huruf besar atau kecil. Jika filemu bernama `dashboard.PNG` atau `dashboard.jpg`, kamu harus mengedit baris kode `img_path = ...` di atas agar sama persis.
        """)
    
    st.markdown("### Key Business Insights")
    st.warning("""
    **1. Overall Risk Level:** The current Non-Performing Loan (NPL) rate stands at **21.94%**. Defaulting borrowers typically take larger loan amounts (avg. $10,854) and face higher interest rates (13.06%).
    
    **2. High-Risk Segment Identified:** Ad-hoc SQL analysis revealed that the most severe defaults originate from **Grade D** borrowers.
    
    **3. The 'Medical' Blindspot:** Within Grade D, loans intended for **Medical** purposes have the highest default volume (577 cases) with dangerously high average loan amounts ($10,849). This indicates that high-risk borrowers are utilizing loans for medical emergencies without the capacity to repay.
    """)
    
    st.markdown("### Actionable Recommendations")
    st.success("""
    To mitigate future NPL, the Data Team recommends the following strategic actions to the Credit & Risk Management:
    
    * **Tighten Medical Segment Criteria:** Require additional supporting documents (e.g., existing health insurance or a co-signer) for 'MEDICAL' loan applications, specifically for applicants falling into the Grade D tier.
    * **Limit Maximum Exposure (Plafon):** Decrease the maximum allowable loan amount for Grade D medical loans to below the current default average. Recommended new limit: **$8,000**.
    * **Calibrate the Scoring Model:** Incorporate 'Loan Intent' as a penalty parameter in our automated Credit Scoring algorithm, deducting extra points if the intent is medical without a strong credit history.
    """)
    
    st.markdown("---")
    st.markdown("🎉 *End of Portfolio Project. Thank you for exploring!*")