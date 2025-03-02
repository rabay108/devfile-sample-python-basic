from flask import Flask
import os

app = Flask(__name__)

# Simple in-memory storage with two default items
items = {
    "1": {"id": "1", "name": "Item 1", "description": "This is item 1"},
    "2": {"id": "2", "name": "Item 2", "description": "This is item 2"}
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values()))

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(items[item_id])

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
