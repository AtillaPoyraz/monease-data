import json

def get_latest_prices():
    # Şimdilik statik, ancak mimari hazır. 
    # Buraya ileride BeautifulSoup ile web scraping eklenebilir.
    return {
        "netflix": {"standart": 229.00, "premium": 299.00},
        "spotify": {"premium": 59.90, "student": 32.90, "family": 99.90},
        "youtube premium": {"individual": 57.99, "family": 115.99},
        "disney+": {"monthly": 135.00, "yearly": 1350.00},
        "spor salonu": {"ortalama": 2000.00}
    }

if __name__ == "__main__":
    prices = get_latest_prices()
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
    print("Fiyat dosyası başarıyla oluşturuldu.")
