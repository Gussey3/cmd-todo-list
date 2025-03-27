from uuid import UUID

from src.interfaces.itodolist import IToDoList
from src.models.task import Task
from src.db import SessionLocal


class ToDoListPsql(IToDoList):
    """
    Менеджер для работы с to-do листом используя postgresql
    """

    def add_task(self, text: str) -> None:
        """
        Создать новую задачу
        :param text: текст задачи
        """
        with SessionLocal() as session:
            task = Task(description=text)
            session.add(task)
            session.commit()

    def edit_task(self, uid: str, text: str) -> None:
        """
        Редактировать текст задачи
        :param uid: uid задачи
        :param text: новый текст
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise KeyError("There is no task with this uid")
            task.description = text
            session.commit()

    def mark_completed(self, uid: str) -> None:
        """
        Пометить задачу выполненной
        :param uid: uid задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise KeyError("There is no task with this uid")
            task.is_completed = True
            session.commit()

    def delete_task(self, uid: str) -> None:
        """
        Удалить задачу
        :param uid: uid задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise KeyError("There is no task with this uid")
            session.delete(task)
            session.commit()

    def get_tasks(self):
        """
        Получить все задачи
        :return: генератор uid, text, done
        """
        with SessionLocal() as session:
            tasks = session.query(Task).all()

            for task in tasks:
                yield task.id, task.description, task.is_completed
