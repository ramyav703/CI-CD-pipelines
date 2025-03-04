from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Sample in-memory database
todos = []

# Define Pydantic model for request validation
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# Create a new To-Do
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# Get all To-Dos
@app.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

# Get a single To-Do by ID
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "To-Do not found"}

# Update a To-Do
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    return {"error": "To-Do not found"}

# Delete a To-Do
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "To-Do deleted successfully"}

