from kafka import KafkaConsumer
import json
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

class KMeansClustering:
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)

    def update_clusters(self, data):
        flattened_data = [item for sublist in data for item in sublist]
        label_encoder = LabelEncoder()
        encoded_data = label_encoder.fit_transform(flattened_data)
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)
        self.kmeans.fit(encoded_data.reshape(-1, 1))  # Fit K-Means model with new data points

    def print_cluster_centroids(self):
        centroids = self.kmeans.cluster_centers_
        print("Current Cluster Centroids:")
        print(centroids)

def consume_data(topic, kmeans_cluster, batch_size=100):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    batch = []

    for message in consumer:
        data = json.loads(message.value)
        alsobuy_items = data.get('alsobuy')

        if alsobuy_items is not None:
            batch.append(alsobuy_items)

        if len(batch) >= batch_size:
            kmeans_cluster.update_clusters(batch)
            kmeans_cluster.print_cluster_centroids()
            batch = []

    consumer.close()

if __name__ == "__main__":
    n_clusters = 3  # Number of clusters, adjust as needed
    kmeans_cluster = KMeansClustering(n_clusters)
    topic = 'preprocessed_data'
    consume_data(topic, kmeans_cluster, batch_size=100)
