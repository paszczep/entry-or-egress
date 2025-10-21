from typing import Literal
from pathlib import Path
from os import environ
from functools import wraps
from databases import Database
from dataclasses import dataclass

@dataclass
class Postgres:
    user: str
    password: str
    host: str
    port: str
    database: str

    @staticmethod
    def _environment() -> dict:
        """Zaczytaj zmienne środowiskowe."""
        return {
            key.split("_")[1]: value
            for key, value in environ.items()
            if key.startswith("postgres")
        }

    @classmethod
    def get(cls) -> "Postgres":
        return cls(**cls._environment())
    
    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Query:
    """Kwerendowanie."""
    
    def __init__(
        self, object: Literal["select", "insert"]
    ) -> "Query":
        """Zaczytaj kwerendę."""
        file = Path(f"app/query/{object}.sql")
        self._query: str = file.read_text()
        

    def arguments(self, **kwargs: dict[str, str]) -> "str":
        """Uzupełnij kwerendę o argumenty."""
        for placeholder, value in kwargs.items():
            self._query = self._query.replace(f":{placeholder}", str(value))
        return self._query


def with_db(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        opened = False
        if not db.is_connected:
            await db.connect()
            opened = True
        try:
            return await func(*args, **kwargs)
        finally:
            if opened:                 
                await db.disconnect()
    return wrapper


db = Database(Postgres.get().url, min_size=0, max_size=5)
