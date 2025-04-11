from src.services.console_control import ConsoleControl
from src.services.fastapi_control import FastApiControl
from src.services.todolist_psql.todolist_psql import ToDoListPsql
from src.services.todolist_json.todolist_json import ToDoListJson
from src.dependencies import todolist as deps
from src.config.app_settings import app_settings


if __name__ == "__main__":
    match app_settings.db_source:
        case "psql":
            db = ToDoListPsql()
        case "json":
            db = ToDoListJson()
        case _:
            raise ValueError("DB_SOURCE should be psql or json")

    match app_settings.app_api:
        case "fastapi":
            control = FastApiControl(db)
        case "console":
            control = ConsoleControl(db)
        case _:
            raise ValueError("API should be fastapi or console")

    deps.todo_list = db
    control.run()
