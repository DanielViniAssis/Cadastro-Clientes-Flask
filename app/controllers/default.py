from app import app
from flask import render_template, url_for, request, jsonify

from app.model.task import Task


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST', 'GET'])
def process():
    title = request.form['title']
    description = request.form['description']
    status = request.form.get('status', 'incompleta')
     
    if title and description:
        new_task = Task.create_task(title=title, description=description, status=status)
        return jsonify({'title': new_task.title, 'description': new_task.description})
    
@app.route("/process/list", methods=['POST'])
def dataList():
    tasks = Task.get_all_tasks()
    return render_template("index.html", tasks=tasks)
