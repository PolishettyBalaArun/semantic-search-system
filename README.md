# semantic-search-system

A Python-based semantic search system that finds the most relevant documents based on meaning instead of exact keyword matches.

## 🚀 Features

* Semantic text search using embeddings
* Document similarity ranking
* Query caching for faster repeated searches
* Clustering support for organizing documents
* Simple and modular Python implementation

## 🛠 Technologies Used

* Python
* Sentence Transformers / Embeddings
* NumPy
* Scikit-learn
* Cosine Similarity

## 📂 Project Structure

semantic-search-system
│
├── main.py                # Main program to run the search system
├── embeddings.py          # Generate embeddings for documents
├── clustering.py          # Document clustering logic
├── cache.py               # Query caching implementation
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

## ⚙️ Installation

Clone the repository:

git clone https://github.com/PolishettyBalaArun/semantic-search-system.git

Navigate to the project folder:

cd semantic-search-system

Install dependencies:

pip install -r requirements.txt

## ▶️ Run the Project

python main.py

## 💡 How It Works

1. Documents are converted into vector embeddings.
2. The user enters a search query.
3. The query is converted into an embedding.
4. Cosine similarity is used to find the most semantically similar documents.
5. Cached results are used for faster repeated queries.

## 📌 Future Improvements

* Add a web interface
* Use vector databases like FAISS
* Improve ranking with hybrid search

## 👤 Author

Bala Arun
