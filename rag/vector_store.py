import chromadb

# Create or connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = client.get_or_create_collection("bug_reports")


def get_collection():
    return collection