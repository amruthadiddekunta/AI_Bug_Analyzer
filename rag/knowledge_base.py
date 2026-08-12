from rag.embedding import generate_embedding
from rag.vector_store import get_collection


def add_verified_bug(
    bug_text,
    resolution,
    bug_id
):
    """
    Add a verified and resolved bug
    to the historical defect knowledge base.
    """

    collection = get_collection()

    # Combine bug information and confirmed resolution
    document = f"""
Bug Report:
{bug_text}

Verified Resolution:
{resolution}
"""

    # Generate embedding using the existing model
    embedding = generate_embedding(document)

    # Add to ChromaDB
    collection.add(
        ids=[str(bug_id)],
        documents=[document],
        embeddings=[embedding],
        metadatas=[
            {
                "status": "verified_resolved",
                "resolution": resolution
            }
        ]
    )

    return {
        "status": "success",
        "message": "Verified bug added to knowledge base.",
        "bug_id": bug_id
    }
from rag.embedding import generate_embedding
from rag.vector_store import get_collection


def add_verified_bug(bug_text, resolution, bug_id):
    """
    Add a verified and resolved bug to the historical
    defect knowledge base.
    """

    collection = get_collection()

    # Combine bug information and verified resolution
    document = (
        bug_text
        + "\n\nVerified Resolution:\n"
        + resolution
    )

    # Generate embedding
    embedding = generate_embedding(document)

    # Add to ChromaDB
    collection.add(
        ids=[bug_id],
        documents=[document],
        embeddings=[embedding]
    )

    return {
        "bug_id": bug_id,
        "status": "added",
        "message": "Verified bug added to knowledge base"
    }