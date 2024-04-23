from kafka import KafkaProducer
import json
import time

# Kafka broker address
bootstrap_servers = ['localhost:9092']

# Kafka topic to which data will be produced
topic = 'preprocessed_data'

# Function to read preprocessed data from JSON file and stream it to Kafka
def stream_preprocessed_data_to_kafka(producer, input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            producer.send(topic, json.dumps(json.loads(line)).encode('utf-8'))
            print(f"Line sent {line}")
            time.sleep(0.01)  # Adjust sleep time based on your throughput requirements

if __name__ == "__main__":
    # Create Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Path to the preprocessed data JSON file
    input_file = 'preprocessed_amazon_metadatafor 5 gb.json'

    # Stream preprocessed data to Kafka
    stream_preprocessed_data_to_kafka(producer, input_file)
