import datetime
from asyncio.subprocess import Process

from pydantic import BaseModel


class TaskParams(BaseModel):
    sh_command: str


class TaskMeta(BaseModel):
    sh_command: str
    started_at: datetime.datetime
    process: Process

    def dict(self, *args, **kwargs):
        # review: if you know any better way to customize pydantic serialization – TELL ME!
        data = super().dict(*args, exclude={'process'}, **kwargs)
        data['is_running'] = self.process.returncode is None
        return data

    class Config:
        arbitrary_types_allowed = True
