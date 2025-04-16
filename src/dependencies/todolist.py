from typing import Optional

from src.exceptions.todolist_exceptions import ToDoListNotInitializedError
from src.interfaces.itodolistmanager import IToDoListManager

todo_list: Optional[IToDoListManager] = None

def get_todo_list() -> IToDoListManager:
    if todo_list is None:
        raise ToDoListNotInitializedError
    return todo_list
