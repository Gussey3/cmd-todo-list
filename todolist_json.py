import json
import os
from dataclasses import asdict
from uuid import uuid4

from itodolist import IToDoList
from task_json import TaskJson


class ToDoListJson(IToDoList):
    """
    Менеджер для работы с to-do листом используя JSON
    """

    def __init__(self) -> None:
        self._tasks = {}
        self._json_name = "data.json"
        self._load_json()

    def _load_json(self) -> None:
        """
        Загружает список задач из json
        """
        if os.path.exists(self._json_name):
            with open(self._json_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                self._tasks = {
                    uid: TaskJson(**task_data) for uid, task_data in data.items()
                }

    def _save_json(self) -> None:
        """
        Сохраняет список задач в json
        """
        with open(self._json_name, "w", encoding="utf-8") as file:
            json.dump(
                {uid: asdict(task) for uid, task in self._tasks.items()},
                file,
                ensure_ascii=False,
            )

    def add_task(self, text: str) -> None:
        """
        Создать новую задачу
        :param text: текст задачи
        """
        uid = str(uuid4())
        task = TaskJson(uid, text)
        self._tasks[uid] = task
        self._save_json()

    def edit_task(self, uid: str, text: str) -> None:
        """
        Редактировать текст задачи
        :param uid: uid задачи
        :param text: новый текст
        """
        if uid not in self._tasks:
            raise KeyError("There is no task with this uid")
        self._tasks[uid].text = text
        self._save_json()

    def mark_done(self, uid: str) -> None:
        """
        Пометить задачу выполненной
        :param uid: uid задачи
        """
        if uid not in self._tasks:
            raise KeyError("There is no task with this uid")
        self._tasks[uid].done = True
        self._save_json()

    def delete_task(self, uid: str) -> None:
        """
        Удалить задачу
        :param uid: uid задачи
        """
        if uid not in self._tasks:
            raise KeyError("There is no task with this uid")
        self._tasks.pop(uid)
        self._save_json()

    def get_tasks(self):
        """
        Получить все задачи
        :return: генератор uid, text, done
        """
        for uid, task in self._tasks.items():
            yield uid, task.text, task.done
