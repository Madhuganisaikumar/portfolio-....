import streamlit as st
import time
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

if "terminal_output" not in st.session_state:
    st.session_state.terminal_output = [
        "Secure system online.",
        "Type 'help' to list available commands."
    ]

# ---------------- BOOT SCREEN (FIRST LOAD) ----------------
if not st.session_state.booted:
    st.markdown("<div class='boot'>INITIALIZING PROTECTED SYSTEM</div>", unsafe_allow_html=True)
    progress = st.progress(0)

    logs = [
        "Mounting secure filesystem",
        "Loading security modules",
        "Initializing AI subsystems",
        "Verifying access policies",
        "System ready"
    ]

    for i, log in enumerate(logs):
        st.markdown(f"<div class='boot-text'>{log}</div>", unsafe_allow_html=True)
        progress.progress((i + 1) * 20)
        time.sleep(0.35)

    st.session_state.booted = True
    st.rerun()

# ---------------- BACKGROUND SCAN LINE ----------------
st.markdown("<div class='scanline'></div>", unsafe_allow_html=True)

# ---------------- TOP SYSTEM BAR ----------------
current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(f"""
<div class="topbar">
<span class="status-dot"></span>
root@sai-secure-node | ACCESS: READ_ONLY | CPU ▓▓▓░ | {current_time}
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

# ---------------- TERMINAL COMMAND HANDLER ----------------
def handle_command(cmd):
    cmd = cmd.lower().strip()

    if cmd == "help":
        return [
            "Available commands:",
            "overview  | system overview",
            "data      | credentials & languages",
            "skills    | skill core",
            "projects  | operations list",
            "logs      | system activity",
            "files     | file system",
            "resume    | download resume"
        ]

    if cmd in ["overview"]:
        st.session_state.module = "OVERVIEW"
        return ["Accessing SYSTEM OVERVIEW..."]

    if cmd in ["data"]:
        st.session_state.module = "DATA"
        return ["Accessing SYSTEM DATA..."]

    if cmd in ["skills"]:
        st.session_state.module = "SKILLS"
        return ["Accessing SKILL CORE..."]

    if cmd in ["projects"]:
        st.session_state.module = "PROJECTS"
        return ["Accessing PROJECT MODULE..."]

    if cmd in ["logs"]:
        st.session_state.module = "LOGS"
        return ["Accessing ACTIVITY LOGS..."]

    if cmd in ["files"]:
        st.session_state.module = "FILES"
        return ["Accessing FILE SYSTEM..."]

    if cmd in ["resume"]:
        st.session_state.module = "FILES"
        return ["Resume file ready for download."]

    return ["Command not recognized. Type 'help'."]

# ---------------- WORKSPACE ----------------
with right:
    st.markdown("<div class='workspace slide'>", unsafe_allow_html=True)

    # ---- SYSTEM OVERVIEW ----
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

    # ---- SYSTEM DATA ----
    elif st.session_state.module == "DATA":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM DATA</b><br><br>
        VERIFIED CREDENTIALS:<br>
        • Oracle Cloud Developer Professional<br>
        • Oracle Cloud Networking Professional<br>
        • Google Cyber Security<br>
        • Salesforce AI Associate<br><br>
        LANGUAGES:<br>
        • English<br>
        • Telugu<br>
        • Hindi
        </div>
        """, unsafe_allow_html=True)

    # ---- SKILLS ----
    elif st.session_state.module == "SKILLS":
        st.markdown("<div class='panel'><b>SKILL CORE</b></div>", unsafe_allow_html=True)
        skills = {
            "Python Engine": 90,
            "Network Security": 80,
            "Linux Systems": 75,
            "Streamlit UI Core": 75,
            "Database Systems": 70
        }
        for s, v in skills.items():
            st.markdown(f"<div class='skill'>{s}</div>", unsafe_allow_html=True)
            st.progress(v)

    # ---- PROJECTS ----
    elif st.session_state.module == "PROJECTS":
        st.markdown("""
        <div class="panel">
        <b>OPERATION: DATA LEAK DETECTION</b><br>
        TYPE : SECURITY TOOL<br>
        TOOLS : Python, Regex, Git<br><br>
        Detects sensitive data exposure and filesystem vulnerabilities.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="panel">
        <b>OPERATION: CIRCULAR DNA ANALYSIS</b><br>
        TYPE : BIOINFORMATICS SYSTEM<br>
        TOOLS : Python, Streamlit, Biopython<br><br>
        Predicts circular DNA structures and generates reports.
        </div>
        """, unsafe_allow_html=True)

    # ---- LOGS ----
    elif st.session_state.module == "LOGS":
        st.markdown("""
        <div class="panel">
        <b>SYSTEM ACTIVITY LOGS</b><br><br>
        [2024-08] Oracle Cloud Certified Developer<br>
        [2024-06] Google Cyber Security Completed<br>
        [2023-12] Data Leak Detection Tool Deployed<br>
        [2023-09] Streamlit Research App Released
        </div>
        """, unsafe_allow_html=True)

    # ---- FILE SYSTEM ----
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

# ---------------- TERMINAL PANEL ----------------
st.markdown("<div class='terminal-box'>", unsafe_allow_html=True)

for line in st.session_state.terminal_output[-8:]:
    st.markdown(f"<div class='terminal-line'>{line}</div>", unsafe_allow_html=True)

command = st.text_input(">", key="terminal_input")

if command:
    st.session_state.terminal_output.append(f"> {command}")
    output_lines = handle_command(command)
    st.session_state.terminal_output.extend(output_lines)
    st.session_state.terminal_input = ""

st.markdown("</div>", unsafe_allow_html=True)


