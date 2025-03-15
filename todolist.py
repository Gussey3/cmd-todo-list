from uuid import UUID

from models import Task
from db import SessionLocal


class ToDoList:
    """
    Класс для работы с to-do листом
    """

    def add_task(self, text: str) -> None:
        """
        Создать новую задачу
        :param text: текст задачи
        """
        with SessionLocal() as session:
            task = Task(text=text)
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
            task.text = text
            session.commit()

    def mark_done(self, uid: str) -> None:
        """
        Пометить задачу выполненной
        :param uid: uid задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise KeyError("There is no task with this uid")
            task.done = True
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
        :return: генератор uid, text, is_done
        """
        with SessionLocal() as session:
            tasks = session.query(Task).all()

            for task in tasks:
                yield task.id, task.text, task.done
