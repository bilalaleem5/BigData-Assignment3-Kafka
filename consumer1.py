from kafka import KafkaConsumer
import json

class Apriori:
    def __init__(self, min_support):
        self.min_support = min_support
        self.item_counts = {}
        self.frequent_itemsets = []

    def process_transaction(self, transaction):
        if transaction is not None:
            for item in transaction:
                if item in self.item_counts:
                    self.item_counts[item] += 1
                else:
                    self.item_counts[item] = 1

    def update_frequent_itemsets(self):
        self.frequent_itemsets = [item for item, count in self.item_counts.items() if count >= self.min_support]

    def print_frequent_itemsets(self):
        print("Frequent Itemsets:")
        for itemset in self.frequent_itemsets:
            print(itemset)

def consume_data(topic, apriori, batch_size=100):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    batch = []

    for message in consumer:
        data = json.loads(message.value)
        alsobuy_items = data.get('alsobuy')  # Removed default value None
        print(alsobuy_items)
        apriori.process_transaction(alsobuy_items)

        if alsobuy_items is not None:  # Added check for None
            batch.append(alsobuy_items)

        if len(batch) >= batch_size:
            apriori.update_frequent_itemsets()
            apriori.print_frequent_itemsets()
            batch = []

    consumer.close()

if __name__ == "__main__":
    min_support = 5  # Adjust this threshold as needed
    apriori = Apriori(min_support)
    topic = 'preprocessed_data'
    consume_data(topic, apriori, batch_size=100)
