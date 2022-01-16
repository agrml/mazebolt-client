from fastapi import FastAPI, HTTPException

from client.errors import ProcessDoesNotExistError, ProcessExistsError
from client.models import TaskParams
from client.runner import (
    get_task_meta_dict,
    run_process,
    stop_process,
)

app = FastAPI()


@app.get("/task")
async def get_task():
    return await get_task_meta_dict()


@app.post("/task")
async def create_task(task_params: TaskParams):
    try:
        await run_process(task_params.sh_command)
    except ProcessExistsError:
        raise HTTPException(
            status_code=400,
            detail="There is an already running process. Terminate it first",
        )

    return await get_task_meta_dict()
    # todo: надо обработать ошибки


@app.delete("/task")
async def cancel_task():
    try:
        await stop_process()
    except ProcessDoesNotExistError:
        raise HTTPException(
            status_code=400,
            detail="there are no running tasks",
        )
    # todo: надо обработать ошибки
    return 'Success'
