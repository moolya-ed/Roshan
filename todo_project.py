import json
import uuid
import os

def load_list(filename='data/todos.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return [] 
def get_todo_details(todo_list, todo_id):
    for todo in todo_list:
        if todo['id'] == todo_id:
            return todo
    raise ValueError(f"Todo with ID {todo_id} not found")

def save_list(todo_list, filename='data/todos.json'):
    with open(filename, 'w') as file:
        json.dump(todo_list, file, indent=4)

def generate_id():
    return str(uuid.uuid4())

def add_todo(todo_list, title, description):
    todo = {
        'id': generate_id(),
        'title': title,
        'description': description,
        'doneStatus': False
    }
    todo_list.append(todo)
    save_list(todo_list)

def update_todo(todo_list, todo_id, title=None, description=None, doneStatus=None):
    for todo in todo_list:
        if todo['id'] == todo_id:
            if title is not None:
                todo['title'] = title
            if description is not None:
                todo['description'] = description
            if doneStatus is not None:
                todo['doneStatus'] = doneStatus
            save_list(todo_list)
            return
    raise ValueError(f"Todo with ID {todo_id} not found")

def remove_todo(todo_list, todo_id):
    for todo in todo_list:
        if todo['id'] == todo_id:
            todo_list.remove(todo)
            save_list(todo_list)
            return
    raise ValueError(f"Todo with ID {todo_id} not found")  
print(load_list(filename='data/todos.json'))
print(get_todo_details(load_list(),'8af52e54045b423aabaa9bcf7003ff4d' ))
print(save_list(load_list(), filename='todos.json'))
print(generate_id())
add_todo(load_list(), "Buy groceries", "Milk, Eggs, Bread")
