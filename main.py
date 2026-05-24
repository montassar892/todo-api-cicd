from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "task is required"}), 400
    todos.append(data['task'])
    return jsonify({"message": "Todo added"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
