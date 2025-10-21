from dataclasses import dataclass, asdict
from enum import IntEnum
from datetime import time, datetime
from app.source.database import db, Query, with_db

class WorkerNotFound(Exception):
    pass

@dataclass
class Worker:
    """Pracownik i jego identyfikator RCP."""
    id: int
    name: str

    @classmethod
    @with_db
    async def fetch(cls, code: int) -> "Worker":
        query = Query("select").arguments(card_number=code)
        values = await db.fetch_one(query)
        if values is not None:
            return cls(**values)
        else:
            raise WorkerNotFound

NIGHT = time(0, 0)
DAY = time(12, 0)


class InOutMode(IntEnum):
    """Kod zdarzenia RCP. Po północy - wejście, po południu - wyjście."""
    entry = 0
    egress = 1

    @classmethod
    def which(cls) -> int:
        now = datetime.now()
        if NIGHT <= now.time() <= DAY:
            return cls.entry
        else:
            return cls.egress


@dataclass
class RcpLog:
    """Wiersz w tabeli 'rcp.log'."""
    worker: int
    mode: InOutMode
    date: str
    time: str
    source: int = 8
    verify: int = 0
    remark: str = "''"

    @classmethod
    def create(cls, worker: int) -> "RcpLog":
        now = datetime.now()
        return cls(
            worker=worker,
            mode=InOutMode.which(),
            date=f"'{now.date().isoformat()}'",
            time=f"'{now.time().strftime("%H:%M")}'",
        )

    @with_db
    async def write(self):
        query = Query("insert").arguments(**asdict(self))
        await db.execute(query)
