import json
import itertools
from kafka import KafkaConsumer

class PCY:
    def __init__(self, min_support, hash_table_size):
        self.min_support = min_support
        self.hash_table_size = hash_table_size
        self.item_counts = {}
        self.pair_counts = {}
        self.frequent_items = set()
        self.frequent_pairs = set()

    def process_transaction(self, transaction):
        if transaction:
            for item in transaction:
                self.item_counts[item] = self.item_counts.get(item, 0) + 1

    def update_frequent_items(self):
        self.frequent_items = {item for item, count in self.item_counts.items() if count >= self.min_support}

    def hash_function(self, pair):
        return hash(pair) % self.hash_table_size

    def process_pairs(self, transaction):
        if transaction:
            pairs = itertools.combinations(sorted(transaction), 2)
            for pair in pairs:
                if all(item in self.frequent_items for item in pair):
                    hash_value = self.hash_function(pair)
                    self.pair_counts[hash_value] = self.pair_counts.get(hash_value, 0) + 1

    def update_frequent_pairs(self):
        try:
            self.frequent_pairs = {(item1, item2) for (item1, item2), count in self.pair_counts.items() if isinstance(item1, tuple) and count >= self.min_support}
        except TypeError as e:
            print(f"Error: TypeError occurred while updating frequent pairs: {e}")
            for pair, count in self.pair_counts.items():
                print(f"Pair: {pair}, Count: {count}")

    #def update_frequent_pairs(self):
    #try:
    #    self.frequent_pairs = {(item1, item2) for (item1, item2), count in self.pair_counts.items() if isinstance(item1, tuple) and count >= self.min_support}
    #except TypeError as e:
     #   print(f"Error: TypeError occurred while updating frequent pairs: {e}")
      #  for pair in self.pair_counts.keys():
       #     if not isinstance(pair, tuple):
        #        print(f"Problematic pair: {pair}")
            



    def print_frequent_itemsets(self):
        print("Frequent Itemsets:")
        for itemset in self.frequent_items:
            print(itemset)
        print("Frequent Pairs:")
        for pair in self.frequent_pairs:
            print(pair)

def consume_data(topic, pcy):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

    for message in consumer:
        data = json.loads(message.value)
        alsobuy_items = data.get('alsobuy')
        pcy.process_transaction(alsobuy_items)
        pcy.process_pairs(alsobuy_items)
        pcy.update_frequent_items()
        pcy.update_frequent_pairs()
        pcy.print_frequent_itemsets()

    consumer.close()

if __name__ == "__main__":
    min_support = 5  # Adjust this threshold as needed
    hash_table_size = 1000  # Adjust hash table size as needed
    pcy = PCY(min_support, hash_table_size)
    topic = 'preprocessed_data'
    consume_data(topic, pcy)
