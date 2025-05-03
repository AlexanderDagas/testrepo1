# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    if not task_data or 'task' not in task_data:
        return jsonify({"error": "Bad request"}), 400
    
    tasks.append(task_data['task'])
    return jsonify({"message": "Task created", "task": task_data['task']}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
