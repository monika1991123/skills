# Binance API Mapping

Use only Binance USDⓈ-M Futures market data.

## Symbol universe
Use exchange information to keep only:
- `quoteAsset == "USDT"`
- `contractType == "PERPETUAL"`
- `status == "TRADING"`

Official docs page:
- `https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information`

Live endpoint path:
- `GET /fapi/v1/exchangeInfo`

## Current funding snapshot
Official docs page:
- `https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price`

Live endpoint path:
- `GET /fapi/v1/premiumIndex`

Fields used:
- `symbol`
- `lastFundingRate`
- `nextFundingTime`

## Previous settled funding
Official docs page:
- `https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History`

Live endpoint path:
- `GET /fapi/v1/fundingRate`

Practical use:
- query the latest settled funding record for each filtered symbol
- compare that settled value with the current `lastFundingRate`

## Funding interval adjustments
Official docs page:
- `https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info`

Live endpoint path:
- `GET /fapi/v1/fundingInfo`

Fields used:
- `symbol`
- `fundingIntervalHours`

Important note:
- this endpoint only returns symbols whose funding cap, floor, or interval was adjusted
- default any missing symbol to `8h`

## Default threshold
Default display threshold for this skill:
- current funding rate `< 0.5%`

## Recommended normalized row schema
Use this structure when building a local snapshot before rendering:

```json
[
  {
    "symbol": "BTCUSDT",
    "current_rate": -0.0009,
    "previous_rate": -0.0007,
    "interval_hours": 8,
    "next_funding_time": 1773379200000
  }
]
```
