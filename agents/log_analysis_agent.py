import re


def analyze_log(bug_text):

    exception_type = "Not Found"
    failure_point = "Not Found"
    affected_code_path = "Not Found"

    # Find Exception Type
    exception_match = re.search(r'(\w+Exception)', bug_text)

    if exception_match:
        exception_type = exception_match.group(1)

    # Find Failure Point
    failure_match = re.search(r'at\s+([\w\.]+)', bug_text)

    if failure_match:
        failure_point = failure_match.group(1)

    # Find Code Path
    code_path_match = re.search(r'([\w]+\.java:\d+)', bug_text)

    if code_path_match:
        affected_code_path = code_path_match.group(1)

    return {
        "exception_type": exception_type,
        "failure_point": failure_point,
        "affected_code_path": affected_code_path
    }