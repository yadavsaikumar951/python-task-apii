# Python Task REST API

A simple RESTful API built using Python and Flask to manage tasks.

## Features
- Create tasks
- Retrieve all tasks
- Update tasks
- Mark tasks as completed
- Delete tasks

## Tech Stack
- Python
- Flask
- JSON file storage

## API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a task |
| PUT | /tasks/<id> | Update task |
| PATCH | /tasks/<id>/complete | Complete task |
| DELETE | /tasks/<id> | Delete task |

## How to Run
```bash
pip install -r requirements.txt
python app.py
