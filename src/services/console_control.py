from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import UUID

from src.interfaces.iapi import IApi

if TYPE_CHECKING:
    from src.interfaces.itodolist import IToDoList


class ConsoleControl(IApi):
    """
    Менеджер для управления приложением через консоль
    """

    def __init__(self, todo_list: IToDoList) -> None:
        """
        :param todo_list: реализация IToDoList
        """
        super().__init__(todo_list)

    def run(self) -> None:
        """
        Запуск приложения
        """
        self.print_menu()

    def print_menu(self) -> None:
        """
        Вывести меню в консоль для начала работы
        """
        while True:
            try:
                command = input("Введите команду: ")
                if command == "get-tasks":
                    for uid, description, is_completed in self.todo.get_tasks():
                        print(f"uid: {uid}\t description: {description}\t is_completed: {is_completed}")
                elif command == "add-task":
                    text = input("text: ")
                    self.todo.add_task(text)
                elif command == "edit-task":
                    uid = UUID(input("uid: "))
                    text = input("text: ")
                    self.todo.edit_task(uid, text)
                elif command == "mark-done":
                    uid = UUID(input("uid: "))
                    self.todo.mark_completed(uid)
                elif command == "delete-task":
                    uid = UUID(input("uid: "))
                    self.todo.delete_task(uid)
                elif command == "exit":
                    break
                else:
                    print("Нет такой команды")

            except Exception as e:
                print(f"Ошибка: {e}")
