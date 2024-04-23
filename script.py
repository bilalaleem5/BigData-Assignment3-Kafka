import json

# Function to preprocess data
def preprocess_data(item):
    cleaned_item = {
       
        "alsobuy": item.get("also_buy" , None)
    }
    return cleaned_item

# Function to save preprocessed data as JSON
def save_preprocessed_data(data, output_file):
    with open(output_file, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')  # Add newline after each JSON object

# Load the Sampled Amazon dataset and preprocess the data
json_file = 'meta_sampledagain.json'
output_file = 'preprocessed_amazon_metadatafor 5 gb.json'

batch_size = 1000  # Define batch size

with open(json_file, 'r', encoding='utf-8') as file:
    batch = []
    for idx, line in enumerate(file):
        item = json.loads(line)
        cleaned_item = preprocess_data(item)
        save_preprocessed_data(cleaned_item, output_file)

print("Preprocessing completed successfully!")
