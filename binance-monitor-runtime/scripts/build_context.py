#!/usr/bin/env python3
"""
币安监控上下文构建脚本
- 获取市场数据
- 生成分析报告
- 输出到 stdout 供 LLM 使用
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

def run_fetch():
    """运行数据获取脚本"""
    script = Path(__file__).parent / "binance_multi_fetch.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout, result.stderr

def run_analyze():
    """运行分析脚本"""
    script = Path(__file__).parent / "multi_analyzer.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return None
    return None

def format_report(data):
    """格式化分析报告为中文"""
    if not data or "symbols" not in data:
        return "❌ 分析数据获取失败"
    
    lines = []
    lines.append("📊 **币安市场监控分析报告**")
    lines.append(f"⏰ 生成时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    lines.append("")
    
    # 监控概览
    total = len(data.get("symbols", {}))
    lines.append(f"📈 **监控概览**: 监控 {total} 个币种")
    lines.append("")
    
    # 排名列表
    lines.append("🏆 **综合评分排名**:")
    for item in data.get("ranking", [])[:5]:
        sym = item["symbol"]
        score = item["score"]
        change = item["change_24h"]
        price = item["price"]
        emoji = "🟢" if change > 0 else "🔴" if change < 0 else "⚪"
        lines.append(f"  {item['rank']}. {sym}: ${price:.4f} | 24h: {emoji}{change:+.2f}% | 评分: {score:.1f}")
    
    lines.append("")
    
    # 异常检测
    anomalies = []
    for sym, info in data.get("symbols", {}).items():
        change = info.get("change_24h_pct", 0)
        score = info.get("composite_score", 50)
        if abs(change) > 5 or score > 60 or score < 40:
            anomalies.append((sym, change, score, info.get("price", 0)))
    
    if anomalies:
        lines.append(f"⚠️ **异常监控**: 发现 {len(anomalies)} 个异常币种")
        for sym, change, score, price in sorted(anomalies, key=lambda x: abs(x[1]), reverse=True):
            emoji = "🚀" if change > 5 else "📉" if change < -5 else "⚡"
            lines.append(f"  {emoji} {sym}: ${price:.4f} | 24h: {change:+.2f}% | 评分: {score:.1f}")
    else:
        lines.append("✅ **异常监控**: 未发现明显异常币种")
    
    lines.append("")
    
    # 详细信息
    lines.append("📋 **币种详情**:")
    for sym, info in list(data.get("symbols", {}).items())[:5]:
        lines.append(f"\n  **{sym}**:")
        lines.append(f"    💰 价格: ${info.get('price', 0):.4f}")
        lines.append(f"    📊 24h涨跌幅: {info.get('change_24h_pct', 0):+.2f}%")
        lines.append(f"    📈 4h涨跌幅: {info.get('change_4h_pct', 0):+.2f}%")
        lines.append(f"    🔒 OI: ${info.get('oi_usdt', 0):,.0f}")
        lines.append(f"    ⭐ 综合评分: {info.get('composite_score', 0):.1f}")
    
    lines.append("")
    lines.append("✅ **执行详情**: 数据采集成功")
    lines.append("📍 **当前状态**: 监控正常运行")
    
    return "\n".join(lines)

def main():
    """主函数"""
    # 获取数据
    fetch_ok, fetch_out, fetch_err = run_fetch()
    if not fetch_ok:
        print(f"数据获取失败:\n{fetch_err}", file=sys.stderr)
        return 1
    
    # 分析数据
    analysis = run_analyze()
    if not analysis:
        print("分析失败", file=sys.stderr)
        return 1
    
    # 输出报告
    report = format_report(analysis)
    print(report)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
