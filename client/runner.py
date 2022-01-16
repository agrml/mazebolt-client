from datetime import datetime

import asyncio

from client.errors import ProcessDoesNotExistError, ProcessExistsError
from client.models import TaskMeta


TASK_META: TaskMeta | None = None


async def run_process(sh_command) -> None:
    global TASK_META

    if TASK_META and TASK_META.process.returncode is None:
        raise ProcessExistsError()

    # todo: escaping
    # todo: handle exceptions
    process = await asyncio.create_subprocess_shell(sh_command)

    TASK_META = TaskMeta(
        sh_command=sh_command,
        started_at=datetime.utcnow(),
        process=process,
    )


async def stop_process() -> None:
    global TASK_META

    if not TASK_META:
        raise ProcessDoesNotExistError()

    TASK_META.process.terminate()
    TASK_META = None


async def get_task_meta_dict() -> dict:
    return TASK_META.dict() if TASK_META else {'is_running': False}
