from uuid import UUID

from fastapi import APIRouter, Depends
from typing import List

from src.dependencies.todolist import get_todo_list
from src.interfaces.itodolistmanager import IToDoListManager
from src.api.schemas.task import TaskSchema, NewTaskSchema

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskSchema)
def add_task(task: NewTaskSchema, todo: IToDoListManager = Depends(get_todo_list)):
    model = todo.add_task(text=task.description)
    return TaskSchema.model_validate(model)


@router.get("", response_model=List[TaskSchema])
def get_tasks(todo: IToDoListManager = Depends(get_todo_list)):
    tasks = [
        TaskSchema(id=uid, description=description, is_completed=is_completed)
        for uid, description, is_completed in todo.get_tasks()
    ]
    return tasks


@router.put("/{task_id}")
def edit_task(
    task_id: str, task_body: NewTaskSchema, todo: IToDoListManager = Depends(get_todo_list)
):
    todo.edit_task(UUID(task_id), text=task_body.description)


@router.delete("/{task_id}")
def delete_task(task_id: str, todo: IToDoListManager = Depends(get_todo_list)):
    todo.delete_task(UUID(task_id))
