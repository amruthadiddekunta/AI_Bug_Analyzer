import pandas as pd
import chromadb

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# -----------------------------
# Read Datasets
# -----------------------------

# Chromium dataset
chromium = pd.read_csv("data/archive/classifier_data_0.csv")
chromium = chromium.head(5000)

# Firefox dataset
firefox = pd.read_csv("data/firefox/Firefox_bugs.csv")

# -----------------------------
# Clean Datasets
# -----------------------------

chromium = chromium.dropna()
chromium = chromium.drop_duplicates()

firefox = firefox.dropna()
firefox = firefox.drop_duplicates()

# -----------------------------
# Create Bug Text
# -----------------------------

# Chromium has title + description
chromium["bug_text"] = (
    chromium["issue_title"] + "\n\n" + chromium["description"]
)

# Firefox only has Summary
firefox["bug_text"] = firefox["Summary"]

# -----------------------------
# Merge Datasets
# -----------------------------

df = pd.concat(
    [
        chromium[["bug_text"]],
        firefox[["bug_text"]],
    ],
    ignore_index=True,
)

# -----------------------------
# Chunking
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = []

for bug in df["bug_text"]:
    chunks.extend(text_splitter.split_text(bug))

# -----------------------------
# Load Embedding Model
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Create ChromaDB
# -----------------------------

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection("bug_reports")

# Add data only if database is empty
# Add data only if database is empty
if collection.count() == 0:

    batch_size = 512

    for start in range(0, len(chunks), batch_size):

        end = min(start + batch_size, len(chunks))

        batch = chunks[start:end]

        embeddings = model.encode(batch).tolist()

        collection.add(
            documents=batch,
            embeddings=embeddings,
            ids=[f"bug_{i}" for i in range(start, end)]
        )

        print(f"Stored {end} / {len(chunks)} chunks")

# -----------------------------
# Semantic Retrieval
# -----------------------------

new_bug = """
Scrolling with touchpad is not working correctly.
"""

query_embedding = model.encode([new_bug]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
)

print("\nMost Similar Historical Bugs:\n")

for i, bug in enumerate(results["documents"][0], start=1):
    print(f"Bug {i}")
    print(bug)
    print("-" * 60)