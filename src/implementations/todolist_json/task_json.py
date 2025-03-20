from dataclasses import dataclass


@dataclass
class TaskJson:
    uid: str
    text: str
    done: bool = False
