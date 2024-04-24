from kafka import KafkaProducer
import json
import time
from pymongo import MongoClient

# Kafka broker address
bootstrap_servers = ['localhost:9092']
# Kafka topic to which data will be produced
topic = 'preprocessed_data'
# MongoDB connection details
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['mydatabase']
collection = db['preprocessed_data']

def stream_preprocessed_data_to_kafka_and_mongodb(producer, input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            producer.send(topic, json.dumps(data).encode('utf-8'))
            collection.insert_one(data)  # Insert data into MongoDB
            print(f"Line sent and inserted into MongoDB: {line}")
            time.sleep(0.01)  # Adjust sleep time based on your throughput requirements

if __name__ == "__main__":
    # Create Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    # Path to the preprocessed data JSON file
    input_file = 'preprocessed_amazon_metadatafor 5 gb.json'
    # Stream preprocessed data to Kafka and MongoDB
    stream_preprocessed_data_to_kafka_and_mongodb(producer, input_file)
