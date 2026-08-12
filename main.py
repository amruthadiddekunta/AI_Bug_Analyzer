import os
import streamlit as st

from agents.orchestrator import analyze_submission
from utils.save_results import save_analysis
from analytics.defect_analytics import generate_analytics
from rag.knowledge_base import add_verified_bug


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="AI Bug Analyzer",
    page_icon="🐞",
    layout="wide"
)


# =====================================================
# Session State
# =====================================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "current_bug_text" not in st.session_state:
    st.session_state.current_bug_text = ""

if "bug_analyzed" not in st.session_state:
    st.session_state.bug_analyzed = False


# =====================================================
# Sidebar
# =====================================================

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
• Defect Pattern Analytics
• Knowledge Base Growth
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
    st.success("✅ Milestone 3")
    st.success("✅ Milestone 4")

    st.markdown("---")

    st.caption("Developed By")
    st.write("Diddekunta Amrutha")


# =====================================================
# Main Page
# =====================================================

st.title("🐞 AI Bug Analyzer & Fix Advisor")

st.markdown("""
Analyze software bug reports using **Artificial Intelligence,
Retrieval-Augmented Generation (RAG), and Multi-Agent Analysis**.
""")

st.markdown("---")

os.makedirs("uploads", exist_ok=True)


# =====================================================
# Bug Submission
# =====================================================

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


# =====================================================
# Analyze Bug
# =====================================================

if st.button("🚀 Analyze Bug"):

    # =================================================
    # TEXT INPUT
    # =================================================

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

        # Save analysis in session
        st.session_state.analysis = analysis
        st.session_state.current_bug_text = bug_text
        st.session_state.bug_analyzed = True

        # Save result
        save_analysis(analysis)

        st.success("Analysis saved successfully!")

        st.caption(
            "Saved as: results/bug_analysis.json"
        )


    # =================================================
    # FILE UPLOAD
    # =================================================

    elif uploaded_file:

        file_path = (
            f"uploads/{uploaded_file.name}"
        )

        with open(
            file_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )

        st.toast("File uploaded successfully!")
        st.success("File uploaded successfully!")


        # =============================================
        # TXT / LOG FILE
        # =============================================

        if uploaded_file.name.endswith(
            (".txt", ".log")
        ):

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                file_text = file.read()


            with st.spinner(
                "Analyzing bug report..."
            ):

                analysis = analyze_submission(
                    file_text
                )


            # Save analysis in session
            st.session_state.analysis = analysis
            st.session_state.current_bug_text = file_text
            st.session_state.bug_analyzed = True

            # Save result
            save_analysis(analysis)

            st.success(
                "Analysis saved successfully!"
            )

            st.caption(
                "Saved as: results/bug_analysis.json"
            )


        # =============================================
        # PDF FILE
        # =============================================

        elif uploaded_file.name.endswith(
            ".pdf"
        ):

            st.info(
                "PDF analysis will be added "
                "in a future update."
            )


    # =================================================
    # NO INPUT
    # =================================================

    else:

        st.warning(
            "Please paste a bug report "
            "or upload a file."
        )


# =====================================================
# Display Analysis
# =====================================================

if st.session_state.analysis is not None:

    analysis = st.session_state.analysis


    # =================================================
    # Similar Historical Bugs
    # =================================================

    st.markdown("---")

    st.subheader(
        "🔍 Similar Historical Bugs"
    )

    for i, bug in enumerate(
        analysis["duplicates"],
        start=1
    ):

        with st.expander(
            f"🐞 Similar Bug {i}"
        ):

            st.write(
                bug["summary"]
            )

            st.write(
                f"Similarity Score: "
                f"{bug['similarity_score']:.2f}"
            )


    # =================================================
    # Triage Analysis
    # =================================================

    st.markdown("---")

    st.subheader(
        "🚦 Triage Analysis"
    )

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

    st.write(
        f"{confidence * 100:.0f}%"
    )

    st.info(
        analysis["triage"]["reasoning"]
    )


    # =================================================
    # Log Analysis
    # =================================================

    st.markdown("---")

    st.subheader(
        "📄 Log Analysis"
    )

    left, right = st.columns(2)

    with left:

        st.write("### Exception Type")

        st.success(
            analysis["log_analysis"][
                "exception_type"
            ]
        )

    with right:

        st.write("### Failure Point")

        st.success(
            analysis["log_analysis"][
                "failure_point"
            ]
        )

    st.write(
        "### Affected Code Path"
    )

    st.code(
        analysis["log_analysis"][
            "affected_code_path"
        ]
    )


    # =================================================
    # Root Cause Analysis
    # =================================================

    st.markdown("---")

    st.subheader(
        "🧠 Root Cause Analysis"
    )

    st.warning(
        analysis["root_cause"][
            "root_cause"
        ]
    )

    rc = analysis["root_cause"]["confidence"]

    st.write("### Confidence")

    st.progress(rc)

    st.write(
        f"{rc * 100:.0f}%"
    )

    st.write(
        "### Supporting Evidence"
    )

    st.info(
        analysis["root_cause"][
            "supporting_evidence"
        ]
    )


    # =================================================
    # Duplicate Detection
    # =================================================

    st.markdown("---")

    st.subheader(
        "🔁 Duplicate Detection"
    )

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
                f"{bug['similarity_score'] * 100:.0f}% Similar"
            )

            st.success(
                bug["resolution_summary"]
            )


    # =================================================
    # Remediation
    # =================================================

    st.markdown("---")

    st.subheader(
        "💡 Recommended Fix"
    )

    st.success(
        analysis["remediation"][
            "recommendation"
        ]
    )

    st.write(
        "### Based On"
    )

    st.info(
        analysis["remediation"][
            "based_on"
        ]
    )


# =====================================================
# Milestone 4 - Knowledge Base Growth
# =====================================================

st.markdown("---")

st.subheader(
    "📚 Knowledge Base Growth"
)

st.write(
    "Resolved bugs with verified fixes can be "
    "added back to the historical defect "
    "knowledge base."
)


if st.session_state.analysis is not None:

    verified = st.checkbox(
        "✅ Bug has been resolved and verified",
        key="verified_bug"
    )

    if verified:

        if st.button(
            "➕ Add Verified Bug to Knowledge Base"
        ):

            analysis = st.session_state.analysis

            bug_text_for_kb = (
                st.session_state.current_bug_text
            )

            resolution = (
                analysis["remediation"][
                    "recommendation"
                ]
            )

            bug_id = (
                "verified_"
                + str(
                    abs(
                        hash(
                            bug_text_for_kb
                        )
                    )
                )
            )

            try:

                result = add_verified_bug(
                    bug_text=bug_text_for_kb,
                    resolution=resolution,
                    bug_id=bug_id
                )

                st.success(
                    "✅ Verified bug added to "
                    "the knowledge base!"
                )

                st.info(
                    f"Bug ID: {bug_id}"
                )

                st.write(
                    "The verified bug can now be "
                    "used for future semantic retrieval."
                )

            except Exception as e:

                st.error(
                    f"Unable to add bug to knowledge base: {e}"
                )

else:

    st.info(
        "Analyze a bug first to enable "
        "Knowledge Base Growth."
    )


# =====================================================
# Milestone 4 - Defect Pattern Analytics
# =====================================================

st.markdown("---")

st.subheader(
    "📊 Defect Pattern Analytics"
)

analytics = generate_analytics()


if analytics["total_bugs"] == 0:

    st.info(
        "No historical bug analyses available yet."
    )

else:

    # =================================================
    # Analytics Summary
    # =================================================

    st.write(
        "### 📈 Analytics Summary"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Bugs Analyzed",
            analytics["total_bugs"]
        )

    with col2:

        st.metric(
            "Unique Components",
            len(
                analytics[
                    "component_distribution"
                ]
            )
        )


    # =================================================
    # Severity Distribution
    # =================================================

    st.write(
        "### 🚦 Severity Distribution"
    )

    severity_data = analytics[
        "severity_distribution"
    ]

    for severity, count in severity_data.items():

        st.write(
            f"**{severity}:** {count}"
        )

        st.progress(
            count / analytics["total_bugs"]
        )


    # =================================================
    # Priority Distribution
    # =================================================

    st.write(
        "### 🎯 Priority Distribution"
    )

    priority_data = analytics[
        "priority_distribution"
    ]

    for priority, count in priority_data.items():

        st.write(
            f"**{priority}:** {count}"
        )

        st.progress(
            count / analytics["total_bugs"]
        )


    # =================================================
    # Frequently Affected Components
    # =================================================

    st.write(
        "### 🧩 Frequently Affected Components"
    )

    component_data = analytics[
        "component_distribution"
    ]

    for component, count in component_data.items():

        st.write(
            f"**{component}:** {count}"
        )

        st.progress(
            count / analytics["total_bugs"]
        )


    # =================================================
    # Common Exception Types
    # =================================================

    st.write(
        "### ⚠️ Common Exception Types"
    )

    exception_data = analytics[
        "exception_distribution"
    ]

    for exception, count in exception_data.items():

        st.write(
            f"**{exception}:** {count}"
        )

        st.progress(
            count / analytics["total_bugs"]
        )


    # =================================================
    # Recurring Root Causes
    # =================================================

    st.write(
        "### 🧠 Recurring Root Causes"
    )

    root_cause_data = analytics[
        "root_causes"
    ]

    for root_cause, count in root_cause_data.items():

        st.write(
            f"**{root_cause}:** {count}"
        )


# =====================================================
# Footer
# =====================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.caption(
        "🐞 AI Bug Analyzer & Fix Advisor"
    )

with col2:

    st.caption(
        "Infosys Springboard Internship"
    )


st.markdown(
    """
<div style="text-align:center; padding:10px;">
    <b>Developed by Diddekunta Amrutha</b><br>
    Computer Science & Engineering<br>
    Infosys Springboard Internship Project
</div>
""",
    unsafe_allow_html=True
)