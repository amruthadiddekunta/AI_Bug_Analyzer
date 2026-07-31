def generate_remediation(bug_text, root_cause):

    """
    Generates fix recommendations based on
    the bug report and predicted root cause.
    """

    text = bug_text.lower()

    recommendation = (
        "Review the affected module, reproduce the issue, "
        "and follow software engineering best practices."
    )

    if "nullpointerexception" in text:
        recommendation = (
            "Initialize objects before use and add null checks "
            "to prevent NullPointerException."
        )

    elif "indexoutofboundsexception" in text:
        recommendation = (
            "Validate index values before accessing arrays or collections."
        )

    elif "filenotfoundexception" in text:
        recommendation = (
            "Verify the file path exists and handle missing files "
            "using proper exception handling."
        )

    elif "ioexception" in text:
        recommendation = (
            "Handle I/O operations using try-catch blocks and "
            "ensure resources are available."
        )

    elif "timeout" in text:
        recommendation = (
            "Increase timeout limits if appropriate and "
            "optimize long-running operations."
        )

    elif "authentication" in text or "login" in text:
        recommendation = (
            "Validate user credentials, session handling, "
            "and authentication logic."
        )

    elif "network" in text:
        recommendation = (
            "Check network connectivity, server availability, "
            "and implement retry mechanisms."
        )

    return {
        "recommendation": recommendation,
        "based_on": root_cause
    }