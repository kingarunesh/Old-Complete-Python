from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from datetime import datetime as dt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=True, nullable=False)
    date = db.Column(db.String(100), nullable=False)


db.create_all()


#############################################################################
#
#           GET ALL TASKS
#
#############################################################################
@app.route("/get-all-task", methods=["GET"])
def home():
    # tasks = Task.query.all()
    tasks = Task.query.order_by(desc(Task.date)).all()

    task_list = []

    for task in tasks:
        task = {
            "id": task.id,
            "title": task.title,
            "date": task.date
        }

        task_list.append(task)
    
    return jsonify({
        "Length": len(task_list),
        "results": {
            "tasks":task_list
        }
        })


#############################################################################
#
#           CREATE NEW TASK
#
#############################################################################
@app.route("/add-new-task", methods=["POST"])
def add_new_task():

    data = request.json 
    task = Task.query.filter_by(title=data["title"]).first()

    if task == None:
        new_task = Task(
            title=data["title"],
            date = dt.now().strftime("%I:%M %p | %d %B %Y")
        )

        db.session.add(new_task)
        db.session.commit()

        return jsonify({
            "status": "Success",
            "message": "New task created successfully."
        }), 201
    else:
        return jsonify({
            "status": "Fail",
            "ERROR": "Please add unique Task."
        }), 400


#############################################################################
#
#           UPDATE TASK
#
#############################################################################
@app.route("/update-task/<int:task_id>", methods=["PATCH"])
def update_task(task_id):

    task = Task.query.get(task_id)

    if task == None:
        return jsonify({
            "status": "Fail",
            "ERROR": "Invalid task ID, Please enter valid task ID."
        }), 404

    if request.method == "PATCH":
        task.title = request.json["title"]

        db.session.add(task)
        db.session.commit()

        return jsonify({
            "status": "Success",
            "message": "Task has been updated successfully."
        }), 205


#############################################################################
#
#           DELETE TASK
#
#############################################################################
@app.route("/delete-task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get(task_id)

    if task == None:
        return jsonify({
            "status": "Fail",
            "ERROR": "Invalid Task ID, Please enter valid task ID."
        }), 404
    
    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "status":"success",
        "message": "Task has been deleted successfully."
    }), 301


if __name__ == "__main__":
    app.run(debug=True)
