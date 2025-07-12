#!/usr/bin/env python3
import csv
from datetime import datetime, timedelta
from pathlib import Path
from src.models import Deal
from src.merge import merge_deals
from scripts.filter import filter_deals

def mock_source() -> list[Deal]:
    base = datetime(2025, 4, 21, 19, 12, 7)
    return [
        Deal(id="mkt1", title="烤串拼盘", price=28.0, source="stall_a", created_at=base, location="望京夜市"),
        Deal(id="mkt2", title="烤串拼盘", price=28.0, source="stall_a", created_at=base + timedelta(minutes=5)),
        Deal(id="mkt3", title="冰粉", price=6.5, source="stall_b", created_at=base + timedelta(minutes=17)),
    ]

def export_csv(deals, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "price", "source", "created_at", "location"])
        for d in deals:
            writer.writerow([d.id, d.title, f"{d.price:.2f}", d.source, d.created_at.isoformat(), d.location or '' ])

def main():
    deals = merge_deals(mock_source())
    # 简单过滤示例：只保留价格 >= 10 的记录
    deals = filter_deals(deals, min_price=10)
    export_csv(deals, Path('data/deals.csv'))
    print(f'exported {len(deals)} deals -> data/deals.csv')

if __name__ == '__main__':
    main()
