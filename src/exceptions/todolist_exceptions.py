class TaskExistException(Exception):
    def __str__(self):
        return f"Отстутствует таск с таким uid"