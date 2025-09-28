#!/usr/bin/env python3
import argparse
from pathlib import Path
from src.merge import merge_deals
from scripts.filter import filter_deals
from scripts.export_csv import mock_source, export_csv


def main():
    p = argparse.ArgumentParser(description="NightMarket Deals helper CLI")
    p.add_argument("--q", help="关键词过滤", default=None)
    p.add_argument("--min", type=float, help="最低价格", default=None)
    p.add_argument("--max", type=float, help="最高价格", default=None)
    p.add_argument("--out", type=Path, help="输出CSV路径", default=Path("data/deals.csv"))
    args = p.parse_args()

    deals = merge_deals(mock_source())
    deals = filter_deals(deals, q=args.q, min_price=args.min, max_price=args.max)
    export_csv(deals, args.out)
    print(f"written {len(deals)} -> {args.out}")


if __name__ == "__main__":
    main()

