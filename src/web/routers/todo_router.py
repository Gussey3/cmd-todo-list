from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from src.dependencies.todolist import get_todo_list
from src.interfaces.itodolist import IToDoList
from src.web.schemas.task import TaskSchema, NewTaskSchema
from src.exceptions.todolist_exceptions import TaskNotExistError

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskSchema)
def add_task(task: NewTaskSchema, todo: IToDoList = Depends(get_todo_list)):
    model = todo.add_task(text=task.description)
    return TaskSchema.model_validate(model)


@router.get("", response_model=List[TaskSchema])
def get_tasks(todo: IToDoList = Depends(get_todo_list)):
    tasks = [
        TaskSchema(id=uid, description=description, is_completed=is_completed)
        for uid, description, is_completed in todo.get_tasks()
    ]
    return tasks

@router.put("/{task_id}")
def edit_task(task_id: str, task_body: NewTaskSchema, todo: IToDoList = Depends(get_todo_list)):
    try:
        todo.edit_task(UUID(task_id), text=task_body.description)
    except TaskNotExistError:
        raise HTTPException(status_code=404, detail="task not found")


@router.delete("/{task_id}")
def delete_task(task_id: str, todo: IToDoList = Depends(get_todo_list)):
    try:
        todo.delete_task(UUID(task_id))
    except TaskNotExistError:
        raise HTTPException(status_code=404, detail="task not found")
