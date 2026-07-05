from rag.embedding import generate_embedding
from rag.vector_store import get_collection


def search_bug(bug_text, n_results=3):
    """
    Search for similar historical bugs.
    """

    collection = get_collection()

    query_embedding = generate_embedding(bug_text)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]