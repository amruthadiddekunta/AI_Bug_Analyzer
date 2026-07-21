# AI Bug Analyzer & Fix Advisor

# Design Document

## 1. Problem Statement

Software developers spend significant time identifying similar historical bugs, understanding stack traces, determining bug severity, and finding the affected software components. Existing error messages are often difficult to interpret, resulting in slower debugging and issue resolution.

This project aims to simplify bug analysis using Artificial Intelligence, Retrieval-Augmented Generation (RAG), and a Multi-Agent Architecture.

---

## 2. Objective

The objective of this project is to develop an AI-powered system capable of:

- Accepting bug reports through text input or file upload
- Building a Historical Defect Knowledge Base
- Retrieving semantically similar historical bugs
- Automatically classifying bug severity and priority
- Identifying the affected component
- Extracting exception details from stack traces
- Producing structured outputs for downstream AI agents

---

## 3. System Architecture

### Implemented Modules

1. Bug Submission Module
2. Historical Defect Knowledge Base
3. RAG Retrieval Pipeline
4. Semantic Similarity Search
5. Triage Agent
6. Log Analysis Agent
7. Multi-Agent Orchestrator
8. Result Display Module
9. JSON Result Storage

### Future Modules

- Root Cause Analysis Agent
- Duplicate Detection Agent
- Remediation Suggestion Agent
- Defect Pattern Analytics Dashboard
- LLM-based Bug Fix Recommendation Agent

---

## 4. Workflow

1. User submits a bug report or uploads a log file.
2. The bug report is preprocessed.
3. Text is converted into embeddings using Sentence Transformers.
4. Embeddings are searched in ChromaDB using RAG.
5. Similar historical bugs are retrieved.
6. The Triage Agent predicts:
   - Severity
   - Priority
   - Affected Component
   - Confidence Score
   - Reasoning
7. The Log Analysis Agent extracts:
   - Exception Type
   - Failure Point
   - Affected Code Path
8. The Multi-Agent Orchestrator combines outputs from both agents.
9. Results are stored in a structured JSON file.
10. Results are displayed through the Streamlit interface.

---

## 5. Knowledge Base Design

The Historical Defect Knowledge Base stores:

- Bug ID
- Bug Description
- Bug Summary
- Embedding Vector

The vector database enables semantic retrieval instead of traditional keyword matching.

---

## 6. Multi-Agent Architecture

### Triage Agent

Responsibilities:

- Predict Severity
- Predict Priority
- Identify Affected Component
- Generate Confidence Score
- Generate Reasoning

Output:

- Severity
- Priority
- Component
- Confidence
- Reasoning

---

### Log Analysis Agent

Responsibilities:

- Parse stack traces
- Detect exception type
- Identify failure point
- Extract affected code path

Output:

- Exception Type
- Failure Point
- Affected Code Path

---

### Multi-Agent Orchestrator

Responsibilities:

- Execute Triage Agent
- Execute Log Analysis Agent
- Combine outputs
- Store results for future milestones

Output:

- Structured JSON file (`bug_analysis.json`)

---

## 7. Validation

Validation was performed using public Firefox and Chromium bug datasets.

Validation includes:

- Triage Agent execution
- Log Analysis Agent execution
- Multi-Agent orchestration
- Structured JSON generation

---

## 8. Technologies Used

- Python
- Streamlit
- Sentence Transformers
- ChromaDB
- LangChain
- Pandas
- Git
- GitHub

---

## 9. Expected Outcome

The system assists developers by:

- Retrieving similar historical bugs
- Predicting bug severity and priority
- Identifying affected components
- Extracting exception details from stack traces
- Producing structured outputs for downstream AI agents

This reduces manual debugging effort and improves software maintenance efficiency.

---

## 10. Future Scope

Future milestones will introduce:

- Root Cause Analysis Agent
- Duplicate Detection Agent
- Remediation Suggestion Agent
- Defect Analytics Dashboard
- LLM-powered Bug Fix Recommendations