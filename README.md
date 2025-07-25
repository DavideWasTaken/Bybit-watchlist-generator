# Bybit USDT Watchlist Extractor

This script extracts all USDT perpetual trading pairs from Bybit and formats them for TradingView import.

## Features

- Fetches all USDT perpetual pairs from Bybit API
- Formats symbols for TradingView compatibility (adds `.P` suffix)
- Generates a watchlist file ready for import

## Requirements

```bash
pip install requests
```

## Usage

1. **Run the script:**
   ```bash
   python extract-bybit-watchlist.py
   ```

2. **The script will generate:**
   - `bybit_tv_watchlist.txt` - Contains all USDT pairs in TradingView format

## How to Import into TradingView

### Method 1: Copy & Paste (Recommended)

1. Open TradingView in your browser
2. Go to **Watchlist** panel (usually on the left sidebar)
3. Click the **+** button to create a new watchlist
4. Name it "Bybit USDT Pairs" or similar
5. Open the generated `bybit_tv_watchlist.txt` file
6. Select all content (Ctrl+A) and copy (Ctrl+C)
7. In TradingView, paste the symbols into the watchlist
8. Press **Enter** to add all symbols

### Method 2: Manual Import

1. In TradingView, go to **Watchlist** panel
2. Click the **+** button to create a new watchlist
3. Name it "Bybit USDT Pairs"
4. Open `bybit_tv_watchlist.txt` and manually add each symbol:
   - Type or paste each symbol (e.g., `BYBIT:BTCUSDT.P`)
   - Press **Enter** after each symbol
   - Repeat for all symbols

## Symbol Format

The script generates symbols in this format:
```
BYBIT:BTCUSDT.P
BYBIT:ETHUSDT.P
BYBIT:ADAUSDT.P
...
```

Where:
- `BYBIT:` - Exchange prefix for TradingView
- `BTCUSDT` - Original Bybit symbol
- `.P` - Perpetual suffix for TradingView

## Notes

- The script fetches only **USDT perpetual** pairs
- All symbols are automatically formatted for TradingView compatibility
- The generated file contains one symbol per line
- You can modify the `prefix` parameter in the script to change the exchange prefix

## Troubleshooting

If you encounter errors:
1. Check your internet connection
2. Verify that the Bybit API is accessible
3. Ensure you have the `requests` library installed
4. Check that the generated file exists and is not empty 