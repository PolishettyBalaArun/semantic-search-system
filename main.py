from fastapi import FastAPI
from pydantic import BaseModel

from embeddings import embed_query, search_similar
from clustering import predict_cluster
from cache import SemanticCache


app = FastAPI()

cache = SemanticCache(threshold=0.85)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_api(request: QueryRequest):

    query = request.query

    query_vector = embed_query(query)

    entry, sim = cache.search(query_vector)

    if entry:

        return {
            "query": query,
            "cache_hit": True,
            "matched_query": entry["query"],
            "similarity_score": float(sim),
            "result": entry["result"],
            "dominant_cluster": entry["cluster"]
        }

    result = search_similar(query_vector)

    cluster = predict_cluster(query_vector)

    cache.add(query, query_vector, result, cluster)

    return {
        "query": query,
        "cache_hit": False,
        "matched_query": None,
        "similarity_score": None,
        "result": result,
        "dominant_cluster": cluster
    }


@app.get("/cache/stats")
def cache_stats():

    return cache.stats()


@app.delete("/cache")
def clear_cache():

    cache.clear()

    return {"message": "Cache cleared"}