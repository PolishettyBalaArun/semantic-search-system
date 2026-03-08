from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import re

print("Loading dataset...")

data = fetch_20newsgroups(subset="all")
documents = data.data

def clean_text(text):
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\n+', ' ', text)
    return text.strip()

documents = [clean_text(doc) for doc in documents]

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
embeddings = model.encode(documents, show_progress_bar=True)

dimension = embeddings.shape[1]

print("Creating FAISS index...")
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def embed_query(query):
    return model.encode([query])[0]


def search_similar(query_vector, k=5):
    D, I = index.search(np.array([query_vector]), k)
    results = [documents[i] for i in I[0]]
    return results