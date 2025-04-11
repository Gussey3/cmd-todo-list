from abc import ABC, abstractmethod

from src.interfaces.itodolist import IToDoList


class IApi(ABC):
    """
    Интерфейс взаимодействия с приложением
    """
    def __init__(self, todo_list: IToDoList) -> None:
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
