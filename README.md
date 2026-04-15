# Binance Futures Testnet Trading Bot

Simplified Python trading bot for placing MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Setup

1. **Binance Testnet Account**:
   - Register at https://testnet.binancefuture.com
   - Generate API Key and Secret (with Futures trading enabled).

2. **Environment**:
   ```
   cd c:/Users/pc/Downloads/trading_bot
   pip install -r requirements.txt
   ```

## Usage

Run via CLI. Provide your Testnet API credentials each time.

### MARKET Order
```
python cli.py market BTCUSDT BUY 0.001 --api-key=YOUR_KEY --api-secret=YOUR_SECRET
```

### LIMIT Order
```
python cli.py limit BTCUSDT BUY 0.001 50000 --api-key=YOUR_KEY --api-secret=YOUR_SECRET
```

**Arguments**:
- `symbol`: e.g., BTCUSDT (validated uppercase +USDT)
- `side`: BUY or SELL
- `quantity`: positive number (e.g., 0.001)
- `price`: positive number (LIMIT only)

**Output**: Request summary, response details (orderId, status, etc.), success/fail. Logs to `trading_bot.log`.

### Example Logs
After running, check `trading_bot.log` for API requests/responses/errors.

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py      # Binance client wrapper
│   ├── orders.py      # Order logic + validation
│   ├── validators.py  # Input validation
│   └── logging_config.py
├── cli.py             # Click CLI
├── README.md
├── requirements.txt
└── TODO.md
```

## Assumptions
- Testnet only (`testnet=True`).
- No precision/min-notional checks (handle via Binance errors).
- LIMIT uses GTC timeInForce.
- Quantity/price as float (binance handles).
- Python 3.8+.

## Testing Deliverables
- Run one MARKET and one LIMIT order.
- Logs generated automatically.

All core requirements met: CLI validation, structured code, logging, error handling.

