from kafka import KafkaConsumer
import json
from collections import defaultdict

class SequentialPatternMiner:
    def __init__(self, min_support):
        self.min_support = min_support
        self.item_counts = defaultdict(int)
        self.sequence_counts = defaultdict(int)
        self.frequent_items = set()
        self.frequent_sequences = set()

    def process_transaction(self, transaction):
        if transaction is not None:
            for item in transaction:
                self.item_counts[item] += 1

    def update_frequent_items(self):
        self.frequent_items = {item for item, count in self.item_counts.items() if count >= self.min_support}

    def process_sequence(self, transaction):
        if transaction is not None:
            n = len(transaction)
            for i in range(n):
                for j in range(i+1, n):
                    sequence = tuple(transaction[i:j+1])
                    self.sequence_counts[sequence] += 1

    def update_frequent_sequences(self):
        self.frequent_sequences = {seq for seq, count in self.sequence_counts.items() if count >= self.min_support}

    def print_frequent_patterns(self):
        print("Frequent Items:")
        for item in self.frequent_items:
            print(item)
        print("Frequent Sequential Patterns:")
        for seq in self.frequent_sequences:
            print(seq)
def consume_data(topic, miner, batch_size=100):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    batch = []

    for message in consumer:
        data = json.loads(message.value)
        alsobuy_items = data.get('alsobuy')
        miner.process_transaction(alsobuy_items)
        miner.process_sequence(alsobuy_items)

        if alsobuy_items is not None:
            # Print frequent patterns after processing each transaction
            miner.update_frequent_items()
            miner.update_frequent_sequences()
            miner.print_frequent_patterns()

        if len(batch) >= batch_size:
            batch = []

    consumer.close()

if __name__ == "__main__":
    min_support = 5  # Adjust this threshold as needed
    miner = SequentialPatternMiner(min_support)
    topic = 'preprocessed_data'
    consume_data(topic, miner, batch_size=100)
