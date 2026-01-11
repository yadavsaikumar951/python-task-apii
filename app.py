from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file"""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks"""
    return jsonify(load_tasks()), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    """Create a new task"""
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Task title is required"}), 400

    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task"""
    data = request.get_json()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            save_tasks(tasks)
            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    """Mark task as completed"""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return jsonify({"message": "Task deleted"}), 200

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
