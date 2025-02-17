from todolist import ToDoList


class ConsoleControl:
    def __init__(self):
        self.todo = ToDoList()

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
