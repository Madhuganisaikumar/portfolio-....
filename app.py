import streamlit as st
import time

st.set_page_config(
    page_title="Sai Kumar | Cyberpunk Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "booted" not in st.session_state:
    st.session_state.booted = False

if not st.session_state.booted:
    st.markdown("<div class='boot'>SYSTEM INITIALIZING</div>", unsafe_allow_html=True)
    progress = st.progress(0)

    logs = [
        "Loading core modules",
        "Initializing AI engine",
        "Verifying security layer",
        "Establishing secure session",
        "Access granted"
    ]

    for i, log in enumerate(logs):
        st.markdown(f"<div class='boot-text'>{log}</div>", unsafe_allow_html=True)
        progress.progress((i + 1) * 20)
        time.sleep(0.35)

    st.session_state.booted = True
    st.rerun()

st.markdown("""
<div class="terminal">
> whoami<br>
<span class="name">MADHUGANI SAI KUMAR</span><br><br>
ROLE: Software Engineer | AI Systems<br>
STATUS: ACTIVE
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/profile.png", width=220)

with col2:
    st.markdown("""
    <div class="panel">
    <b>PROFILE_001</b><br><br>
    Software Engineer specializing in AI, LLM systems,
    and full-stack development. Experienced in building
    real-world products like fraud detection platforms
    and intelligent document analyzers.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## SYSTEM STATS")

skills = {
    "Python": 92,
    "LLMs & AI": 85,
    "Streamlit": 88,
    "Blockchain": 70,
    "SQL": 75
}

for skill, level in skills.items():
    st.markdown(f"<div class='skill'>{skill}</div>", unsafe_allow_html=True)
    st.progress(level)

st.markdown("---")

st.markdown("## MISSIONS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="panel">
    <b>MISSION: CHAINGUARDIAN</b><br>
    TYPE: AI + BLOCKCHAIN<br>
    STATUS: DEPLOYED
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="panel">
    <b>MISSION: MEDICAL REPORT ANALYZER</b><br>
    TYPE: LLM SYSTEM<br>
    STATUS: ACTIVE
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="terminal">
OPEN SECURE CHANNELS<br><br>
> GitHub<br>
> LinkedIn<br>
> Email
</div>
""", unsafe_allow_html=True)
