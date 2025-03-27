from abc import ABC, abstractmethod


class IToDoList(ABC):
    """
    Интерфейс менеджера для работы с to-do листом
    """

    @abstractmethod
    def add_task(self, text: str) -> None:
        """
        Создать новую задачу
        :param text: текст задачи
        """
        pass

    @abstractmethod
    def edit_task(self, uid: str, text: str) -> None:
        """
        Редактировать текст задачи
        :param uid: uid задачи
        :param text: новый текст
        """
        pass

    @abstractmethod
    def mark_completed(self, uid: str) -> None:
        """
        Пометить задачу выполненной
        :param uid: uid задачи
        """
        pass

    @abstractmethod
    def delete_task(self, uid: str) -> None:
        """
        Удалить задачу
        :param uid: uid задачи
        """
        pass

    @abstractmethod
    def get_tasks(self):
        """
        Получить все задачи
        :return: генератор uid, text, done
        """
        pass
