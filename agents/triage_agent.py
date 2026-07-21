import re


def analyze_bug(bug_text):

    bug_text = bug_text.lower()

    severity = "Low"
    priority = "P4"
    component = "General"
    confidence = 0.60
    reasoning = "No critical keywords found."

    # Severity and Priority

    if any(word in bug_text for word in ["crash", "fatal", "critical"]):
        severity = "Critical"
        priority = "P1"
        confidence = 0.98
        reasoning = "Bug indicates a system crash or critical failure."

    elif any(word in bug_text for word in ["exception", "error", "failed"]):
        severity = "High"
        priority = "P2"
        confidence = 0.92
        reasoning = "Bug contains exceptions or failure messages."

    elif any(word in bug_text for word in ["slow", "delay", "timeout"]):
        severity = "Medium"
        priority = "P3"
        confidence = 0.85
        reasoning = "Bug affects performance."

    # Component Detection

    if "login" in bug_text:
        component = "Authentication"

    elif "upload" in bug_text:
        component = "File Upload"

    elif "database" in bug_text or "sql" in bug_text:
        component = "Database"

    elif "payment" in bug_text:
        component = "Payment"

    elif "network" in bug_text:
        component = "Network"

    elif "ui" in bug_text or "button" in bug_text:
        component = "User Interface"

    return {
        "severity": severity,
        "priority": priority,
        "component": component,
        "confidence": confidence,
        "reasoning": reasoning
    }