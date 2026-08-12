import json
import os
from collections import Counter


HISTORY_DIR = "results/history"


def load_all_results():
    """
    Load all previously saved bug analysis results.
    """

    results = []

    if not os.path.exists(HISTORY_DIR):
        return results

    for filename in os.listdir(HISTORY_DIR):

        if filename.endswith(".json"):

            file_path = os.path.join(
                HISTORY_DIR,
                filename
            )

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    data = json.load(file)

                    results.append(data)

            except Exception as e:

                print(
                    f"Could not read {filename}: {e}"
                )

    return results


def generate_analytics():
    """
    Analyze all historical bug results.
    """

    results = load_all_results()

    if not results:

        return {
            "total_bugs": 0,
            "severity_distribution": {},
            "priority_distribution": {},
            "component_distribution": {},
            "exception_distribution": {},
            "root_causes": {}
        }

    # ---------------------------------------------
    # Severity
    # ---------------------------------------------

    severities = []

    # ---------------------------------------------
    # Priority
    # ---------------------------------------------

    priorities = []

    # ---------------------------------------------
    # Components
    # ---------------------------------------------

    components = []

    # ---------------------------------------------
    # Exceptions
    # ---------------------------------------------

    exceptions = []

    # ---------------------------------------------
    # Root Causes
    # ---------------------------------------------

    root_causes = []

    for result in results:

        # Triage information
        triage = result.get(
            "triage",
            {}
        )

        severity = triage.get(
            "severity"
        )

        priority = triage.get(
            "priority"
        )

        component = triage.get(
            "component"
        )

        if severity:
            severities.append(severity)

        if priority:
            priorities.append(priority)

        if component:
            components.append(component)

        # Log analysis
        log_analysis = result.get(
            "log_analysis",
            {}
        )

        exception_type = log_analysis.get(
            "exception_type"
        )

        if exception_type:
            exceptions.append(exception_type)

        # Root cause
        root_cause = result.get(
            "root_cause",
            {}
        )

        root_cause_text = root_cause.get(
            "root_cause"
        )

        if root_cause_text:
            root_causes.append(root_cause_text)

    # ---------------------------------------------
    # Create frequency distributions
    # ---------------------------------------------

    severity_distribution = dict(
        Counter(severities)
    )

    priority_distribution = dict(
        Counter(priorities)
    )

    component_distribution = dict(
        Counter(components)
    )

    exception_distribution = dict(
        Counter(exceptions)
    )

    root_cause_distribution = dict(
        Counter(root_causes)
    )

    # ---------------------------------------------
    # Final analytics result
    # ---------------------------------------------

    analytics = {

        "total_bugs": len(results),

        "severity_distribution":
            severity_distribution,

        "priority_distribution":
            priority_distribution,

        "component_distribution":
            component_distribution,

        "exception_distribution":
            exception_distribution,

        "root_causes":
            root_cause_distribution
    }

    return analytics