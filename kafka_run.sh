#!/bin/bash

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
