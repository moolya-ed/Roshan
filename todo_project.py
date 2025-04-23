import json
import os
import uuid
def load_list():
    file_path = "data/todos.json"
    if not os.path.exists(file_path):
        print("File not found! Returning empty list.")
        return []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print("Error reading file:", e)
        return []
todos = load_list()
print("Todo List:", todos)
def get_todo_details(todo_id)
    todos = load_list()
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    raise Exception("404 Not Found: Todo with this ID does not exist.")
result = get_todo_details("7f3d774efcad4dcbbccd891c2b121860")
print(result)

def save_list(todo_list):
    file_path = "data/todos.json"
    try:
        with open(file_path, 'w') as file:
            json.dump(todo_list, file, indent=4)
            return "Todo list saved successfully."
    except Exception as e:
        print(" Error saving file:", e)
print(save_list(load_list()))

def remove_todo(todo_id):
    todos = load_list()
    updated_todos = [todo for todo in todos if todo['id'] != todo_id]
    if len(todos) == len(updated_todos):
        raise Exception("404 Not Found: Todo with this ID does not exist.")
    save_list(updated_todos)
    print(f"Todo with ID {todo_id} removed.")
remove_todo("7f3d774efcad4dcbbccd891c2b121860")

def update_todo(todo_id, new_data):
    todos = load_list()
    found = False
    for todo in todos:
        if todo['id'] == todo_id:
            todo.update(new_data)
            found = True
            break
    if not found:
        raise Exception("404 Not Found: Todo with this ID does not exist.")
    save_list(todos)
update_todo("8af52e54045b423aabaa9bcf7003ff4d", {
    "title": "Learn Python & Django",
    "doneStatus": True
})
def generate_id():
    return uuid.uuid4().hex
new_id = generate_id()
print(new_id)

def add_todo(new_todo):
    todos = load_list()
    new_todo['id'] = generate_id()
    todos.append(new_todo)
    save_list(todos)
    return new_todo
new_todo= {
    "title": "Start Selenium Practice",
    "description": "Complete first test case",
    "doneStatus": False
}
created = add_todo(new_todo)
print(created)

