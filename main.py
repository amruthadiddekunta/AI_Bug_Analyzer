import os
import streamlit as st

st.set_page_config(page_title="AI Bug Analyzer", page_icon="🐞")

st.title("🐞 AI Bug Analyzer")

st.write("Upload a bug report or paste one below.")

os.makedirs("uploads", exist_ok=True)

bug_text = st.text_area("Paste Bug Report", height=250)

uploaded_file = st.file_uploader(
    "Upload Bug Report / Log File",
    type=["txt", "log", "pdf"]
)

if st.button("Analyze Bug"):

    if bug_text:
        with open("uploads/bug_report.txt", "w", encoding="utf-8") as file:
            file.write(bug_text)

    if uploaded_file:
        with open(f"uploads/{uploaded_file.name}", "wb") as file:
            file.write(uploaded_file.getbuffer())

    st.success("Bug submitted successfully!")