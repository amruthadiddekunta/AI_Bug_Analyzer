import json
import os
from datetime import datetime

# Create result directories
os.makedirs("results", exist_ok=True)
os.makedirs("results/history", exist_ok=True)


def save_analysis(result):

    # --------------------------------------------------
    # Save latest analysis
    # --------------------------------------------------

    with open(
        "results/bug_analysis.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )

    # --------------------------------------------------
    # Save analysis to history
    # --------------------------------------------------

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    history_file = (
        f"results/history/bug_analysis_{timestamp}.json"
    )

    with open(
        history_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )