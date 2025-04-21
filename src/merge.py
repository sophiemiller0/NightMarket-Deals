from __future__ import annotations
from datetime import datetime
from typing import Iterable, List
from .models import Deal

def merge_deals(deals: Iterable[Deal]) -> List[Deal]:
    seen = set()
    out: List[Deal] = []
    for d in deals:
        key = (d.title.lower().strip(), round(d.price, 2), d.source)
        if key in seen:
            continue
        seen.add(key)
        out.append(d)
    out.sort(key=lambda x: x.created_at, reverse=True)
    return out
