# Output Template

Always use this structure:

```markdown
共 {{count}} 个币安 USDT 永续合约当前资金费低于 {{threshold_pct}}%，已按资金费从小到大排列。

| 排名 | 交易对 | 当前资金费 | 相对上次 | 上次资金费 | 结算周期 | 下一次结算倒计时 |
|---:|---|---:|:---:|---:|---:|---:|
| 1 | {{symbol}} | {{current_rate_formatted}} | {{arrow}} | {{previous_rate_formatted}} | {{interval_formatted}} | {{countdown}} |
```

## Arrow rules
- `↑` current > previous
- `↓` current < previous
- `→` current == previous
- `—` previous missing

## Funding rate formatting
- normal: `-0.1234%`
- <= -1%: `**-1.2345%**`
- <= -2%: `<span style="color:#d92d20"><strong>-2.3456%</strong></span>`

## Interval formatting
- normal: `8h`
- 1-hour cycle: `<span style="color:#d92d20"><strong>1h</strong></span>`

## Countdown formatting
- under 1 day: `HH:MM:SS`
- 1 day or more: `Xd HH:MM:SS`
