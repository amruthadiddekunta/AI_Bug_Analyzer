import os
import streamlit as st

from rag.retrieval import search_bug

st.set_page_config(page_title="AI Bug Analyzer", page_icon="🐞")

st.title("🐞 AI Bug Analyzer")

st.write("Upload a bug report or paste one below.")

os.makedirs("uploads", exist_ok=True)

bug_text = st.text_area(
    "Paste Bug Report",
    height=250
)

uploaded_file = st.file_uploader(
    "Upload Bug Report / Log File",
    type=["txt", "log", "pdf"]
)

if st.button("Analyze Bug"):

    if bug_text:

        with open(
            "uploads/bug_report.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(bug_text)

        st.success("Bug submitted successfully!")

        st.subheader("🔍 Similar Historical Bugs")

        similar_bugs = search_bug(bug_text)

        for i, bug in enumerate(similar_bugs, start=1):
            st.write(f"### Bug {i}")
            st.write(bug)

    elif uploaded_file:

        with open(
            f"uploads/{uploaded_file.name}",
            "wb"
        ) as file:
            file.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")

    else:
        st.warning("Please paste a bug report or upload a file.")