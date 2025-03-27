from dataclasses import dataclass


@dataclass
class TaskJson:
    uid: str
    description: str
    is_completed: bool = False
