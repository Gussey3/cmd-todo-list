import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions.todolist_exceptions import TaskNotExistError
from src.interfaces.iapi import IApi
from src.interfaces.itodolistmanager import IToDoListManager
from src.api.routers.todo_router import router

app = FastAPI()
app.include_router(router)


@app.exception_handler(TaskNotExistError)
def task_not_found_handler(request: Request, exc: TaskNotExistError):
    return JSONResponse(
        status_code=404,
        content={"detail": "Не найден таск с таким uid"},
    )


class FastApiControl(IApi):
    """
    Менеджер для управления приложением через fastapi
    """

    def __init__(self, todo_list: IToDoListManager) -> None:
        """
        :param todo_list: реализация IToDoList
        """
        super().__init__(todo_list)

    def run(self) -> None:
        """
        Запуск приложения
        """
        uvicorn.run("src.api.fastapi_control:app", port=8090)
