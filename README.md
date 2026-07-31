# 🐞 AI Bug Analyzer & Fix Advisor

## 📌 Project Overview

AI Bug Analyzer & Fix Advisor is an AI-powered application that assists developers in analyzing software bug reports using **Retrieval-Augmented Generation (RAG)** and a **Multi-Agent Architecture**.

The system accepts bug reports through direct text input or file uploads, retrieves semantically similar historical defects, classifies bug severity and priority, analyzes stack traces, identifies probable root causes, detects duplicate issues, and recommends possible fixes using multiple AI agents.

This project is developed as part of the **Infosys Springboard Internship**.

---

# ✨ Features

- 📝 Paste bug reports directly
- 📂 Upload bug reports, log files, or PDF files
- 🧹 Data preprocessing and text chunking
- 🧠 Sentence Transformer embedding generation
- 🗂️ Historical Defect Knowledge Base
- 🔍 Semantic similarity search using RAG
- 🚦 Triage Agent
- 📄 Log Analysis Agent
- 🧠 Root Cause Analysis Agent
- 🔁 Duplicate Detection Agent
- 💡 Remediation Agent
- 🤖 Multi-Agent Orchestrator
- 💾 ChromaDB Vector Database
- 📊 Structured JSON Output
- 🌐 Interactive Streamlit Dashboard

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas |
| Text Chunking | LangChain RecursiveCharacterTextSplitter |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| Retrieval | Retrieval-Augmented Generation (RAG) |
| AI Architecture | Multi-Agent System |
| Version Control | Git & GitHub |

---

# 📂 Datasets

The Historical Defect Knowledge Base is built using public software bug datasets.

Datasets Used

- Firefox Bug Reports (Kaggle)
- Chromium Bug Reports (Kaggle)

> **Note:** Due to GitHub file size limitations, only sample datasets are included in this repository. Download the complete datasets separately and place them inside the `data/` directory.

---

# 📁 Project Structure

```text
AI_Bug_Analyzer/
│
├── agents/
│   ├── __init__.py
│   ├── triage_agent.py
│   ├── log_analysis_agent.py
│   ├── root_cause_agent.py
│   ├── duplicate_agent.py
│   ├── remediation_agent.py
│   └── orchestrator.py
│
├── data/
│   ├── archive/
│   └── firefox/
│
├── docs/
│   ├── Architecture.png
│   ├── Design_Document.md
│   └── Tech_Stack.md
│
├── rag/
│   ├── __init__.py
│   ├── embedding.py
│   ├── retrieval.py
│   └── vector_store.py
│
├── utils/
│   ├── __init__.py
│   └── save_results.py
│
├── uploads/
│
├── results/
│   └── bug_analysis.json
│
├── validate_agents.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🏗️ System Architecture

![Architecture](docs/Architecture.png)

---

# 📥 Clone the Repository

```bash
git clone https://github.com/amruthadiddekunta/AI_Bug_Analyzer.git
cd AI_Bug_Analyzer
```

---

# ⚙️ Installation

Create and activate a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run main.py
```

---

# 📌 Current Progress

## ✅ Milestone 1 Completed

Implemented:

- Bug Submission Module
- File Upload Support
- Historical Defect Knowledge Base
- Data Cleaning
- Bug Text Creation
- Text Chunking
- Embedding Generation
- ChromaDB Vector Database
- Semantic Retrieval using RAG
- Streamlit User Interface
- Design Documentation
- System Architecture
- Technical Documentation

---

## ✅ Milestone 2 Completed

Implemented:

- Triage Agent
- Log Analysis Agent
- Multi-Agent Orchestration
- Severity Prediction
- Priority Prediction
- Component Identification
- Confidence Score Generation
- Reasoning Generation
- Exception Type Extraction
- Failure Point Identification
- Affected Code Path Extraction
- Structured JSON Output
- Agent Validation using Firefox and Chromium datasets

---

## ✅ Milestone 3 Completed

Implemented:

- Root Cause Analysis Agent
- Duplicate Detection Agent
- Remediation Agent
- Structured Findings Dashboard
- Root Cause Hypothesis Generation
- Confidence Score Generation
- Supporting Historical Evidence
- Semantic Duplicate Detection
- Similarity Score Generation
- Historical Resolution Summaries
- Fix Recommendation Generation
- End-to-End Multi-Agent Pipeline

---

# 📊 Validation

The complete multi-agent pipeline was validated using Firefox and Chromium bug datasets.

Validation includes:

- RAG Retrieval Pipeline
- Triage Agent
- Log Analysis Agent
- Root Cause Agent
- Duplicate Detection Agent
- Remediation Agent
- Multi-Agent Orchestration
- Structured JSON Output

---

# 🔮 Future Enhancements

- 🤖 LLM-powered Root Cause Analysis
- 💡 LLM-based Bug Fix Recommendations
- 📊 Defect Analytics Dashboard
- 📈 Bug Trend Visualization
- 🔄 Continuous Learning Knowledge Base
- ☁️ Cloud Deployment
- 🔗 REST API Integration

---

# 👩‍💻 Developed By

**Diddekunta Amrutha**

Bachelor of Engineering (Computer Science and Engineering)

Nitte Meenakshi Institute of Technology, Bengaluru

---

# 📄 License

This project is developed for academic and educational purposes as part of the Infosys Springboard Internship Program.