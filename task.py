from dataclasses import dataclass, asdict


@dataclass
class Task:
    uid: str
    text: str
    is_done: bool = False

    def edit_text(self, text: str) -> None:
        """
        Редактировать текст задачи
        :param text: новый текст
        """
        self.text = text

    def mark_done(self, is_done: bool) -> None:
        """
        Изменить состояние задачи
        :param is_done: готовность задачи
        """
        self.is_done = is_done

    def to_dict(self) -> dict:
        """
        Преобразовать в словарь
        :return: словарь uid, text, is_done
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """
        Создать задачу из словаря
        :param data: словарь
        :return: задача
        """
        return Task(**data)
