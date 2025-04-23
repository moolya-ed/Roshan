import json
import os
import uuid

FILE_PATH = "data/todos.json"

def load_list():
    if not FILE_PATH:
        raise ValueError("File path cannot be empty.")
    if not os.path.exists(FILE_PATH):
        print(" Warning: Todo file not found. Returning an empty list.")
        return []
    try:
        with open(FILE_PATH, "r") as file:
            todos = json.load(file)
            return todos
    except Exception as e:
        print(f"Error reading todos: {e}")
        return []

def save_list(todo_list):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(todo_list, file, indent=4)
    except Exception as e:
        print(f"Error saving todos: {e}")

def get_todo_details(todo_id):
    todos = load_list()
    for todo in todos:
        if todo.get("id") == todo_id:
            return todo
    raise Exception(f"404 Not Found: Todo with ID {todo_id} not found.")

def remove_todo(todo_id):
    todos = load_list()
    new_todos = [todo for todo in todos if todo.get("id") != todo_id]
    if len(new_todos) == len(todos):
        raise Exception(f"404 Not Found: Todo with ID {todo_id} not found.")
    save_list(new_todos)

def update_todo(todo_id, new_data):
    todos = load_list()
    found= False
    for todo in todos:
        if todo.get("id") == todo_id:
            todo.update(new_data)
            found = True
            break
    if not found:
        raise Exception(f"404 Not Found: Todo with ID {todo_id} not found.")
    save_list(todos)

def generate_id():
    return uuid.uuid4().hex