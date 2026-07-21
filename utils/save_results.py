import json
import os

os.makedirs("results", exist_ok=True)


def save_analysis(result):

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