from pydantic import BaseModel, Field
from uuid import UUID


class TaskSchema(BaseModel):
    id: UUID = Field(title="Уникальный идентификатор задачи")
    description: str = Field(title="Описание задачи")
    is_completed: bool = Field(False, title="Флаг выполненности задачи")

    model_config = {
        "from_attributes": True
    }


class NewTaskSchema(BaseModel):
    description: str = Field(title="Описание задачи")
