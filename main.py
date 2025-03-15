from console import ConsoleControl
from todolist import ToDoList

if __name__ == "__main__":
    cc = ConsoleControl(ToDoList())
    cc.print_menu()
