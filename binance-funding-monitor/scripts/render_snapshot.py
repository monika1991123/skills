#!/usr/bin/env python3
"""Render a normalized Binance funding snapshot into a markdown table.

Input schema:
[
  {
    "symbol": "BTCUSDT",
    "current_rate": -0.0009,
    "previous_rate": -0.0007,
    "interval_hours": 8,
    "next_funding_time": 1773379200000
  }
]

Use this script when live endpoint payloads have already been normalized into rows.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

RED_HTML = '<span style="color:#d92d20"><strong>{}</strong></span>'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Binance funding monitor markdown from normalized JSON rows.")
    parser.add_argument("snapshot", type=Path, help="Path to normalized snapshot JSON file.")
    parser.add_argument("--threshold-pct", type=float, default=0.5, help="Keep rows whose current funding rate is strictly lower than this percent. Default: 0.5")
    parser.add_argument("--now-ms", type=int, default=None, help="Current timestamp in milliseconds. Defaults to local system time.")
    return parser.parse_args()


def load_rows(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Snapshot JSON must be a list of row objects.")
    rows: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each row must be an object.")
        symbol = str(item["symbol"])
        current_rate = float(item["current_rate"])
        previous_raw = item.get("previous_rate")
        previous_rate = None if previous_raw is None else float(previous_raw)
        interval_hours = int(item.get("interval_hours", 8))
        next_funding_time = int(item["next_funding_time"])
        rows.append(
            {
                "symbol": symbol,
                "current_rate": current_rate,
                "previous_rate": previous_rate,
                "interval_hours": interval_hours,
                "next_funding_time": next_funding_time,
            }
        )
    return rows


def format_pct(rate_decimal: float | None) -> str:
    if rate_decimal is None:
        return "—"
    pct = rate_decimal * 100.0
    base = f"{pct:.4f}%"
    if rate_decimal <= -0.02:
        return RED_HTML.format(base)
    if rate_decimal <= -0.01:
        return f"**{base}**"
    return base


def format_cycle(hours: int) -> str:
    text = f"{hours}h"
    if hours == 1:
        return RED_HTML.format(text)
    return text


def format_countdown(target_ms: int, now_ms: int) -> str:
    remaining = max(0, target_ms - now_ms)
    total_seconds = remaining // 1000
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    if days:
        return f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def arrow(current_rate: float, previous_rate: float | None) -> str:
    if previous_rate is None:
        return "—"
    if current_rate > previous_rate:
        return "↑"
    if current_rate < previous_rate:
        return "↓"
    return "→"


def render(rows: list[dict[str, Any]], threshold_pct: float, now_ms: int) -> str:
    threshold_decimal = threshold_pct / 100.0
    filtered = [row for row in rows if row["current_rate"] < threshold_decimal]
    filtered.sort(key=lambda row: row["current_rate"])

    if not filtered:
        return f"当前没有币安 USDT 永续合约的资金费低于 {threshold_pct:.4f}%。"

    lines = [
        f"共 {len(filtered)} 个币安 USDT 永续合约当前资金费低于 {threshold_pct:.4f}%，已按资金费从小到大排列。",
        "",
        "| 排名 | 交易对 | 当前资金费 | 相对上次 | 上次资金费 | 结算周期 | 下一次结算倒计时 |",
        "|---:|---|---:|:---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(filtered, start=1):
        lines.append(
            "| {rank} | {symbol} | {current} | {trend} | {previous} | {cycle} | {countdown} |".format(
                rank=idx,
                symbol=row["symbol"],
                current=format_pct(row["current_rate"]),
                trend=arrow(row["current_rate"], row["previous_rate"]),
                previous=format_pct(row["previous_rate"]),
                cycle=format_cycle(row["interval_hours"]),
                countdown=format_countdown(row["next_funding_time"], now_ms),
            )
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    rows = load_rows(args.snapshot)
    now_ms = args.now_ms if args.now_ms is not None else int(time.time() * 1000)
    output = render(rows, args.threshold_pct, now_ms)
    sys.stdout.write(output)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
