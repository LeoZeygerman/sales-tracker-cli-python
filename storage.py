import json

def load_data():
    try:
        with open('data/product.json', 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('data/product.json', 'w') as f:
        json.dump(data, f)