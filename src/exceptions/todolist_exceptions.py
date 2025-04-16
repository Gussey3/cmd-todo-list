class TaskNotExistError(Exception):
    def __str__(self):
        return "Отсутствует таск с таким uid"


class ToDoListNotInitializedError(Exception):
    def __str__(self):
        return "Не инициализирован todo list"
