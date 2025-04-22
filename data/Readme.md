#  Todo App

This is a simple **Todo Management System** built using **Python**.  
It helps to manage tasks like adding, viewing, updating, and deleting todos.

---

##  Features

-  Add new todo
-  View todo details
-  Update existing todo
-  Delete todo
-  Save and load todos using a JSON file

Each todo item includes:
- Title
- Description
- Done status (True/False)
- Unique ID (generated with UUID)

---

##  Technologies Used

- Python
- JSON (for data storage)
- UUID (to generate unique IDs)

---

##  Project Structure

todo-app/ ├── todo_app.py # Main Python file with all functions ├── data/ │ └── todos.json # File to store todo items in JSON format ├── README.md # Project documentation file 
##  Example Todo Format

Here’s how your todos will look inside the `todos.json` file:

```json
[
  {
    "title": "Learn Python",
    "description": "Finish basic tutorial",
    "doneStatus": false,
    "id": "123abc456"
  }
]
