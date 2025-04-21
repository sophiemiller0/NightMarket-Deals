from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Deal:
    id: str
    title: str
    price: float
    source: str
    created_at: datetime
    location: Optional[str] = None
