#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import asdict
from typing import Iterable
from datetime import datetime
from src.models import Deal


def filter_deals(
    deals: Iterable[Deal], *,
    q: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> list[Deal]:
    out: list[Deal] = []
    for d in deals:
        if q and q.lower() not in d.title.lower():
            continue
        if min_price is not None and d.price < min_price:
            continue
        if max_price is not None and d.price > max_price:
            continue
        out.append(d)
    return out


if __name__ == "__main__":
    # 小示例，便于快速手动验证
    base = datetime(2025, 4, 21, 21, 7, 3)
    deals = [
        Deal(id="1", title="烤串拼盘", price=28.0, source="stall_a", created_at=base),
        Deal(id="2", title="冰粉", price=6.5, source="stall_b", created_at=base),
    ]
    res = filter_deals(deals, q="烤串", min_price=20)
    print([asdict(x) for x in res])

