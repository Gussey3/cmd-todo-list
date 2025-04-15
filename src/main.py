from src.api.console_control import ConsoleControl
from src.api.fastapi_control import FastApiControl
from src.services.psql_db_manager.psql_db_manager import PsqlDBManager
from src.services.json_db_manager.json_db_manager import JsonDBManager
from src.dependencies import todolist as deps
from src.config.app_settings import app_settings


if __name__ == "__main__":
    match app_settings.db_source:
        case "psql":
            db = PsqlDBManager()
        case "json":
            db = JsonDBManager()
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
