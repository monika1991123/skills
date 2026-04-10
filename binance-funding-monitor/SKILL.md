---
name: binance-funding-monitor
description: monitor binance usdⓈ-m usdt perpetual funding rates and present a sorted watchlist when the user asks to check funding, rank symbols below a threshold, compare the current funding rate with the previous settlement, show funding interval hours and countdown to the next settlement, or highlight extreme negative funding and 1-hour funding cycles. use for requests such as "列出币安 usdt 合约资金费小于 0.5% 的交易对", "看负资金费排行", "展示下一次资金费倒计时", or "做一个资金费监控表".
---

# Binance Funding Monitor

Use official Binance USDⓈ-M futures market data and the bundled references. Treat this skill as an on-demand monitoring workflow, not a background alerting daemon.

## Workflow

1. Collect the tradable universe.
   - Use only USDⓈ-M perpetual symbols whose `quoteAsset` is `USDT`, `contractType` is `PERPETUAL`, and `status` is `TRADING`.
   - Ignore delivery contracts and non-USDT symbols.

2. Collect the current funding snapshot.
   - Read the current funding rate from `lastFundingRate`.
   - Read the next settlement timestamp from `nextFundingTime`.

3. Collect funding interval adjustments.
   - Use `fundingIntervalHours` when Binance explicitly returns it.
   - Default to `8` hours when a symbol is absent from the interval-adjustment payload.

4. Collect the previous settled funding rate.
   - Compare the current funding rate against the latest settled funding rate for the same symbol.
   - Use arrows only: `↑` for increase, `↓` for decrease, `→` for unchanged, `—` when previous data is unavailable.

5. Filter, sort, and format.
   - Default threshold: keep symbols whose current funding rate is strictly lower than `0.5%`.
   - Sort ascending by current funding rate, from the most negative to the least negative / smallest positive.
   - Show one row per symbol.

## Required Output

Always return a compact summary line followed by a table using the column order below:

| 排名 | 交易对 | 当前资金费 | 相对上次 | 上次资金费 | 结算周期 | 下一次结算倒计时 |
|---:|---|---:|:---:|---:|---:|---:|

Formatting rules:
- Render funding rates as percentages with 4 decimal places.
- Make the current funding rate **bold** when it is less than or equal to `-1%`.
- Make the current funding rate **bold and red** when it is less than or equal to `-2%`.
- Make the settlement cycle **bold and red** when `fundingIntervalHours == 1`.
- Preserve the sort order exactly as computed.
- Show countdown as `Xd HH:MM:SS` when at least one full day remains, otherwise `HH:MM:SS`.

Use HTML styling only for the red cases:
- rate: `<span style="color:#d92d20"><strong>-2.1234%</strong></span>`
- cycle: `<span style="color:#d92d20"><strong>1h</strong></span>`

If HTML color is unavailable in the environment, keep the bold formatting and prefix the cell with `红`.

## Data Handling Rules

- Convert Binance decimal funding values to percentages by multiplying by `100` only at render time.
- Compare raw decimal funding values before formatting.
- Clamp negative countdowns to `00:00:00`.
- If a previous settled funding rate is unavailable, render `—` for both the arrow and the previous rate cell.
- If no symbol matches the threshold, say so explicitly and still mention the threshold used.

## Environment Variants

Use the best available route in this order:
1. Live official Binance API access if the environment can fetch current endpoint payloads.
2. User-provided exported JSON files that mirror the official endpoint responses.
3. A normalized snapshot file processed through `scripts/render_snapshot.py`.

Use `references/binance-api.md` for endpoint mapping and `references/output-template.md` for the exact display pattern.
