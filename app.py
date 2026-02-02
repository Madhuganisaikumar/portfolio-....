import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sai Kumar | Cyberpunk Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD CSS ----------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- FIRST LOAD BOOT SCREEN ----------------
if "booted" not in st.session_state:
    st.session_state.booted = False

if not st.session_state.booted:
    st.markdown("<div class='boot'>SYSTEM INITIALIZING</div>", unsafe_allow_html=True)
    progress = st.progress(0)

    logs = [
        "Loading core modules",
        "Initializing secure environment",
        "Verifying system integrity",
        "Mounting user profile",
        "Access granted"
    ]

    for i, log in enumerate(logs):
        st.markdown(f"<div class='boot-text'>{log}</div>", unsafe_allow_html=True)
        progress.progress((i + 1) * 20)
        time.sleep(0.35)

    st.session_state.booted = True
    st.rerun()

# ---------------- HERO / TERMINAL ----------------
st.markdown("""
<div class="terminal">
> whoami<br>
<span class="name">MADHUGANI SAI KUMAR</span><br><br>
ROLE: Software Engineer | Cybersecurity & AI<br>
STATUS: ACTIVE
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PROFILE ----------------
st.markdown("""
<div class="panel">
<b>PROFILE</b><br><br>
Final-year engineering student with strong problem-solving skills and hands-on experience in
Python, cybersecurity tools, and secure system design. Passionate about building scalable
software solutions and continuously improving through coding challenges and real-world projects.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SKILLS ----------------
st.markdown("## SYSTEM STATS")

skills = {
    "Python": 90,
    "Cybersecurity & Networking": 80,
    "Linux": 75,
    "MySQL / DBMS": 70,
    "Streamlit": 75
}

for skill, level in skills.items():
    st.markdown(f"<div class='skill'>{skill}</div>", unsafe_allow_html=True)
    st.progress(level)

st.markdown("---")

# ---------------- EDUCATION ----------------
st.markdown("""
<div class="panel">
<b>EDUCATION</b><br><br>

<b>Koneru Lakshmaiah Education Foundation</b><br>
B.Tech – Biotechnology (2022 – Present)<br>
CGPA: 8.67<br><br>

<b>Sri Chaitanya</b><br>
Intermediate (2019 – 2021)<br>
CGPA: 7.4<br><br>

<b>Sai Chaitanya</b><br>
SSC (2019)<br>
CGPA: 9.5
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PROJECTS ----------------
st.markdown("## MISSIONS")

st.markdown("""
<div class="panel">
<b>MISSION: DATA LEAK DETECTION TOOL</b><br>
TOOLS: Python, Regex, File System, Git<br><br>
• Detects sensitive data (passwords, API keys, personal info) in files and emails<br>
• Identifies vulnerabilities and prevents unauthorized data exposure
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="panel">
<b>MISSION: CIRCULAR DNA PREDICTION TOOL</b><br>
TOOLS: Python, Streamlit, Biopython, Matplotlib, FPDF<br><br>
• Predicts circular DNA structures from FASTA sequences<br>
• Detects repeats, ORFs, TATA box, polyA signals<br>
• Visualizes genomes and generates PDF reports<br>
• Deployed as a Streamlit web application
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- CERTIFICATIONS ----------------
st.markdown("""
<div class="panel">
<b>CERTIFICATIONS</b><br><br>
• Oracle Cloud Infrastructure – Certified Developer Professional<br>
• Oracle Cloud Infrastructure – Certified Networking Professional<br>
• Google Cyber Security<br>
• Salesforce AI Associate<br>
• Python Statcraft
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- RESUME DOWNLOAD (FIXED) ----------------
with open("resume.pdf.pdf", "rb") as file:
    st.download_button(
        label="⬇ Download Resume",
        data=file,
        file_name="Madhugani_Sai_Kumar_Resume.pdf"
    )

st.markdown("---")

# ---------------- CONTACT ----------------
st.markdown("""
<div class="terminal">
OPEN SECURE CHANNELS<br><br>
> Email: madhuganisai30@gmail.com<br>
> GitHub: https://github.com/Madhuganisaikumar<br>
> LinkedIn: https://linkedin.com/in/sai-madhugani<br>
> TryHackMe: https://tryhackme.com/r/p/Madhuganisai
</div>
""", unsafe_allow_html=True)
