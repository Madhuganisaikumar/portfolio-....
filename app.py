import streamlit as st
import time
import random
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sai Kumar | Secure Cyber Workstation",
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

if "active_project" not in st.session_state:
    st.session_state.active_project = None

# ---------------- BOOT SCREEN ----------------
if not st.session_state.booted:
    st.markdown("<div class='boot'>INITIALIZING PROTECTED SYSTEM</div>", unsafe_allow_html=True)
    progress = st.progress(0)

    for i, msg in enumerate([
        "Mounting secure filesystem",
        "Loading security modules",
        "Initializing AI subsystems",
        "Applying access rules",
        "System online"
    ]):
        st.markdown(f"<div class='boot-text'>{msg}</div>", unsafe_allow_html=True)
        progress.progress((i + 1) * 20)
        time.sleep(0.3)

    st.session_state.booted = True
    st.rerun()

# ---------------- BACKGROUND EFFECTS ----------------
st.markdown("<div class='scanline'></div>", unsafe_allow_html=True)

# ---------------- TOP BAR ----------------
current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(f"""
<div class="topbar">
<span class="status-dot"></span>
root@sai-secure-node | READ_ONLY | CPU ▓▓▓░ | {current_time}
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([1, 4])

# ---------------- SIDEBAR ----------------
with left:
    st.markdown("<div class='sidebar'>SYSTEM MODULES</div>", unsafe_allow_html=True)

    if st.button("SYSTEM OVERVIEW"): st.session_state.module = "OVERVIEW"
    if st.button("SKILL CORE"): st.session_state.module = "SKILLS"
    if st.button("PROJECTS"): st.session_state.module = "PROJECTS"
    if st.button("ACTIVITY LOGS"): st.session_state.module = "LOGS"
    if st.button("FILE SYSTEM"): st.session_state.module = "FILES"

# ---------------- WORKSPACE ----------------
with right:
    st.markdown("<div class='workspace slide'>", unsafe_allow_html=True)

    # -------- OVERVIEW --------
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

        # ---- SYSTEM METRICS ----
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='panel'><b>SYSTEM METRICS</b></div>", unsafe_allow_html=True)

        st.progress(random.randint(60, 85))  # CPU
        st.caption("CPU Load")

        st.progress(random.randint(50, 75))  # Memory
        st.caption("Memory Usage")

    # -------- SKILLS --------
    elif st.session_state.module == "SKILLS":
        st.markdown("<div class='panel'><b>SKILL CORE</b></div>", unsafe_allow_html=True)
        for s, v in {
            "Python Engine": 90,
            "Network Security": 80,
            "Linux Systems": 75,
            "Streamlit UI Core": 75
        }.items():
            st.markdown(f"<div class='skill'>{s}</div>", unsafe_allow_html=True)
            st.progress(v)

    # -------- PROJECTS --------
    elif st.session_state.module == "PROJECTS":
        st.markdown("<div class='panel'><b>OPERATIONS</b></div>", unsafe_allow_html=True)

        if st.button("Inspect: Data Leak Detection"):
            st.session_state.active_project = "DLD"

        if st.button("Inspect: Circular DNA Analysis"):
            st.session_state.active_project = "DNA"

        # ---- PROJECT DIALOG ----
        if st.session_state.active_project == "DLD":
            st.markdown("""
            <div class="dialog">
            <b>OPERATION: DATA LEAK DETECTION</b><br><br>
            TYPE : SECURITY TOOL<br>
            TOOLS : Python, Regex, Git<br><br>
            Detects sensitive data exposure in files and emails.
            Identifies filesystem vulnerabilities and prevents leaks.
            </div>
            """, unsafe_allow_html=True)

        if st.session_state.active_project == "DNA":
            st.markdown("""
            <div class="dialog">
            <b>OPERATION: CIRCULAR DNA ANALYSIS</b><br><br>
            TYPE : BIOINFORMATICS SYSTEM<br>
            TOOLS : Python, Streamlit, Biopython<br><br>
            Predicts circular DNA structures and generates reports.
            </div>
            """, unsafe_allow_html=True)

    # -------- LOGS --------
    elif st.session_state.module == "LOGS":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM LOGS</b><br><br>
        [2024-08] Oracle Cloud Developer Certified<br>
        [2024-06] Google Cyber Security Completed<br>
        [2023-12] Data Leak Tool Deployed
        </div>
        """, unsafe_allow_html=True)

    # -------- FILES --------
    elif st.session_state.module == "FILES":
        st.markdown("""
        <div class="panel">
        <b>FILE SYSTEM</b><br><br>
        /root/<br>
        ├── resume.pdf<br>
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



