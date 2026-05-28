import streamlit as st
import base64

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Brillian Gultom | Portofolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. HERO SECTION (Perkenalan Diri)
col1, col2 = st.columns([2.5, 1])
with col1:
    st.markdown('<h1>Hi, I am Brillian Gultom 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h4>Entry-Level Data Analyst | Civil Engineering Graduate</h4>', unsafe_allow_html=True)
    
    st.write("""
    I am an engineering graduate with a strong foundation in **data processing, structuring, and quantitative analysis**. 
    I specialize in transforming raw, multivariate, and time-series datasets into actionable business insights. 
    Whether it's writing SQL queries, manipulating arrays with Python, or designing interactive Power BI dashboards, 
    I enjoy solving complex problems through data.
    """)
    
    st.write("📍 **Jakarta Selatan, Indonesia**")
    
with col2:
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    try:
        # Menampilkan foto profil
        img_base64 = get_base64_image("./Brillian Gultom.jpg")
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_base64}" 
                     style="border-radius: 20px; width: 100%; max-width: 220px; box-shadow: 2px 2px 10px rgba(0,0,0,0.15);">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("Foto Brillian Gultom.jpg tidak ditemukan di folder utama.")

st.divider()

# 3. TECH STACK & SKILLS
st.header("Core Competencies")

st.markdown("""
    <style>
    .skill-container {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .skill-card {
        flex: 1;
        min-width: 200px;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 5px solid;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
        background-color: #F8FAFC;
    }
    .card-blue { border-left-color: #1E3A8A; background-color: #F0F6FF; }
    .card-green { border-left-color: #15803D; background-color: #F0FDF4; }
    .card-amber { border-left-color: #B45309; background-color: #FFFBEB; }
    .card-red { border-left-color: #B91C1C; background-color: #FEF2F2; }
    
    .card-title { font-weight: bold; font-size: 1.1rem; margin-bottom: 0.8rem; color: #1E293B; }
    .card-body { font-size: 0.95rem; line-height: 1.5; color: #475569; }
    .card-body ul { margin: 0; padding-left: 1.2rem; }
    </style>
    
    <div class="skill-container">
        <div class="skill-card card-blue">
            <div class="card-title">👨‍💻 Programming</div>
            <div class="card-body">
                <ul>
                    <li>Python (NumPy, Pandas)</li>
                    <li>SQL (PostgreSQL)</li>
                </ul>
            </div>
        </div>
        <div class="skill-card card-green">
            <div class="card-title">📊 Visualization</div>
            <div class="card-body">
                <ul>
                    <li>Power BI</li>
                    <li>Streamlit</li>
                </ul>
            </div>
        </div>
        <div class="skill-card card-amber">
            <div class="card-body">
                <div class="card-title">⚙️ Processing</div>
                <ul>
                    <li>Data Cleaning</li>
                    <li>EDA & Modeling</li>
                </ul>
            </div>
        </div>
        <div class="skill-card card-red">
            <div class="card-title">🛠️ Tools</div>
            <div class="card-body">
                <ul>
                    <li>Git / GitHub</li>
                    <li>Docker</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. JOURNEY & BACKGROUND
st.header("Background")
tab1, tab2, tab3 = st.tabs(["Education", "Experience", "Training & Certifications"])

with tab1:
    st.subheader("Pancasila University")
    st.write("**Bachelor of Engineering (Civil Engineering) | Graduated: 2026**")
    st.markdown("""
    **Capstone Project: Data-Driven Traffic Analysis**
    - Structured a complex multivariate dataset across multiple dimensions (2 road directions, 3 time segments, 15-minute intervals).
    - Processed multiple variables including vehicle categories and side friction factors.
    - Conducted time-series aggregation and trend analysis to identify peak patterns and anomalies.
    - Generated actionable insights to support data-driven decision-making.
    """)

with tab2:
    st.subheader("PT. Biro Arsitek dan Insinjur Sangkuriang")
    st.write("**Construction Management Intern | Bogor, Indonesia (Aug 2023 - Oct 2023)**")
    st.markdown("""
    - Analyzed project data to support progress tracking and performance monitoring.
    - Monitored daily metrics to identify delays, inefficiencies, and anomalies on-site.
    - Structured and maintained project data for reporting and analytical purposes.
    """)

with tab3:
    st.write("#### Certifications & Credentials")
    st.write("Click to expand and verify the official certificate images.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- SERTIFIKAT 1 ---
    st.markdown("🏅 **Microsoft Excel Professional — Coursera (2026)**")
    with st.expander("📜 View Certificate"):
        try:
            st.image("projects/certificates/Coursera_Microsoft Excel.jpg", width=750)
        except Exception as e:
            st.error("💡 Gambar tidak dapat dimuat. Pastikan file berada di folder: projects/certificates/")
            
    st.markdown("---")
    
    # --- SERTIFIKAT 2 ---
    st.markdown("🏅 **Construction Management Specialization — Coursera (2026)**")
    with st.expander("📜 View Certificate"):
        try:
            st.image("projects/certificates/Coursera_Construction Management.jpg", width=750)
        except Exception as e:
            st.error("💡 Gambar tidak dapat dimuat. Pastikan file berada di folder: projects/certificates/")

st.divider()

# 5. CALL TO ACTION
st.header("📂 Explore My Portofolio")
st.write("""
👈 **Navigate through the sidebar** to see my end-to-end data projects in action. Currently featuring:
- **Project 1:** Credit Risk Analytics (Full-Stack Data Pipeline, NumPy Modeling, & Dashboard)
""")