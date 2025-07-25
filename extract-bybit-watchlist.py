import requests

def get_bybit_usdt_pairs():
    url = "https://api.bybit.com/v5/market/instruments-info"
    params = {"category": "linear"}  # Perpetual derivati

    response = requests.get(url, params=params)
    data = response.json()

    if data["retCode"] != 0:
        raise Exception("Errore nella richiesta Bybit:", data)

    pairs = []
    for item in data["result"]["list"]:
        symbol = item["symbol"]
        if symbol.endswith("USDT"):
            # Aggiungi ".P" per farlo riconoscere su TradingView
            pairs.append(symbol + ".P")
    return pairs

def convert_to_tradingview_format(pairs, prefix="BYBIT"):
    return [f"{prefix}:{pair}" for pair in pairs]

def save_watchlist(tv_pairs, filename="bybit_tv_watchlist.txt"):
    with open(filename, "w") as f:
        for pair in tv_pairs:
            f.write(pair + "\n")
    print(f"✅ Watchlist generata con {len(tv_pairs)} simboli USDT (formato TradingView) in '{filename}'.")

# Esegui tutto
if __name__ == "__main__":
    pairs = get_bybit_usdt_pairs()
    tv_pairs = convert_to_tradingview_format(pairs)
    save_watchlist(tv_pairs)
