import uvicorn
from fastapi import FastAPI

from src.interfaces.iapi import IApi
from src.interfaces.idbmanager import IDBManager
from src.api.routers.todo_router import router

app = FastAPI()
app.include_router(router)


class FastApiControl(IApi):
    """
    Менеджер для управления приложением через fastapi
    """
    def __init__(self, todo_list: IDBManager) -> None:
        """
        :param todo_list: реализация IToDoList
        """
        super().__init__(todo_list)

    def run(self) -> None:
        """
        Запуск приложения
        """
        uvicorn.run("src.services.fastapi_control:app", port=8090)
