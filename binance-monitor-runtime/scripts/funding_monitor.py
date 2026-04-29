#!/usr/bin/env python3
"""
Binance 资金费率监控
- 获取所有 USDT 永续合约资金费率
- 检测负资金费率排行
- 检测 1 小时结算周期的币种
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import requests

BINANCE_API = "https://fapi.binance.com"
TIMEOUT = 10

def fetch_funding_rates() -> List[Dict]:
    """获取所有币种资金费率"""
    try:
        url = f"{BINANCE_API}/fapi/v1/premiumIndex"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        
        # 只保留 USDT 永续合约
        return [
            {
                "symbol": d["symbol"],
                "markPrice": float(d.get("markPrice", 0)),
                "lastFundingRate": float(d.get("lastFundingRate", 0)),
                "nextFundingTime": d.get("nextFundingTime", 0),
            }
            for d in data
            if d["symbol"].endswith("USDT") and "_" not in d["symbol"]
        ]
    except Exception as e:
        print(f"❌ 资金费率获取失败: {e}", file=sys.stderr)
        return []

def fetch_funding_intervals() -> Dict[str, int]:
    """获取资金费率结算周期"""
    try:
        url = f"{BINANCE_API}/fapi/v1/fundingInfo"
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        return {
            d["symbol"]: d.get("fundingIntervalHours", 8)
            for d in data if d["symbol"].endswith("USDT")
        }
    except Exception as e:
        print(f"❌ 结算周期获取失败: {e}", file=sys.stderr)
        return {}

def format_countdown(ms: int) -> str:
    """格式化倒计时"""
    if ms <= 0:
        return "00:00:00"
    
    seconds = ms // 1000
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if days > 0:
        return f"{days}d {hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def main():
    """主函数"""
    print("🔄 获取资金费率数据...")
    
    funding_data = fetch_funding_rates()
    intervals = fetch_funding_intervals()
    
    if not funding_data:
        print("❌ 无数据", file=sys.stderr)
        return 1
    
    # 添加结算周期
    for item in funding_data:
        item["fundingIntervalHours"] = intervals.get(item["symbol"], 8)
    
    # 按资金费率排序（负到正）
    sorted_data = sorted(funding_data, key=lambda x: x["lastFundingRate"])
    
    now = datetime.utcnow()
    
    # 生成报告
    lines = []
    lines.append("💰 **币安资金费率监控报告**")
    lines.append(f"⏰ 生成时间: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC")
    lines.append("")
    
    # 极端负费率告警
    extreme_negative = [d for d in sorted_data if d["lastFundingRate"] <= -0.0002]
    if extreme_negative:
        lines.append(f"🔴 **极端负费率** ({len(extreme_negative)} 个):")
        for item in extreme_negative[:5]:
            rate_pct = item["lastFundingRate"] * 100
            symbol = item["symbol"].replace("USDT", "")
            lines.append(f"  📉 {symbol}: **{rate_pct:.4f}%**")
        lines.append("")
    
    # 1小时结算周期
    hourly = [d for d in sorted_data if d.get("fundingIntervalHours") == 1]
    if hourly:
        lines.append(f"⏱️ **1小时结算周期** ({len(hourly)} 个):")
        for item in hourly[:5]:
            rate_pct = item["lastFundingRate"] * 100
            symbol = item["symbol"].replace("USDT", "")
            lines.append(f"  ⚡ {symbol}: {rate_pct:.4f}%")
        lines.append("")
    
    # 负费率排行
    negative = [d for d in sorted_data if d["lastFundingRate"] < 0]
    if negative:
        lines.append(f"📉 **负资金费率排行** (共 {len(negative)} 个):")
        for i, item in enumerate(negative[:10], 1):
            rate_pct = item["lastFundingRate"] * 100
            symbol = item["symbol"].replace("USDT", "")
            countdown = format_countdown(item["nextFundingTime"] - int(time.time() * 1000))
            cycle = item.get("fundingIntervalHours", 8)
            
            # 标记极端负费率
            marker = "🔴" if rate_pct <= -0.2 else "🟠" if rate_pct <= -0.1 else "🟡"
            lines.append(f"  {i}. {marker} {symbol}: **{rate_pct:.4f}%** | 周期: {cycle}h | 下次: {countdown}")
    else:
        lines.append("✅ 当前无负资金费率币种")
    
    lines.append("")
    
    # 正费率最高
    positive = [d for d in sorted_data if d["lastFundingRate"] > 0]
    if positive:
        top_positive = sorted(positive, key=lambda x: x["lastFundingRate"], reverse=True)[:5]
        lines.append("📈 **正费率最高** (Top 5):")
        for i, item in enumerate(top_positive, 1):
            rate_pct = item["lastFundingRate"] * 100
            symbol = item["symbol"].replace("USDT", "")
            lines.append(f"  {i}. 🟢 {symbol}: +{rate_pct:.4f}%")
        lines.append("")
    
    lines.append(f"📊 **总监控**: {len(funding_data)} 个 USDT 永续合约")
    lines.append("✅ **数据来源**: Binance USDⓈ-M Futures")
    
    report = "\n".join(lines)
    print(report)
    
    # 保存到文件
    data_dir = Path(__file__).parent.parent.parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    funding_file = data_dir / "funding_report.txt"
    funding_file.write_text(report, encoding='utf-8')
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
