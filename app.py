import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Fanuel Kemei | Product Builder",
    page_icon="🌍",
    layout="wide",
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* 1. FORCE TOP SPACING REMOVAL */
    .block-container {
        padding-top: 1rem !important;
        margin-top: 0rem !important;
    }

    /* 2. TYPOGRAPHY & COLORS */
    
    /* H1: LIGHTER BLUE (DodgerBlue) - SWAPPED */
    h1 {
        color: #1E90FF !important; 
        font-weight: 800; 
        font-size: 3rem;
    }
    
    /* H2-H6: DEEP BLUE (Streamlit Blue) - SWAPPED */
    h2, h3, h4, h5, h6 {
        color: #0068c9 !important; 
        font-weight: 700;
    }
    
    /* Specific sizing/borders for main levels */
    h2 {
        border-bottom: 2px solid #e5e7eb; 
        padding-bottom: 10px;
    }
    
    /* 3. LEADERSHIP CARDS - FIXED TEXT COLOR */
    /* We must override the blue above to force Black text inside the colored cards 
       so they remain visible against the green/yellow/blue backgrounds */
    
    /* Climate Card (Green) */
    .climate-box {
        background-color: #dcfce7;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #16a34a;
        height: 100%;
        color: #000000 !important;
    }
    
    /* Innovation Card (Yellow) */
    .innovator-box {
        background-color: #fef3c7;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #d97706;
        height: 100%;
        color: #000000 !important;
    }
    
    /* Community Card (Blue) */
    .community-box {
        background-color: #dbeafe;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
        height: 100%;
        color: #000000 !important;
    }
    
    /* Force headings inside cards to be BLACK (override global blue) */
    .climate-box h3, .innovator-box h3, .community-box h3 {
        color: #000000 !important;
    }
    
    .role-text {
        font-size: 1.3rem;
        font-weight: bold;
        color: #808495; /* Grey that works in both modes */
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    try:
        st.image("images/fanu.jpg", use_container_width=True)
    except:
        st.warning("⚠️ Photo not found. Please check 'images/fanu.jpg'")

    st.title("Fanuel Kemei")
    st.write("📍 Nairobi, Kenya")
    st.write("📧 fanueljunior08@gmail.com")
    st.write("📞 +254 705 730236")
    
    st.markdown("---")
    st.write("**Connect:**")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/fanuel--951a69276/)")
    st.markdown("[GitHub Profile](https://github.com/fanuel08)")
    
    st.markdown("---")
    
    # CV DOWNLOAD
    try:
        with open("CV_Fanuel_Kemei.pdf", "rb") as pdf_file:
            pdfbytes = pdf_file.read()
        st.download_button(
            label="📄 Download Full CV",
            data=pdfbytes,
            file_name="CV_Fanuel_Kemei.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.warning("⚠️ Please place 'CV_Fanuel_Kemei.pdf' in the folder.")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Hello, I'm Fanuel Kemei")
    st.markdown('<p class="role-text">Data Scientist | Backend Developer | Climate Advocate 🌿</p>', unsafe_allow_html=True)
    
    st.write("""
    **I build intelligent, end-to-end systems.**
    
    I am a Product Builder who bridges the gap between **Data Science**, **Software Engineering**, and **Strategy**. I don't just analyze data; I build the Django APIs that serve it and the automated pipelines that clean it.
    """)
    
    st.success("**🌱 Proud Ambassador: Climate Restoration Alliance   -   # Championing restoration & preservation tech.**")

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacer
    with st.container():
        st.info("🎓 **B.Sc. Computer Science**")
        
        # Using HTML h5 tag so it turns Blue
        st.markdown("<h5>📜 Certifications notable:</h5>", unsafe_allow_html=True)
        st.markdown("""
        * **HCIA - AI** (Huawei)
        * **Data Science and AI** (Udemy)            
        * **Software Dev** (Power Learn Project)
        * **Cybersecurity** (ICT Authority)
        """)

st.markdown("---")

# --- SKILLS SECTION ---
st.header("🛠 Tech Stack & Expertise")

sk1, sk2, sk3 = st.columns(3)

with sk1:
    st.markdown("### 📊 Data Science")
    st.write("I turn raw numbers into predictive insights.")
    st.progress(80)
    st.caption("Python (Pandas, NumPy, Matplotlib, Seaborn)")
    st.progress(85)
    st.caption("Scikit-learn & ML Models")
    st.progress(40)
    st.caption("Data Visualization")

with sk2:
    st.markdown("### ⚙️ Backend Engineering")
    st.write("I architect secure, scalable systems.")
    st.progress(60)
    st.caption("Django & REST APIs")
    st.progress(60)
    st.caption("SQL (MySQL / PostgreSQL)")
    st.progress(75)
    st.caption("System Architecture")

with sk3:
    st.markdown("### 🚀 Tools & DevOps")
    st.write("I automate workflows to save time.")
    st.progress(73)
    st.caption("Git & GitHub")
    st.progress(75)
    st.caption("Bash Scripting & Automation")
    st.progress(70)
    st.caption("Docker")

st.markdown("---")

# --- PROJECT SHOWCASE ---
st.header("💻 Featured Projects")

st.caption("Explore the different 'Hats' I wear on projects: Data, Engineering, and Management.")

# Project 1: Telemedicine
with st.expander("🏥 Telemedicine Platform for Rural Access (AI-Driven)", expanded=True):
    tab1, tab2, tab3 = st.tabs(["🧠 The Data (AI)", "⚙️ The Engineering", "📋 The Management"])
    
    with tab1:
        st.markdown("#### Focus: Machine Learning & Diagnostics")
        st.write("""
        * **Model:** Engineered a symptom-classification model using Scikit-learn.
        * **Data:** Preprocessed **2,000+ patient records**, handling imputation for missing medical history.
        * **Result:** Achieved **85% accuracy** in preliminary triage categorization.
        """)
    
    with tab2:
        st.markdown("#### Focus: Backend Architecture")
        st.write("""
        * **API:** Built a RESTful API with **Django** to serve model predictions in real-time.
        * **Performance:** Optimized database queries to achieve **sub-200ms** response times.
        * **Security:** Implemented Role-Based Access Control (RBAC) to protect patient privacy.
        """)
        
    with tab3:
        st.markdown("#### Focus: Product Strategy")
        st.write("""
        * **Strategy:** Defined the product roadmap based on rural healthcare accessibility gaps.
        * **Agile:** Managed the development lifecycle to prioritize critical triage features.
        """)

# Project 2: E-Commerce
with st.expander("📚 E-Commerce Bookstore Database (Scalable Architecture)"):
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### 📊 Data & Insights")
        st.write("""
        * **Reporting:** Generated actionable inventory datasets from raw transaction logs.
        * **Analytics:** Enabled real-time sales reporting to track bestseller trends.
        """)
    
    with col_b:
        st.markdown("#### ⚙️ Database Architecture")
        st.write("""
        * **Schema:** Designed a normalized MySQL schema for **1,000+ SKUs**.
        * **Optimization:** Refactored SQL queries, reducing report generation time by **30%**.
        """)

# Project 3: Automation
with st.expander("⚙️ Process Automation Initiative"):
    st.markdown("#### Focus: DevOps & Efficiency")
    st.write("""
    * **Problem:** Identified a bottleneck in manual data cleaning that consumed ~5 hours/week.
    * **Solution:** Wrote Python & Bash scripts to process batches of **500+ files** automatically.
    * **Result:** **40% reduction** in manual workload, allowing the team to focus on analysis.
    """)

st.markdown("---")

# --- LEADERSHIP & IMPACT ---
st.header("🏆 Leadership & Impact")

# 3 COLUMNS: Climate | Innovation | Community
lead1, lead2, lead3 = st.columns(3)

with lead1:
    # THE CLIMATE 
    st.markdown("""
    <div class="climate-box">
        <h3>🌿 Global Ambassador</h3>
        <p><b>Climate Restoration Alliance</b></p>
        <p><i>"Restoring the climate for future generations."</i></p>
        <p>Working alongside global leaders like <b>Ilan Mandel</b> to accelerate the mission of restoring atmospheric CO2 to safe pre-industrial levels (<300ppm).</p>
        <p><b>My Role:</b> Advocating for scalable restoration technologies and data-driven climate solutions.</p>
    </div>
    """, unsafe_allow_html=True)

with lead2:
    # THE INNOVATOR 
    st.markdown("""
    <div class="innovator-box">
        <h3>💡 Recognized Innovator</h3>
        <p><b>Access 2.0 Qualifier</b></p>
        <p><i>"Tech for Social Good"</i></p>
        <p>Recognized for technical excellence and creative problem-solving.</p>
        <p><b>My Role:</b> Qualified in the competitive <b>Access 2.0</b> program, demonstrating the ability to build practical, impactful technology solutions under rigorous standards.</p>
    </div>
    """, unsafe_allow_html=True)

with lead3:
    # THE COMMUNITY 
    st.markdown("""
    <div class="community-box">
        <h3>🎓 Campus Ambassador</h3>
        <p><b>Phoenix KE Analytics</b></p>
        <p><i>"Building the Data Workforce"</i></p>
        <p>Bridging the gap between academia and industry for Kenyan students.</p>
        <p><b>My Role:</b> Organized training sessions for <b>30+ peers</b>, creating a pathway for students to access professional data science networks and mentorship.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 Fanuel Kemei. Built with Python & Streamlit.")