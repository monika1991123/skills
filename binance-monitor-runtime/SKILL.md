---
name: binance-monitor-runtime
description: Binance USDⓈ-M USDT 永续合约市场监控运行时 - 自动扫描价格、资金费、成交量异常，生成评分报告并推送 Telegram
version: 1.0.0
author: hermes-user
platforms: [linux, macos]
prerequisites:
  commands: [python3, pip]
metadata:
  hermes:
    tags: [binance, crypto, monitor, funding, alert]
---

# Binance Monitor Runtime

币安 USDⓈ-M USDT 永续合约市场监控运行时，自动检测价格异动、资金费率异常、成交量变化，生成综合评分报告并推送到 Telegram。

## 核心能力

- **多币种监控**：并发获取 10 个币种的市场数据
- **综合评分算法**：动能(25%) + 共振(25%) + 成交量(20%) + 大户(20%) + 波动(10%)
- **异常检测**：价格涨跌幅 > 5%、评分异常(>60 或 <40) 自动标记
- **资金费率监控**：检测负资金费率、1小时结算周期的极端情况
- **TG 推送**：定时报告 + 异常告警

## 架构设计

### 数据流
```
Binance API → 24h行情 + 4hK线 + OI + 大户比 → 综合评分 → 异常检测 → TG推送
                ↓
         资金费率 API → 资金费排行 → 负费率告警
```

### 监控币种
PEIVERSE, EDGE, GUA, APR, TRIA, LAB, STABLE, MYX, SOON, TA

### 评分权重
- **momentum_score**: 25% (24h + 4h 平均涨跌幅)
- **resonance_score**: 25% (OI 与价格共振)
- **volume_score**: 20% (成交量倍数)
- **whale_score**: 20% (大户多空比)
- **volatility_score**: 10% (波动率)

## 使用方式

### 1. 单次扫描测试
```bash
python3 scripts/binance_multi_fetch.py
python3 scripts/multi_analyzer.py
```

### 2. 生成完整报告
```bash
python3 scripts/build_context.py
```

### 3. 资金费率监控
```bash
python3 scripts/funding_monitor.py
```

### 4. 查看历史数据
```bash
tail -5 data/multi_snapshot_history.jsonl
```

## Cron 集成

```bash
# 每 10 分钟执行监控扫描
hermes cron create "*/10 * * * *" --skill binance-monitor-runtime \
  --script scripts/build_context.py \
  "执行币安市场监控扫描，生成评分报告，检测异常并推送 Telegram"
```

## 文件结构

```
binance-monitor-runtime/
├── SKILL.md                    # 本文件
├── scripts/
│   ├── binance_multi_fetch.py  # 多币种数据采集
│   ├── multi_analyzer.py       # 综合评分分析
│   ├── build_context.py        # Cron 上下文构建
│   ├── funding_monitor.py      # 资金费率监控
│   └── build_evolution_context.py  # 复盘上下文
└── templates/
    ├── alert_anomaly.md        # 异常告警模板
    ├── report_daily.md         # 日报模板
    └── report_summary.md       # 监控摘要模板
```

## 数据存储

### 最新快照 (data/multi_snapshot_latest.json)
```json
{
  "timestamp": "2026-04-29T02:42:50Z",
  "symbols": {
    "GUA": {
      "price": 0.8638,
      "change_24h_pct": 4.07,
      "change_4h_pct": -0.53,
      "oi_usdt": 25020291,
      "volume_24h": 1234567,
      "composite_score": 54.2
    }
  }
}
```

### 历史记录 (data/multi_snapshot_history.jsonl)
每行一条快照记录，用于趋势分析和评分计算。

### 分析报告 (data/analysis_report_latest.json)
包含最新评分排名、异常币种、综合状态。

## 环境变量

```bash
# Telegram 配置
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_CHAT_ID=6806013278

# Binance API
BINANCE_API_BASE=https://fapi.binance.com

# 监控间隔
MONITOR_INTERVAL=60
```

## 输出格式

监控报告使用中文标签 + emoji：
```
📊 **币安市场监控分析报告**
⏰ 生成时间: 2026-04-29 02:42:50 UTC

📈 **监控概览**: 监控 9 个币种

🏆 **综合评分排名**:
  1. GUA: $0.8638 | 24h: 🟢+4.07% | 评分: 54.2

⚠️ **异常监控**: 发现 1 个异常币种
  📉 TRIA: $0.0344 | 24h: -5.93% | 评分: 50.1
```

## 安全边界

1. **只读模式**：仅调用 Binance 公开 API，无交易操作
2. **超时重试**：网络请求带 10s 超时和自动重试
3. **失败降级**：单个币种失败不影响整体流程
4. **数据保留**：历史数据本地存储，支持回溯分析
