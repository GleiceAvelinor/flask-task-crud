"""Task CRUD API using Flask and Flasgger."""
from flasgger import Swagger
from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "API de Gerenciamento de Tarefas",
    "uiversion": 3,
    "openapi": "3.0.0",
    "version": "1.0.0",
    "description": "Documentação oficial da API de gerenciamento de tarefas.",
    "termsOfService": "",
    "contact": {
        "name": "Suporte",
        "email": "seu-email@exemplo.com",
    },
    "license": {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    "servers": [{"url": "http://127.0.0.1:5000", "description": "Servidor de Desenvolvimento"}],
}



swagger = Swagger(app)
tasks=[]

@app.route('/tasks', methods=['POST'])
def create_task():
    '''Cria uma nova tarefa
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
    responses:
      201:
        description: Tarefa criada com sucesso
    '''
    data = request.get_json()
    task = Task(task_id=len(tasks), title=data['title'], description=data['description'], completed=False)
    tasks.append(task)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    '''Lista todas as tarefas
    ---
    responses:
      200:
        description: Lista retornada com sucesso
    '''
    return jsonify({"tasks": [task.__dict__ for task in tasks]}), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    '''Busca uma tarefa pelo ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa encontrada
      404:
        description: Tarefa não encontrada
    '''
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify({"task": task.__dict__}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    '''Atualiza uma tarefa existente
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            completed:
              type: boolean
    responses:
      200:
        description: Tarefa atualizada com sucesso
      404:
        description: Tarefa não encontrada
    '''
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
    '''Deleta uma tarefa pelo ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa deletada com sucesso
    '''
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200




if __name__ == "__main__":
    app.run(debug=True)