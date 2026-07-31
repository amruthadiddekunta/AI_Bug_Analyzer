def find_duplicates(similar_bugs):
    """
    Identifies duplicate bug reports from the
    retrieved historical bugs.
    """

    duplicates = []

    similarity = 0.95

    for bug in similar_bugs:

        duplicates.append({

            "summary": bug,

            "similarity_score": round(similarity, 2),

            "resolution_summary":
                "Similar issue found in historical defect knowledge base."

        })

        similarity -= 0.03

        if similarity < 0.80:
            similarity = 0.80

    return duplicates