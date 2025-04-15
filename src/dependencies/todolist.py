from typing import Optional

from src.exceptions.todolist_exceptions import ToDoListNotInitializedError
from src.interfaces.idbmanager import IDBManager

todo_list: Optional[IDBManager] = None

def get_todo_list() -> IDBManager:
    if todo_list is None:
        raise ToDoListNotInitializedError
    return todo_list
