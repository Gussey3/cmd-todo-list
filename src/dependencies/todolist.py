from typing import Optional

from src.exceptions.todolist_exceptions import ToDoListNotInitializedError
from src.interfaces.itodolist import IToDoList

todo_list: Optional[IToDoList] = None

def get_todo_list() -> IToDoList:
    if todo_list is None:
        raise ToDoListNotInitializedError
    return todo_list
