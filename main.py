import os
import streamlit as st

from rag.retrieval import search_bug
from agents.orchestrator import analyze_submission
from utils.save_results import save_analysis

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Bug Analyzer",
    page_icon="🐞",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🐞 AI Bug Analyzer")

    st.markdown("---")

    st.subheader("Project")

    st.write("""
AI-powered Software Defect Analysis

Features:

• Retrieval-Augmented Generation (RAG)
• Triage Agent
• Log Analysis Agent
• Multi-Agent Orchestrator
""")

    st.markdown("---")

    st.subheader("Tech Stack")

    st.write("🐍 Python")
    st.write("🌐 Streamlit")
    st.write("🧠 Sentence Transformers")
    st.write("🗂️ ChromaDB")
    st.write("🤖 RAG")

    st.markdown("---")

    st.subheader("Milestones")

    st.success("Milestone 1")
    st.success("Milestone 2")

    st.markdown("---")

    st.caption("Developed By")
    st.write("Diddekunta Amrutha")

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("🐞 AI Bug Analyzer & Fix Advisor")

st.markdown("""
Analyze software bug reports using **Artificial Intelligence,
Retrieval-Augmented Generation (RAG), and Multi-Agent Analysis**.
""")

st.markdown("---")

os.makedirs("uploads", exist_ok=True)

st.subheader("📄 Submit Bug Report")

bug_text = st.text_area(
    "Paste Bug Report",
    height=250,
    placeholder="Paste bug report or stack trace..."
)

uploaded_file = st.file_uploader(
    "Upload Bug Report / Log File",
    type=["txt", "log", "pdf"]
)

if st.button("🚀 Analyze Bug"):

    # =====================================================
    # TEXT INPUT
    # =====================================================

    if bug_text:

        with open(
            "uploads/bug_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(bug_text)

        st.toast("Bug submitted successfully!")
        st.success("Bug submitted successfully!")

        with st.spinner("Searching historical bugs..."):

            similar_bugs = search_bug(bug_text)

        analysis = analyze_submission(bug_text)

        save_analysis(analysis)

        st.success("Analysis saved successfully!")
        st.caption("Saved as: results/bug_analysis.json")

        st.markdown("---")

        st.subheader("🔍 Similar Historical Bugs")

        for i, bug in enumerate(similar_bugs, start=1):

            with st.expander(f"🐞 Similar Bug {i}"):

                st.write(bug)

        st.markdown("---")

        st.subheader("🚦 Triage Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Severity",
            analysis["triage"]["severity"]
        )

        col2.metric(
            "Priority",
            analysis["triage"]["priority"]
        )

        col3.metric(
            "Component",
            analysis["triage"]["component"]
        )

        confidence = analysis["triage"]["confidence"]

        st.write("### Confidence Score")

        st.progress(confidence)

        st.write(f"{confidence*100:.0f}%")

        st.write("### Reasoning")

        st.info(
            analysis["triage"]["reasoning"]
        )

        st.markdown("---")

        st.subheader("📄 Log Analysis")

        left, right = st.columns(2)

        with left:

            st.write("### Exception Type")

            st.success(
                analysis["log_analysis"]["exception_type"]
            )

        with right:

            st.write("### Failure Point")

            st.success(
                analysis["log_analysis"]["failure_point"]
            )

        st.write("### Affected Code Path")

        st.code(
            analysis["log_analysis"]["affected_code_path"]
        )
    # =====================================================
    # FILE UPLOAD
    # =====================================================

    elif uploaded_file:

        file_path = f"uploads/{uploaded_file.name}"

        with open(file_path, "wb") as file:

            file.write(uploaded_file.getbuffer())

        st.toast("File uploaded successfully!")
        st.success("File uploaded successfully!")

        if uploaded_file.name.endswith((".txt", ".log")):

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                file_text = file.read()

            with st.spinner("Searching historical bugs..."):

                similar_bugs = search_bug(file_text)

            analysis = analyze_submission(file_text)

            save_analysis(analysis)

            st.success("Analysis saved successfully!")
            st.caption("Saved as: results/bug_analysis.json")

            st.markdown("---")

            st.subheader("🔍 Similar Historical Bugs")

            for i, bug in enumerate(similar_bugs, start=1):

                with st.expander(f"🐞 Similar Bug {i}"):

                    st.write(bug)

            st.markdown("---")

            st.subheader("🚦 Triage Analysis")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Severity",
                analysis["triage"]["severity"]
            )

            col2.metric(
                "Priority",
                analysis["triage"]["priority"]
            )

            col3.metric(
                "Component",
                analysis["triage"]["component"]
            )

            confidence = analysis["triage"]["confidence"]

            st.write("### Confidence Score")

            st.progress(confidence)

            st.write(f"{confidence*100:.0f}%")

            st.write("### Reasoning")

            st.info(
                analysis["triage"]["reasoning"]
            )

            st.markdown("---")

            st.subheader("📄 Log Analysis")

            left, right = st.columns(2)

            with left:

                st.write("### Exception Type")

                st.success(
                    analysis["log_analysis"]["exception_type"]
                )

            with right:

                st.write("### Failure Point")

                st.success(
                    analysis["log_analysis"]["failure_point"]
                )

            st.write("### Affected Code Path")

            st.code(
                analysis["log_analysis"]["affected_code_path"]
            )

        elif uploaded_file.name.endswith(".pdf"):

            st.info(
                "PDF analysis will be added in a future update."
            )

    else:

        st.warning(
            "Please paste a bug report or upload a file."
        )
# =====================================================
# Footer
# =====================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.caption("🐞 AI Bug Analyzer & Fix Advisor")

with col2:
    st.caption("Infosys Springboard Internship")

st.markdown(
    """
<div style="text-align:center; padding:10px;">
    <b>Developed by Diddekunta Amrutha</b><br>
    Computer Science & Engineering<br>
    Infosys SpringBoard
</div>
""",
    unsafe_allow_html=True,
)