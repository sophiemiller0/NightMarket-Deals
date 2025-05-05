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
    # 次级排序：时间降序，其次价格升序，最后标题字典序，稳定输出
    out.sort(key=lambda x: (x.created_at, -x.price, x.title.lower()), reverse=True)
    return out
