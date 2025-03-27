from os import getenv

from console import ConsoleControl
from src.implementations.todolist_psql.todolist_psql import ToDoListPsql
from src.implementations.todolist_json.todolist_json import ToDoListJson
from db import settings


if __name__ == "__main__":
    match settings.db_source:
        case "psql":
            todo_list = ToDoListPsql()
        case "json":
            todo_list = ToDoListJson()
        case _:
            raise ValueError("DB_SOURCE should be psql or json")

    cc = ConsoleControl(todo_list)
    cc.print_menu()
