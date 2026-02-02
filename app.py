import streamlit as st
import time
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sai Kumar | Secure Workstation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD CSS ----------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "booted" not in st.session_state:
    st.session_state.booted = False

if "module" not in st.session_state:
    st.session_state.module = "OVERVIEW"

# ---------------- BOOT SCREEN (FIRST LOAD) ----------------
if not st.session_state.booted:
    st.markdown("<div class='boot'>INITIALIZING SECURE WORKSTATION</div>", unsafe_allow_html=True)
    progress = st.progress(0)

    logs = [
        "Mounting file system",
        "Loading security modules",
        "Initializing AI subsystems",
        "Applying access policies",
        "System ready"
    ]

    for i, log in enumerate(logs):
        st.markdown(f"<div class='boot-text'>{log}</div>", unsafe_allow_html=True)
        progress.progress((i + 1) * 20)
        time.sleep(0.35)

    st.session_state.booted = True
    st.rerun()

# ---------------- TOP SYSTEM BAR ----------------
current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(f"""
<div class="topbar">
root@sai-secure-node &nbsp; | &nbsp; STATUS: SECURE &nbsp; | &nbsp;
CPU: ▓▓▓░ &nbsp; | &nbsp; {current_time}
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([1, 4])

# ---------------- LEFT MODULE PANEL ----------------
with left:
    st.markdown("<div class='sidebar'>SYSTEM MODULES</div>", unsafe_allow_html=True)

    if st.button("SYSTEM OVERVIEW"):
        st.session_state.module = "OVERVIEW"
    if st.button("SYSTEM DATA"):
        st.session_state.module = "DATA"
    if st.button("SKILL CORE"):
        st.session_state.module = "SKILLS"
    if st.button("PROJECTS"):
        st.session_state.module = "PROJECTS"
    if st.button("ACTIVITY LOGS"):
        st.session_state.module = "LOGS"
    if st.button("FILE SYSTEM"):
        st.session_state.module = "FILES"

# ---------------- WORKSPACE (SLIDE-IN PANELS) ----------------
with right:
    st.markdown("<div class='workspace slide'>", unsafe_allow_html=True)

    # -------- SYSTEM OVERVIEW --------
    if st.session_state.module == "OVERVIEW":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM OVERVIEW</b><br><br>
        NODE ID : SAI-KUMAR-01<br>
        ROLE : SOFTWARE ENGINEER<br>
        DOMAINS : CYBERSECURITY | AI | PYTHON<br>
        EDUCATION : B.Tech (CGPA 8.67)<br>
        STATUS : AVAILABLE
        </div>
        """, unsafe_allow_html=True)

    # -------- SYSTEM DATA --------
    elif st.session_state.module == "DATA":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM DATA</b><br><br>
        • Oracle Cloud – Developer Professional<br>
        • Oracle Cloud – Networking Professional<br>
        • Google Cyber Security<br>
        • Salesforce AI Associate<br><br>
        LANGUAGES SUPPORTED:<br>
        • English<br>
        • Telugu<br>
        • Hindi
        </div>
        """, unsafe_allow_html=True)

    # -------- SKILL CORE --------
    elif st.session_state.module == "SKILLS":
        st.markdown("<div class='panel'><b>SKILL CORE</b></div>", unsafe_allow_html=True)
        skills = {
            "Python Engine": 90,
            "Network Security": 80,
            "Linux Systems": 75,
            "Streamlit UI Core": 75,
            "Database Systems": 70
        }
        for skill, level in skills.items():
            st.markdown(f"<div class='skill'>{skill}</div>", unsafe_allow_html=True)
            st.progress(level)

    # -------- PROJECTS --------
    elif st.session_state.module == "PROJECTS":
        st.markdown("""
        <div class="panel">
        <b>OPERATION: DATA LEAK DETECTION</b><br>
        TYPE : SECURITY TOOL<br>
        TOOLS : Python, Regex, Git<br><br>
        Detects sensitive data exposure and file system vulnerabilities.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="panel">
        <b>OPERATION: CIRCULAR DNA ANALYSIS</b><br>
        TYPE : BIOINFORMATICS SYSTEM<br>
        TOOLS : Python, Streamlit, Biopython<br><br>
        Predicts circular DNA structures and generates visual reports.
        </div>
        """, unsafe_allow_html=True)

    # -------- ACTIVITY LOGS --------
    elif st.session_state.module == "LOGS":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM ACTIVITY LOGS</b><br><br>
        [2024-08] Oracle Cloud Developer Certified<br>
        [2024-06] Google Cyber Security Completed<br>
        [2023-12] Security Tool Deployed<br>
        [2023-09] Streamlit Research App Released
        </div>
        """, unsafe_allow_html=True)

    # -------- FILE SYSTEM --------
    elif st.session_state.module == "FILES":
        st.markdown("""
        <div class="panel">
        <b>FILE SYSTEM</b><br><br>
        /root/<br>
        ├── resume.pdf<br>
        ├── certifications/<br>
        └── reports/
        </div>
        """, unsafe_allow_html=True)

        with open("resume.pdf.pdf", "rb") as f:
            st.download_button(
                "⬇ Download resume.pdf",
                f,
                file_name="Madhugani_Sai_Kumar_Resume.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

