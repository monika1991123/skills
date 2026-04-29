# 📈 监控摘要

**生成时间**: {{timestamp}}

## 综合状态

{{#is_healthy}}
🟢 监控正常运行
{{/is_healthy}}
{{^is_healthy}}
🟠 部分币种数据异常
{{/is_healthy}}

## 关键指标

- 采集币种: {{collected}}/{{total}} 成功
- 最新评分: {{latest_score}} 分
- 资金费率异常: {{funding_alerts}} 个

## 24h 涨跌幅分布

- 🟢 上涨 > 5%: {{up_large}} 个
- 🟡 上涨 0-5%: {{up_small}} 个
- ⚪ 持平: {{flat}} 个
- 🟠 下跌 0-5%: {{down_small}} 个
- 🔴 下跌 > 5%: {{down_large}} 个
