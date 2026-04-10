---
name: binance-readonly
description: Use installed Binance tooling for read-only market/account research. Activate when the user asks for Binance prices, klines, order book, balances, open orders, or account checks. Never place/cancel orders unless the user explicitly asks to enable trading later.
---

# Binance Read-Only

Use this skill for Binance market research and future read-only account inspection.

## Current safety posture

- `binance-mcp-server` is installed on the host.
- Do **not** assume API keys are configured.
- Treat this skill as **read-only** by default.
- Do **not** place orders, cancel orders, or enable trading unless the user explicitly asks for a separate trading setup.

## What this skill is for

- Price checks
- Order book snapshots
- Kline/candlestick research
- 24h ticker stats
- Future read-only balance / open order inspection once API keys are provided

## Installed package

- Global npm package: `binance-mcp-server`

## Safe operating rules

1. Prefer public market data tasks first.
2. If account data is needed, confirm that read-only Binance API credentials have been configured.
3. Refuse to use trading actions under this skill.
4. If the user later asks for live trading, require a separate confirmation and separate risk controls.

## Notes for future setup

Expected env vars for account access:

- `BINANCE_API_KEY`
- `BINANCE_API_SECRET`
- `BINANCE_TESTNET`

Recommended default for testing: `BINANCE_TESTNET=true`

Recommended production posture for later:

- Read-only API key first
- IP allowlist if Binance account supports it
- Separate key for trading if ever enabled
- Small explicit symbol whitelist
- Hard position/risk caps documented before any trading enablement
