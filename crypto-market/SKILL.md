---
name: crypto-market
description: Use installed crypto market tooling for general market research, trend checks, and historical price analysis. Activate when the user asks for crypto prices, market analysis, exchange comparison, or historical trends.
---

# Crypto Market Research

Use this skill for broad cryptocurrency market research that does not require exchange account access.

## Installed package

- Global npm package: `mcp-crypto-price`

## Good uses

- Spot price checks
- 24h change / volume / market cap
- Historical trend summaries
- Exchange/market analysis
- Cross-checking Binance-specific views with broader market data

## Safety posture

- No account credentials required for basic use
- Optional future env var for higher rate limits: `COINCAP_API_KEY`
- This skill is research-only and should not be treated as trade execution

## Working style

1. Use this skill when the user wants quick crypto market context.
2. Prefer concise summaries with the option to expand.
3. Cross-check with Binance-specific research when exchange-local detail matters.
4. Keep clear separation between market analysis and trade execution.
