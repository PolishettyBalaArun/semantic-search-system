from sklearn.mixture import GaussianMixture
import numpy as np
from embeddings import embeddings

print("Training clustering model...")

num_clusters = 15

gmm = GaussianMixture(
    n_components=num_clusters,
    covariance_type="tied",
    random_state=42
)

gmm.fit(embeddings)

cluster_probs = gmm.predict_proba(embeddings)
dominant_clusters = np.argmax(cluster_probs, axis=1)


def predict_cluster(vector):
    probs = gmm.predict_proba([vector])[0]
    return int(np.argmax(probs))