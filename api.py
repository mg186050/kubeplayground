from flask import Flask, jsonify, request
  
app = Flask(__name__)

# Sample data for demonstration purposes
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)