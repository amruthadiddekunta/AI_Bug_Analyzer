from agents.triage_agent import analyze_bug
from agents.log_analysis_agent import analyze_log
from agents.root_cause_agent import analyze_root_cause
from agents.duplicate_agent import find_duplicates
from agents.remediation_agent import generate_remediation

from rag.retrieval import search_bug


def analyze_submission(bug_text):

    # ---------------------------------
    # Retrieve Similar Historical Bugs
    # ---------------------------------

    similar_bugs = search_bug(bug_text)

    # ---------------------------------
    # Triage Agent
    # ---------------------------------

    triage_result = analyze_bug(bug_text)

    # ---------------------------------
    # Log Analysis Agent
    # ---------------------------------

    log_result = analyze_log(bug_text)

    # ---------------------------------
    # Root Cause Agent
    # ---------------------------------

    root_cause_result = analyze_root_cause(
        bug_text,
        similar_bugs
    )

    # ---------------------------------
    # Duplicate Detection Agent
    # ---------------------------------

    duplicate_result = find_duplicates(
        similar_bugs
    )

    # ---------------------------------
    # Remediation Agent
    # ---------------------------------

    remediation_result = generate_remediation(
        bug_text,
        root_cause_result["root_cause"]
    )

    # ---------------------------------
    # Final Output
    # ---------------------------------

    combined_result = {

        "triage": triage_result,

        "log_analysis": log_result,

        "root_cause": root_cause_result,

        "duplicates": duplicate_result,

        "remediation": remediation_result

    }

    return combined_result