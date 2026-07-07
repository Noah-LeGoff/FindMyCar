from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class User:
    id: Optional[int]
    telegram_id: int
    username: Optional[str]
    first_name: str
    created_at: Optional[datetime] = None