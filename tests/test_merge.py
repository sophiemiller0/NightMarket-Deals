from datetime import datetime, timedelta
from src.models import Deal
from src.merge import merge_deals


def test_merge_deals_dedup_and_sort():
    base = datetime(2025, 4, 21, 20, 3, 11)
    deals = [
        Deal(id="1", title="烤串拼盘", price=28.0, source="stall_a", created_at=base),
        Deal(id="2", title="烤串拼盘", price=28.0, source="stall_a", created_at=base + timedelta(minutes=2)),
        Deal(id="3", title="冰粉", price=6.5, source="stall_b", created_at=base + timedelta(minutes=10)),
    ]
    merged = merge_deals(deals)
    assert len(merged) == 2
    assert merged[0].title == "冰粉"
