#!/bin/bash

# Navigate to Kafka directory
cd /home/bilal/kafka

# Run Zookeeper
echo "Starting Zookeeper..."
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Wait for Zookeeper to start
sleep 5

# Run Kafka server
echo "Starting Kafka server..."
bin/kafka-server-start.sh config/server.properties &

# Wait for Kafka server to start
sleep 5

# Create Kafka topic
echo "Creating Kafka topic..."
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic preprocessed_data

# Wait for topic creation
sleep 5

# Navigate back to the original directory
cd -

# Run Kafka producer
echo "Starting Kafka producer..."
python3 producer.py &

# Run Kafka consumers
echo "Starting Kafka consumers..."
python3 consumer1.py &
python3 consumer2.py &
python3 consumer3.py &
python3 consumer4.py &

echo "All Kafka processes started successfully."
