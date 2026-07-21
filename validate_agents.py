import pandas as pd

from agents.triage_agent import analyze_bug
from agents.log_analysis_agent import analyze_log

# ---------------------------------
# Load Firefox Dataset
# ---------------------------------

firefox = pd.read_csv("data/firefox/Firefox_bugs.csv")

# ---------------------------------
# Chromium Dataset Files
# ---------------------------------

chromium_files = [
    "data/archive/classifier_data_0.csv",
    "data/archive/classifier_data_5.csv",
    "data/archive/classifier_data_10.csv",
    "data/archive/classifier_data_20.csv",
    "data/archive/deep_data.csv"
]

total_reports = 0
triage_success = 0
log_success = 0

# ---------------------------------
# Validate Firefox Dataset
# ---------------------------------

for _, row in firefox.iterrows():

    bug_text = str(row["Summary"])

    triage = analyze_bug(bug_text)
    log = analyze_log(bug_text)

    total_reports += 1

    if triage:
        triage_success += 1

    if log:
        log_success += 1

# ---------------------------------
# Validate Chromium Datasets
# ---------------------------------

for file in chromium_files:

    df = pd.read_csv(file)

    for _, row in df.iterrows():

        title = ""
        description = ""

        if "issue_title" in df.columns:
            title = str(row["issue_title"])

        if "description" in df.columns:
            description = str(row["description"])

        elif "descriptionn" in df.columns:
            description = str(row["descriptionn"])

        bug_text = title + " " + description

        triage = analyze_bug(bug_text)
        log = analyze_log(bug_text)

        total_reports += 1

        if triage:
            triage_success += 1

        if log:
            log_success += 1

# ---------------------------------
# Validation Report
# ---------------------------------

print("\n==============================")
print(" Milestone 2 Validation Report")
print("==============================")

print(f"Total Bug Reports Tested : {total_reports}")

print(
    f"Triage Agent Success : {(triage_success / total_reports) * 100:.2f}%"
)

print(
    f"Log Analysis Agent Success : {(log_success / total_reports) * 100:.2f}%"
)

print("==============================")
print("Validation Completed")
print("==============================")