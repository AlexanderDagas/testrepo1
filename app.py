from flask import Flask, request

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    task_text = task_data.get('task')
    print(f"Received task: {task_text}")
    return "Task received", 200

#test variable

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)