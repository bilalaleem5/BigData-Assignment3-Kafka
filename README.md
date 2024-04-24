Kafka Stream Processing Project
Overview

This project demonstrates stream processing using Apache Kafka for analyzing transaction data. It includes components for data preprocessing, association rule mining, frequent itemset mining, sequential pattern mining, and K-means clustering.
Components

    Producer (producer.py):
        Kafka producer script to stream preprocessed data to the Kafka cluster.
        Reads preprocessed data from a JSON file and sends it to a Kafka topic.

    Consumers:
        Consumer 1 (consumer1.py):
            Implements Apriori algorithm for association rule mining.
            Consumes preprocessed data from Kafka and prints frequent itemsets.
        Consumer 2 (consumer2.py):
            Implements PCY algorithm for frequent itemset mining.
            Consumes preprocessed data from Kafka and prints frequent itemsets and pairs.
        Consumer 3 (consumer3.py):
            Implements Sequential Pattern Mining algorithm.
            Consumes preprocessed data from Kafka and prints frequent items and sequential patterns.
        Consumer 4 (consumer4.py):
            Implements K-Means clustering algorithm.
            Consumes preprocessed data from Kafka, clusters the data using K-Means, and prints cluster centroids.

    Preprocessing (preprocessing.py):
        Preprocesses raw data from a JSON file.
        Extracts relevant features and formats the data for stream processing.

    Bash Script (run.sh):
        Starts the Kafka producer and all consumer scripts.

Preprocessing

    Raw data is preprocessed using the preprocessing.py script.
    The script extracts relevant information and formats it for stream processing.
    Preprocessed data is stored in JSON format.

Setup Instructions

    Install Apache Kafka and Python dependencies (kafka-python, scikit-learn, etc.).
    Start the Kafka broker and create a topic named preprocessed_data.
    Run the preprocessing script (preprocessing.py) to prepare the data.
    Execute the bash script (run.sh) to start the Kafka producer and consumers.

Configuration

    Adjust parameters such as minimum support, batch size, hash table size, and number of clusters in the respective consumer scripts as needed.

Requirements

    Python 3.x
    Apache Kafka
    kafka-python library
    scikit-learn library

Notes

    Ensure that Kafka broker address and topic configuration are consistent across all scripts.
    Customize preprocessing logic and algorithms according to specific requirements.
