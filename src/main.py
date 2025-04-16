from src.api.console_control import ConsoleControl
from src.api.fastapi_control import FastApiControl
from src.services.psql_todolist_manager.psql_todolist_manager import PsqlToDoListManager
from src.services.json_todolist_manager.json_todolist_manager import JsonToDoListManager
from src.dependencies import todolist as deps
from src.config.app_settings import app_settings


if __name__ == "__main__":
    match app_settings.db_source:
        case "psql":
            manager = PsqlToDoListManager()
        case "json":
            manager = JsonToDoListManager()
        case _:
            raise ValueError("DB_SOURCE should be psql or json")

    match app_settings.app_api:
        case "fastapi":
            control = FastApiControl(manager)
        case "console":
            control = ConsoleControl(manager)
        case _:
            raise ValueError("API should be fastapi or console")

    deps.todo_list = manager

    control.run()
