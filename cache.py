import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCache:

    def __init__(self, threshold=0.85):

        self.threshold = threshold
        self.cache = []
        self.hit_count = 0
        self.miss_count = 0

    def search(self, query_vector):

        for entry in self.cache:

            sim = cosine_similarity(
                [query_vector],
                [entry["vector"]]
            )[0][0]

            if sim >= self.threshold:
                self.hit_count += 1
                return entry, sim

        self.miss_count += 1
        return None, None

    def add(self, query, vector, result, cluster):

        entry = {
            "query": query,
            "vector": vector,
            "result": result,
            "cluster": cluster
        }

        self.cache.append(entry)

    def stats(self):

        total = len(self.cache)

        total_requests = self.hit_count + self.miss_count

        hit_rate = 0
        if total_requests > 0:
            hit_rate = self.hit_count / total_requests

        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }

    def clear(self):

        self.cache = []
        self.hit_count = 0
        self.miss_count = 0