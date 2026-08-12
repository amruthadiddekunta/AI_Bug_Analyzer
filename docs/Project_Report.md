1. Abstract

Software development teams regularly spend considerable time analyzing bug reports, understanding stack traces, identifying root causes, searching for previously reported issues, and determining suitable fixes. When these activities are performed manually, debugging and issue resolution can become time-consuming.

The AI Bug Analyzer & Fix Advisor is an AI-powered software defect analysis system developed using Python, Streamlit, Sentence Transformers, ChromaDB, Retrieval-Augmented Generation (RAG), and a Multi-Agent Architecture.

The system accepts bug reports through text input or file upload and processes them through multiple specialized agents. The system retrieves semantically similar historical bugs from a vector database and uses the retrieved information to support triage, log analysis, root-cause identification, duplicate detection, and remediation recommendations.

The project was further extended during Milestone 4 with a Defect Pattern Analytics module, a Knowledge Base Growth mechanism, and end-to-end testing using five different bug types. The final system successfully processed NullPointerException, FileNotFoundException, ArrayIndexOutOfBoundsException, SQLException, and IOException test cases through the complete analysis pipeline.

The testing demonstrated that the system can identify recurring defect patterns, retrieve related historical issues, generate structured analysis, and continuously grow its historical defect knowledge base through verified bug resolutions.

2. Introduction

Software bugs are an unavoidable part of software development. Developers need to investigate error messages, stack traces, affected components, previous incidents, and possible solutions before resolving a defect.

Traditional debugging generally requires developers to:

Read and understand bug reports manually
Search historical issue trackers
Identify similar defects
Analyze stack traces
Determine severity and priority
Identify possible root causes
Search for previous solutions
Recommend corrective actions

This process can become inefficient when organizations have large numbers of historical bug reports.

The AI Bug Analyzer & Fix Advisor addresses this problem by combining semantic search, Retrieval-Augmented Generation, and multiple specialized software defect analysis agents.

The project maintains a historical defect knowledge base containing previously analyzed bugs. New bug submissions are converted into semantic embeddings and compared against the historical knowledge base using ChromaDB. The retrieved information is then used by the analysis pipeline to provide relevant defect insights.

3. Project Objectives

The main objectives of the project are:

Develop an automated software defect analysis system.
Accept bug reports through text input and file upload.
Build a historical defect knowledge base.
Generate semantic embeddings for bug reports.
Retrieve similar historical bugs using ChromaDB.
Automatically determine bug severity and priority.
Identify affected software components.
Extract exception types and failure points from stack traces.
Identify probable root causes.
Detect duplicate or highly similar historical bugs.
Generate remediation recommendations.
Store analysis results in structured JSON format.
Develop defect pattern analytics.
Allow verified resolved bugs to be added to the knowledge base.
Perform end-to-end testing using multiple bug types.
Demonstrate the complete multi-agent analysis pipeline.
4. Project Overview

The final application provides an interactive Streamlit dashboard called:

AI Bug Analyzer & Fix Advisor

The application allows a user to submit a software defect either by:

Pasting a bug report or stack trace
Uploading a .txt file
Uploading a .log file
Uploading a PDF file

For supported text and log inputs, the submitted defect is passed through the analysis pipeline.

The final output contains:

Similar historical bugs
Severity
Priority
Affected component
Confidence score
Exception type
Failure point
Affected code path
Root cause
Supporting evidence
Duplicate detection results
Similarity scores
Recommended fix
Recommendation basis

The application also provides:

Knowledge Base Growth
Defect Pattern Analytics
Historical defect statistics
5. System Implementation
5.1 Bug Submission Module

The Bug Submission Module provides the user interface for entering defect information.

The Streamlit interface contains:

Bug report text area
File upload option
Analyze Bug button

Text-based submissions are stored locally before being processed.

Uploaded .txt and .log files are read as text and passed to the same analysis pipeline.

PDF uploads are currently accepted by the interface, while PDF-specific content analysis is reserved for future enhancement.

6. Embedding and Retrieval Implementation

The project uses the Sentence Transformers all-MiniLM-L6-v2 model to convert bug reports into numerical embedding vectors.

The embedding process allows the system to represent the semantic meaning of a bug report rather than relying only on exact keyword matching.

The generated embedding is stored and searched using ChromaDB.

The retrieval process follows these steps:

Receive the submitted bug report.
Generate its embedding.
Query the ChromaDB collection.
Retrieve the most similar historical bug reports.
Pass the retrieved results to the analysis pipeline.

The retrieval module uses a configurable number of results, with the current implementation retrieving the top three results.

This enables the system to identify historical bugs that are semantically related to a new submission.

7. Historical Defect Knowledge Base

The project maintains a historical defect knowledge base using ChromaDB.

The knowledge base contains historical bug information that can be retrieved when a new bug is submitted.

The stored information includes:

Bug ID
Bug description
Bug summary
Embedding information
Resolution information for verified bugs

The knowledge base is important because the analysis agents can use previous defects and their resolutions as supporting evidence.

8. Multi-Agent Analysis Pipeline

The system implements a multi-agent architecture consisting of five primary analysis agents and a central orchestrator.

The agents are:

Triage Agent
Log Analysis Agent
Root Cause Analysis Agent
Duplicate Detection Agent
Remediation Agent

The Multi-Agent Orchestrator coordinates the execution of these agents and combines their outputs.

8.1 Triage Agent

The Triage Agent analyzes the submitted defect and determines:

Severity
Priority
Affected component
Confidence
Reasoning

During testing, the submitted defects were classified with outputs such as:

Severity: High
Priority: P2

The component identification varied according to the submitted defect, including:

Authentication
General
Database
File Upload
8.2 Log Analysis Agent

The Log Analysis Agent analyzes stack traces and error information.

It identifies:

Exception type
Failure point
Affected code path

For example, during testing the system identified:

NullPointerException

with:

LoginService.authenticate

and:

LoginService.java:42

Similarly, other tests identified exceptions such as:

FileNotFoundException
ArrayIndexOutOfBoundsException
SQLException
IOException
8.3 Root Cause Analysis Agent

The Root Cause Analysis Agent uses the submitted defect and retrieved historical information to determine the most probable cause of the problem.

The output contains:

Root cause
Confidence score
Supporting evidence

Examples from testing included:

NullPointerException

A null object is being accessed before it has been initialized.

FileNotFoundException

The required file could not be located at the specified path.

ArrayIndexOutOfBoundsException

The code is accessing an index outside the valid collection size.

IOException

An input/output operation failed.

For the SQLException test, the system reported:

Unable to determine the exact root cause.

This demonstrates that the system can also indicate uncertainty when sufficient evidence is not available.

9. Duplicate Detection

The Duplicate Detection Agent performs semantic similarity search against historical defects.

The system displays:

Similar historical bug
Similarity score
Historical resolution summary

During testing, the ArrayIndexOutOfBoundsException test identified historical NullPointerException issues with similarity scores of approximately:

92%
89%

This demonstrates the use of semantic retrieval to identify potentially related historical defects.

10. Remediation Agent

The Remediation Agent generates a recommended solution based on the identified root cause and historical resolutions.

Examples from the five test cases included:

NullPointerException

Initialize objects before use and add null checks to prevent NullPointerException.

FileNotFoundException

Verify the file path exists and handle missing files using proper exception handling.

ArrayIndexOutOfBoundsException

Validate index values before accessing arrays or collections.

SQLException

Review the affected module, reproduce the issue, and follow software engineering best practices.

IOException

Handle I/O operations using try-catch blocks and ensure resources are available.

The remediation output provides developers with an initial actionable direction for resolving the reported defect.

11. Multi-Agent Orchestrator

The Multi-Agent Orchestrator coordinates the complete analysis process.

The general execution flow is:

Bug Submission
      ↓
Preprocessing
      ↓
Embedding Generation
      ↓
ChromaDB Retrieval
      ↓
Triage Agent
      ↓
Log Analysis Agent
      ↓
Root Cause Agent
      ↓
Duplicate Detection Agent
      ↓
Remediation Agent
      ↓
Orchestrator
      ↓
Structured JSON Result
      ↓
Streamlit Dashboard

The orchestrator combines the results generated by the individual agents into a structured analysis object.

The final results are saved using the project's JSON result storage mechanism.

12. Milestone 4 Implementation

Milestone 4 extended the project beyond the basic analysis pipeline.

The major additions were:

Defect Pattern Analytics
Knowledge Base Growth
End-to-End Testing
Technical documentation and final demonstration preparation
13. Defect Pattern Analytics

A Defect Pattern Analytics module was implemented to analyze historical bug results.

The analytics module calculates:

Total bugs analyzed
Severity distribution
Priority distribution
Component distribution
Exception distribution
Recurring root causes

The results are displayed through the Streamlit dashboard.

The analytics module provides an overview of recurring software defect patterns across analyzed submissions.

14. Analytics Results

During the five-test demonstration, the analytics dashboard accumulated historical analysis results.

The final observed dashboard showed:

Total Bugs Analyzed: 17

Unique Components: 4

Component Distribution
Component	Count
Authentication	3
General	8
Database	4
File Upload	2
Exception Distribution
Exception	Count
NullPointerException	3
FileNotFoundException	5
ArrayIndexOutOfBoundsException	3
SQLException	4
IOException	2
Recurring Root Causes
Root Cause	Count
A null object is being accessed before it has been initialized.	3
The required file could not be located at the specified path.	5
The code is accessing an index outside the valid collection size.	3
Unable to determine the exact root cause.	4
An input/output operation failed.	2

All 17 recorded analyses in this observed run were classified as:

Severity: High
Priority: P2

These values reflect the current project's analysis logic and test data; they should not be interpreted as independently validated production-grade classification accuracy.

15. Knowledge Base Growth Mechanism

A Knowledge Base Growth mechanism was implemented during Milestone 4.

After a bug has been resolved and its solution has been verified, the user can select:

"Bug has been resolved and verified"

The system then provides an option to:

"Add Verified Bug to Knowledge Base"

The verified bug and its resolution are then added to the historical defect knowledge base.

A generated bug ID is assigned to the verified entry.

For example, during testing, verified bug IDs were generated in the form:

verified_5170385313268718198

and similar unique identifiers for subsequent verified submissions.

This creates a feedback mechanism:

New Bug
   ↓
Analysis
   ↓
Recommended Fix
   ↓
Developer Verification
   ↓
Verified Resolution
   ↓
Knowledge Base
   ↓
Future Retrieval

The mechanism allows historical knowledge to grow as additional defects are resolved.

16. End-to-End Testing

End-to-end testing was performed using five different bug submissions.

Each test was submitted through the Streamlit application and processed through the analysis pipeline.

The five test cases were selected to represent different exception categories and software components.

17. Test Case 1 – NullPointerException
Input

A login-related bug containing:

java.lang.NullPointerException
at LoginService.authenticate(LoginService.java:42)
System Output

Severity: High

Priority: P2

Component: Authentication

Exception: NullPointerException

Failure Point:

LoginService.authenticate

Affected Code Path:

LoginService.java:42

Root Cause:

A null object is being accessed before it has been initialized.

Root Cause Confidence: 93%

Recommended Fix:

Initialize objects before use and add null checks to prevent NullPointerException.

Observation

The system successfully identified the exception type, affected service, code location, probable root cause, and recommended corrective action.

The resolved bug was also added to the knowledge base.

18. Test Case 2 – FileNotFoundException
Input

A configuration-related defect containing:

java.io.FileNotFoundException: config.properties
at FileService.loadConfig(FileService.java:25)
System Output

Severity: High

Priority: P2

Component: General

Exception: FileNotFoundException

Failure Point:

FileService.loadConfig

Affected Code Path:

FileService.java:25

Root Cause:

The required file could not be located at the specified path.

Root Cause Confidence: 90%

Recommended Fix:

Verify the file path exists and handle missing files using proper exception handling.

Observation

The system correctly identified the missing-file problem and retrieved historical file-related defects as supporting evidence.

The verified resolution was added to the knowledge base.

19. Test Case 3 – ArrayIndexOutOfBoundsException
Input

A user service defect containing:

java.lang.ArrayIndexOutOfBoundsException:
Index 10 out of bounds for length 10
at UserService.getUser(UserService.java:58)
System Output

Severity: High

Priority: P2

Component: General

Exception: ArrayIndexOutOfBoundsException

Failure Point:

UserService.getUser

Affected Code Path:

UserService.java:58

Root Cause:

The code is accessing an index outside the valid collection size.

Root Cause Confidence: 91%

Recommended Fix:

Validate index values before accessing arrays or collections.

The duplicate detection stage also retrieved similar historical defects.

Observed similarity scores included:

92%
89%
Observation

The system successfully identified an invalid index access and provided a specific corrective recommendation.

20. Test Case 4 – SQLException
Input

A database connection defect containing:

java.sql.SQLException:
Connection refused
at DatabaseService.connect(DatabaseService.java:31)
System Output

Severity: High

Priority: P2

Component: Database

Exception: SQLException

Failure Point:

DatabaseService.connect

Affected Code Path:

DatabaseService.java:31

Root Cause:

Unable to determine the exact root cause.

Root Cause Confidence: 60%

Recommended Fix:

Review the affected module, reproduce the issue, and follow software engineering best practices.

Observation

This test demonstrated an important behavior of the system: when the available evidence was insufficient for a precise root-cause conclusion, the system reported uncertainty instead of presenting a highly confident specific cause.

21. Test Case 5 – IOException
Input

A file-processing defect containing:

java.io.IOException:
Failed to read uploaded file
at FileUploadService.processFile(FileUploadService.java:47)
System Output

Severity: High

Priority: P2

Component: File Upload

Exception: IOException

Failure Point:

FileUploadService.processFile

Affected Code Path:

FileUploadService.java:47

Root Cause:

An input/output operation failed.

Root Cause Confidence: 88%

Recommended Fix:

Handle I/O operations using try-catch blocks and ensure resources are available.

Observation

The system identified the file-processing component and generated a relevant I/O-related remediation recommendation.

The verified bug was added to the historical knowledge base.

22. End-to-End Testing Summary
Test	Bug Type	Component	Root Cause Identified	Fix Recommended
1	NullPointerException	Authentication	Yes	Yes
2	FileNotFoundException	General	Yes	Yes
3	ArrayIndexOutOfBoundsException	General	Yes	Yes
4	SQLException	Database	Uncertain	Yes
5	IOException	File Upload	Yes	Yes

The five test cases covered different exception types, components, stack-trace formats, and defect scenarios.

23. Testing Observations

The end-to-end testing produced the following observations:

23.1 Exception Identification

The system successfully extracted different exception types from the submitted stack traces.

23.2 Failure Point Identification

The system identified relevant methods such as:

LoginService.authenticate
FileService.loadConfig
UserService.getUser
DatabaseService.connect
FileUploadService.processFile
23.3 Root Cause Analysis

The system generated specific root-cause explanations for most test cases.

For the SQLException test, the confidence was lower and the system reported that the exact root cause could not be determined.

23.4 Duplicate Detection

The semantic retrieval mechanism identified related historical defects and provided similarity scores where sufficiently similar records were available.

23.5 Remediation

Each test case produced a recommended corrective action.

23.6 Knowledge Base Growth

Verified defects were successfully added to the knowledge base after analysis.

23.7 Analytics

The analytics module accumulated results from the submitted defects and identified recurring exception types, components, and root causes.

24. Accuracy and Evaluation

The current Milestone 4 implementation focuses primarily on functional end-to-end validation rather than a formally benchmarked accuracy study.

The five test cases demonstrated that the complete pipeline can:

Accept bug submissions
Generate embeddings
Retrieve historical defects
Execute analysis agents
Generate structured results
Detect similar defects
Generate remediation recommendations
Add verified bugs to the knowledge base
Update defect analytics

The current test results do not provide sufficient evidence to claim a numerical overall accuracy percentage for the complete system.

A larger manually labeled evaluation dataset would be required to calculate reliable precision, recall, F1-score, retrieval accuracy, duplicate-detection accuracy, and root-cause accuracy.

25. Defect Analytics Findings

The observed analytics provide useful information about the accumulated test dataset.

The most frequent exception in the observed results was:

FileNotFoundException – 5 occurrences

The most frequently affected component was:

General – 8 occurrences

The most frequently observed recurring root cause was:

The required file could not be located at the specified path.

with 5 occurrences.

These results demonstrate how the analytics module can be used to identify recurring defect patterns in the analyzed dataset.

26. Challenges Encountered

During implementation, several technical challenges were encountered.

26.1 Vector Database Integration

The system required integration between the embedding model and ChromaDB for semantic retrieval.

26.2 Embedding Generation

The Sentence Transformers model had to be loaded and reused efficiently to generate embeddings for submitted defects.

26.3 Multi-Agent Integration

The outputs of individual agents had to be combined into a consistent structured format.

26.4 Knowledge Base Updates

A mechanism was required to safely add verified bugs and their resolutions back into the vector database.

26.5 Streamlit Integration

The complete backend analysis pipeline had to be connected to an interactive Streamlit interface.

26.6 Testing

Different bug formats and exception types had to be tested to verify that the pipeline worked across multiple scenarios.

27. Limitations

The current implementation has several limitations.

The current root-cause and remediation logic is not equivalent to a fully autonomous LLM-based debugging system.
The testing dataset is relatively small.
The five demonstration tests are not sufficient for statistically significant accuracy claims.
PDF analysis is not yet implemented as a complete extraction pipeline.
The system currently focuses primarily on textual bug reports and logs.
The current analytics module is based on stored analysis results and does not yet provide advanced time-series trend analysis.
Cloud deployment has not yet been implemented.
A production-grade REST API has not yet been implemented.
More extensive manually labeled datasets are required for rigorous agent-level evaluation.
28. Project Outcome

The final implementation successfully combines:

Bug submission
Semantic embedding
Vector retrieval
Historical defect knowledge
Multi-agent analysis
Duplicate detection
Root-cause analysis
Remediation recommendation
Knowledge-base growth
Defect analytics
Structured result storage
Interactive visualization

The five end-to-end demonstrations showed that different categories of defects can be processed through the complete pipeline.

The system also demonstrated continuous knowledge-base growth by allowing verified resolutions to be stored for future retrieval.

29. Future Improvements

The following improvements can be considered for future versions:

29.1 LLM-Based Analysis

Integrate a dedicated Large Language Model for deeper root-cause analysis and contextual reasoning.

29.2 Intelligent Code Analysis

Allow the system to analyze source-code files along with bug reports and stack traces.

29.3 Advanced Duplicate Detection

Improve duplicate detection using calibrated similarity thresholds and labeled historical duplicate pairs.

29.4 Advanced Analytics

Add:

Time-based defect trends
Component-wise severity analysis
Root-cause trends
Interactive charts
Defect frequency analysis
29.5 REST API

Expose the analysis pipeline through a REST API for integration with software development tools.

29.6 Cloud Deployment

Deploy the application to a cloud environment for access by distributed development teams.

29.7 Automated Feedback Loop

Automatically update the knowledge base after confirmed fixes while maintaining verification and quality controls.

30. Conclusion

The AI Bug Analyzer & Fix Advisor demonstrates how Artificial Intelligence, semantic retrieval, and multi-agent processing can be combined to support software defect analysis.

The project progressed from building a historical defect knowledge base and RAG retrieval pipeline to implementing specialized agents for triage, log analysis, root-cause analysis, duplicate detection, and remediation.

Milestone 4 extended the system with Defect Pattern Analytics, Knowledge Base Growth, and end-to-end validation.

Five different bug types were successfully processed:

NullPointerException
FileNotFoundException
ArrayIndexOutOfBoundsException
SQLException
IOException

The system successfully generated structured analysis for these submissions, identified relevant historical defects, provided remediation recommendations, and updated the knowledge base with verified resolutions.

The final project demonstrates a functional prototype for AI-assisted software defect analysis and provides a foundation for future improvements involving LLM-based reasoning, advanced analytics, source-code analysis, API integration, and cloud deployment.