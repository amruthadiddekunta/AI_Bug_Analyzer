import re


def analyze_root_cause(bug_text, similar_bugs):
    """
    Identifies the probable root cause of a bug
    using the submitted bug report and similar
    historical bugs retrieved through RAG.
    """

    text = bug_text.lower()

    root_cause = "Unable to determine the exact root cause."
    confidence = 0.60

    # -----------------------------
    # Rule-Based Root Cause Detection
    # -----------------------------

    if "nullpointerexception" in text:
        root_cause = (
            "A null object is being accessed before "
            "it has been initialized."
        )
        confidence = 0.93

    elif "indexoutofboundsexception" in text:
        root_cause = (
            "The code is accessing an index outside "
            "the valid collection size."
        )
        confidence = 0.91

    elif "filenotfoundexception" in text:
        root_cause = (
            "The required file could not be located "
            "at the specified path."
        )
        confidence = 0.90

    elif "ioexception" in text:
        root_cause = (
            "An input/output operation failed."
        )
        confidence = 0.88

    elif "timeout" in text:
        root_cause = (
            "The operation exceeded the allowed "
            "execution time."
        )
        confidence = 0.86

    elif "authentication" in text or "login" in text:
        root_cause = (
            "Authentication process failed due to "
            "invalid credentials or login handling."
        )
        confidence = 0.84

    elif "network" in text:
        root_cause = (
            "A network connectivity issue prevented "
            "successful communication."
        )
        confidence = 0.82

    # -----------------------------
    # Supporting Evidence
    # -----------------------------

    evidence = []

    for bug in similar_bugs[:3]:
        evidence.append(bug)

    supporting_evidence = "\n".join(evidence)

    return {
        "root_cause": root_cause,
        "confidence": confidence,
        "supporting_evidence": supporting_evidence
    }