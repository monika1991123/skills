# 📊 币安市场监控日报

**日期**: {{date}}
**报告周期**: 24小时

## 市场概览

- 监控币种: {{total_symbols}} 个
- 正常币种: {{normal_count}} 个
- 异常币种: {{anomaly_count}} 个

## 评分排名 (Top 5)

| 排名 | 币种 | 价格 | 24h涨跌 | 评分 |
|:--:|:---:|:---:|:---:|:---:|
{{#ranking}}
| {{rank}} | {{symbol}} | ${{price}} | {{change_24h}}% | {{score}} |
{{/ranking}}

## 异常币种

{{#anomalies}}
- **{{symbol}}**: {{description}}
{{/anomalies}}

{{^anomalies}}
✅ 今日无异常币种
{{/anomalies}}

## 资金费率概况

- 负费率币种: {{negative_funding_count}} 个
- 极端负费率 (< -0.2%): {{extreme_negative_count}} 个
- 1小时结算周期: {{hourly_count}} 个

---
*数据来源: Binance USDⓈ-M Futures*
