#!/usr/bin/env python3
"""
多币种 Binance 数据采集工具
- 并发获取 10 个币种的市场数据
- 存储为 JSONL 格式历史数据
"""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from typing import Dict, Any, Optional

# 配置
SYMBOLS = ["PEIVERSE", "EDGE", "GUA", "APR", "TRIA", "LAB", "STABLE", "MYX", "SOON", "TA"]
BINANCE_API = "https://fapi.binance.com"
TIMEOUT = 10
MAX_WORKERS = 5

def fetch_24h_ticker(symbol: str) -> Optional[Dict[str, Any]]:
    """获取 24h 行情数据"""
    try:
        url = f"{BINANCE_API}/fapi/v1/ticker/24hr?symbol={symbol}USDT"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        return {
            "symbol": symbol,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "price": float(data.get("lastPrice", 0)),
            "change_24h_pct": float(data.get("priceChangePercent", 0)),
            "volume_24h": float(data.get("quoteAssetVolume", 0)),
            "raw_24h": data
        }
    except Exception as e:
        print(f"❌ {symbol} 24h ticker 失败: {e}", file=sys.stderr)
        return None

def fetch_4h_kline(symbol: str) -> Optional[Dict[str, Any]]:
    """获取最近 4h 蜡烛数据"""
    try:
        url = f"{BINANCE_API}/fapi/v1/klines?symbol={symbol}USDT&interval=4h&limit=2"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        klines = resp.json()
        if len(klines) >= 2:
            open_price = float(klines[-2][1])
            close_price = float(klines[-1][4])
            change_4h = ((close_price - open_price) / open_price * 100) if open_price > 0 else 0
            return {
                "change_4h_pct": change_4h,
                "4h_volume": float(klines[-1][7])
            }
        return {"change_4h_pct": 0, "4h_volume": 0}
    except Exception as e:
        print(f"❌ {symbol} 4h kline 失败: {e}", file=sys.stderr)
        return None

def fetch_open_interest(symbol: str) -> Optional[Dict[str, Any]]:
    """获取未平仓合约数据"""
    try:
        url = f"{BINANCE_API}/fapi/v1/openInterest?symbol={symbol}USDT"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        oi = resp.json()
        return {
            "oi_usdt": float(oi.get("openInterest", 0)),
            "oi_symbol": oi.get("symbol", "")
        }
    except Exception as e:
        print(f"❌ {symbol} OI 失败: {e}", file=sys.stderr)
        return None

def fetch_top_trader_ratio(symbol: str) -> Optional[Dict[str, Any]]:
    """获取大户多空比"""
    try:
        # 查询账户持仓比
        url = f"{BINANCE_API}/fapi/v1/topLongShortAccountRatio?symbol={symbol}USDT&period=5m&limit=1"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        if data:
            latest = data[-1]
            long_ratio = float(latest.get("longAccount", 0))
            short_ratio = float(latest.get("shortAccount", 0))
            return {
                "whale_long_ratio": long_ratio,
                "whale_short_ratio": short_ratio,
                "whale_net": long_ratio - short_ratio
            }
        return {"whale_long_ratio": 0, "whale_short_ratio": 0, "whale_net": 0}
    except Exception as e:
        print(f"❌ {symbol} 大户比 失败: {e}", file=sys.stderr)
        return None

def fetch_symbol_data(symbol: str) -> Optional[Dict[str, Any]]:
    """并发获取一个币种的所有数据"""
    ticker = fetch_24h_ticker(symbol)
    if not ticker:
        return None
    
    kline = fetch_4h_kline(symbol)
    oi = fetch_open_interest(symbol)
    whale = fetch_top_trader_ratio(symbol)
    
    result = {**ticker}
    if kline:
        result.update(kline)
    if oi:
        result.update(oi)
    if whale:
        result.update(whale)
    
    return result

def main():
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    snapshot_file = data_dir / "multi_snapshot_latest.json"
    history_file = data_dir / "multi_snapshot_history.jsonl"
    
    print(f"🔄 开始采集 {len(SYMBOLS)} 个币种数据...")
    
    # 并发获取所有币种
    snapshot = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "symbols": {}
    }
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_symbol_data, sym): sym for sym in SYMBOLS}
        for future in as_completed(futures):
            symbol = futures[future]
            try:
                data = future.result()
                if data:
                    snapshot["symbols"][symbol] = data
                    print(f"✅ {symbol}: {data.get('price', 'N/A')} | 24h: {data.get('change_24h_pct', 0):.2f}%")
            except Exception as e:
                print(f"❌ {symbol} 采集失败: {e}", file=sys.stderr)
    
    # 保存最新快照
    snapshot_file.write_text(json.dumps(snapshot, indent=2) + "\n")
    print(f"\n✅ 最新快照已保存: {snapshot_file}")

    # 追加历史记录
    with open(history_file, 'a') as f:
        f.write(json.dumps(snapshot) + "\n")
    print(f"✅ 历史记录已追加: {history_file}")
    
    print(f"📊 本次采集成功: {len(snapshot['symbols'])}/{len(SYMBOLS)} 个币种")
    return 0 if len(snapshot['symbols']) > 0 else 1

if __name__ == "__main__":
    sys.exit(main())
