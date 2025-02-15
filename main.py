import json
import os
from uuid import uuid4


class Task:
    def __init__(self, uid, text, is_done=False):
        self._uid = uid
        self._text = text
        self._is_done = is_done

    def edit_text(self, text: str) -> None:
        """
        Редактировать текст задачи
        :param text: новый текст
        """
        self._text = text

    def mark_done(self, is_done: bool) -> None:
        """
        Изменить состояние задачи
        :param is_done: готовность задачи
        """
        self._is_done = is_done

    @property
    def uid(self) -> str:
        """
        :return: uid задачи
        """
        return self._uid

    @property
    def text(self) -> str:
        """
        :return: текст задачи
        """
        return self._text

    @property
    def is_done(self) -> bool:
        """
        :return: состояние задачи
        """
        return self._is_done

    def to_dict(self) -> dict:
        """
        Преобразовать в словарь
        :return: словарь uid, text, is_done
        """
        return {"uid": self._uid, "text": self._text, "is_done": self._is_done}

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """
        Создать задачу из словаря
        :param data: словарь
        :return: задача
        """
        return Task(data["uid"], data["text"], data["is_done"])


class ToDoList:
    def __init__(self):
        self._tasks = {}
        self._json_name = "data.json"
        self._load_json()

    def _load_json(self) -> None:
        """
        Загружает список задач из json
        """
        if os.path.exists(self._json_name):
            with open(self._json_name, "r") as file:
                data = json.load(file)
                self._tasks = {
                    uid: Task.from_dict(task_data) for uid, task_data in data.items()
                }

    def _save_json(self) -> None:
        """
        Сохраняет список задач в json
        """
        with open(self._json_name, "w") as file:
            json.dump({uid: task.to_dict() for uid, task in self._tasks.items()}, file)

    def add_task(self, text: str) -> None:
        """
        Создать новую задачу
        :param text: текст задачи
        """
        uid = str(uuid4())
        task = Task(uid, text)
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
        self._tasks[uid].edit_text(text)
        self._save_json()

    def mark_done(self, uid: str) -> None:
        """
        Пометить задачу выполненной
        :param uid: uid задачи
        """
        if uid not in self._tasks:
            raise KeyError("There is no task with this uid")
        self._tasks[uid].mark_done(True)
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
        :return: генератор uid, text, is_done
        """
        for uid, task in self._tasks.items():
            yield uid, task.text, task.is_done


class ConsoleControl:
    def __init__(self):
        self.todo = ToDoList()
        self.print_menu()

    def print_menu(self) -> None:
        """
        Вывести меню в консоль для начала работы
        """
        while True:
            try:
                command = input("Enter command: ")
                if command == "get-tasks":
                    for uid, text, is_done in self.todo.get_tasks():
                        print(f"uid: {uid}\t text: {text}\t done: {is_done}")
                elif command == "add-task":
                    text = input("text: ")
                    self.todo.add_task(text)
                elif command == "edit-task":
                    uid = input("uid: ")
                    text = input("text: ")
                    self.todo.edit_task(uid, text)
                elif command == "mark-done":
                    uid = input("uid: ")
                    self.todo.mark_done(uid)
                elif command == "delete-task":
                    uid = input("uid: ")
                    self.todo.delete_task(uid)
                elif command == "exit":
                    break
                else:
                    print("There is no such command")

            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    cc = ConsoleControl()
