from abc import ABC, abstractmethod

from src.interfaces.idbmanager import IDBManager


class IApi(ABC):
    """
    Интерфейс взаимодействия с приложением
    """
    def __init__(self, todo_list: IDBManager) -> None:
        """
        :param todo_list: реализация IToDoList
        """
        self.todo = todo_list

    @abstractmethod
    def run(self) -> None:
        """
        Запуск приложения
        """
        pass
