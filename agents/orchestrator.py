from agents.triage_agent import analyze_bug
from agents.log_analysis_agent import analyze_log


def analyze_submission(bug_text):

    triage_result = analyze_bug(bug_text)

    log_result = analyze_log(bug_text)

    combined_result = {
        "triage": triage_result,
        "log_analysis": log_result
    }

    return combined_result