#!/usr/bin/env python3
from __future__ import annotations
from typing import Iterable
from difflib import SequenceMatcher
from src.models import Deal


def is_similar(a: str, b: str, threshold: float = 0.82) -> bool:
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio() >= threshold


def fuzzy_dedupe(deals: Iterable[Deal], *, threshold: float = 0.86) -> list[Deal]:
    result: list[Deal] = []
    for d in deals:
        if any(is_similar(d.title, x.title, threshold=threshold) and abs(d.price - x.price) < 0.01 for x in result):
            continue
        result.append(d)
    return result

