from flask import Flask, request, jsonify
from models.task import Task


app = Flask(__name__)

tasks=[]

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(task_id=len(tasks), title=data['title'], description=data['description'], completed=False)
    tasks.append(task)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": [task.__dict__ for task in tasks]}), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify({"task": task.__dict__}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        task.title = data['title']
        task.description = data['description']
        task.completed = data['completed']
        return jsonify({"message": "Task updated successfully"}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200




if __name__ == "__main__":
    app.run(debug=True)
