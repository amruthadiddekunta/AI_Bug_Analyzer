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
• Root Cause Agent
• Duplicate Detection Agent
• Remediation Agent
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

    st.success("✅ Milestone 1")
    st.success("✅ Milestone 2")
    st.info("🚀 Milestone 3")

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

        with st.spinner("Analyzing bug report..."):

            analysis = analyze_submission(bug_text)

        save_analysis(analysis)

        st.success("Analysis saved successfully!")
        st.caption("Saved as: results/bug_analysis.json")

        # -----------------------------------
        # Similar Historical Bugs
        # -----------------------------------

        st.markdown("---")

        st.subheader("🔍 Similar Historical Bugs")

        for i, bug in enumerate(
            analysis["duplicates"],
            start=1
        ):

            with st.expander(
                f"🐞 Similar Bug {i}"
            ):

                st.write(bug["summary"])

                st.write(
                    f"Similarity Score: "
                    f"{bug['similarity_score']:.2f}"
                )

        # -----------------------------------
        # Triage Analysis
        # -----------------------------------

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

        st.write("### Confidence")

        st.progress(confidence)

        st.write(f"{confidence*100:.0f}%")

        st.info(
            analysis["triage"]["reasoning"]
        )

        # -----------------------------------
        # Log Analysis
        # -----------------------------------

        st.markdown("---")

        st.subheader("📄 Log Analysis")

        left, right = st.columns(2)

        with left:

            st.success(
                analysis["log_analysis"]["exception_type"]
            )

        with right:

            st.success(
                analysis["log_analysis"]["failure_point"]
            )

        st.code(
            analysis["log_analysis"][
                "affected_code_path"
            ]
        )

        # -----------------------------------
        # Root Cause
        # -----------------------------------

        st.markdown("---")

        st.subheader("🧠 Root Cause Analysis")

        st.warning(
            analysis["root_cause"]["root_cause"]
        )

        rc = analysis["root_cause"]["confidence"]

        st.write("Confidence")

        st.progress(rc)

        st.write(f"{rc*100:.0f}%")

        st.write("Supporting Evidence")

        st.info(
            analysis["root_cause"][
                "supporting_evidence"
            ]
        )

        # -----------------------------------
        # Duplicate Detection
        # -----------------------------------

        st.markdown("---")

        st.subheader("🔁 Duplicate Detection")

        for i, bug in enumerate(
            analysis["duplicates"],
            start=1
        ):

            with st.expander(
                f"Duplicate {i}"
            ):

                st.write(
                    bug["summary"]
                )

                st.progress(
                    bug["similarity_score"]
                )

                st.write(
                    f"{bug['similarity_score']*100:.0f}% Similar"
                )

                st.success(
                    bug["resolution_summary"]
                )

        # -----------------------------------
        # Remediation
        # -----------------------------------

        st.markdown("---")

        st.subheader("💡 Recommended Fix")

        st.success(
            analysis["remediation"][
                "recommendation"
            ]
        )

        st.write("Based On")

        st.info(
            analysis["remediation"][
                "based_on"
            ]
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

            with st.spinner("Analyzing bug report..."):

                analysis = analyze_submission(file_text)

            save_analysis(analysis)

            st.success("Analysis saved successfully!")
            st.caption("Saved as: results/bug_analysis.json")

            # -----------------------------------
            # Similar Historical Bugs
            # -----------------------------------

            st.markdown("---")

            st.subheader("🔍 Similar Historical Bugs")

            for i, bug in enumerate(
                analysis["duplicates"],
                start=1
            ):

                with st.expander(
                    f"🐞 Similar Bug {i}"
                ):

                    st.write(bug["summary"])

                    st.write(
                        f"Similarity Score: "
                        f"{bug['similarity_score']:.2f}"
                    )

            # -----------------------------------
            # Triage Analysis
            # -----------------------------------

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

            st.write("### Confidence")

            st.progress(confidence)

            st.write(f"{confidence*100:.0f}%")

            st.info(
                analysis["triage"]["reasoning"]
            )

            # -----------------------------------
            # Log Analysis
            # -----------------------------------

            st.markdown("---")

            st.subheader("📄 Log Analysis")

            left, right = st.columns(2)

            with left:

                st.success(
                    analysis["log_analysis"]["exception_type"]
                )

            with right:

                st.success(
                    analysis["log_analysis"]["failure_point"]
                )

            st.code(
                analysis["log_analysis"][
                    "affected_code_path"
                ]
            )

            # -----------------------------------
            # Root Cause
            # -----------------------------------

            st.markdown("---")

            st.subheader("🧠 Root Cause Analysis")

            st.warning(
                analysis["root_cause"]["root_cause"]
            )

            rc = analysis["root_cause"]["confidence"]

            st.write("Confidence")

            st.progress(rc)

            st.write(f"{rc*100:.0f}%")

            st.write("Supporting Evidence")

            st.info(
                analysis["root_cause"][
                    "supporting_evidence"
                ]
            )

            # -----------------------------------
            # Duplicate Detection
            # -----------------------------------

            st.markdown("---")

            st.subheader("🔁 Duplicate Detection")

            for i, bug in enumerate(
                analysis["duplicates"],
                start=1
            ):

                with st.expander(
                    f"Duplicate {i}"
                ):

                    st.write(
                        bug["summary"]
                    )

                    st.progress(
                        bug["similarity_score"]
                    )

                    st.write(
                        f"{bug['similarity_score']*100:.0f}% Similar"
                    )

                    st.success(
                        bug["resolution_summary"]
                    )

            # -----------------------------------
            # Remediation
            # -----------------------------------

            st.markdown("---")

            st.subheader("💡 Recommended Fix")

            st.success(
                analysis["remediation"][
                    "recommendation"
                ]
            )

            st.write("Based On")

            st.info(
                analysis["remediation"][
                    "based_on"
                ]
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
    Infosys Springboard Internship Project
</div>
""",
    unsafe_allow_html=True,
)