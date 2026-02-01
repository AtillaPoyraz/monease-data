import requests
import json
import re
import os

# Çıktı yolu
OUTPUT_PATH = 'data/prices/global_prices.json'

def scrape_global(url, pattern, fallback):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=15)
        match = re.search(pattern, response.text, re.IGNORECASE | re.DOTALL)
        if match:
            return float(match.group(1).replace(",", "."))
    except:
        pass
    return fallback

def get_latest_prices():
    tr_news = "https://shiftdelete.net/en-populer-abonelik-ucretleri-2026"
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Veri Hazinesi
    prices_data = {
        "last_update": "2026-02-01",
        "tr": {
            "netflix": {
                "basic": scrape_global(tr_news, r"Netflix Temel.*?(\d+[\.,]\d+)", 149.99),
                "standard": scrape_global(tr_news, r"Netflix Standart.*?(\d+[\.,]\d+)", 229.99),
                "premium": scrape_global(tr_news, r"Netflix Özel.*?(\d+[\.,]\d+)", 299.99)
            },
            "spotify": {"student": 32.90, "individual": 59.90, "family": 99.90},
            "youtube": {"individual": 57.99, "family": 115.99, "student": 37.99},
            "disney+": {"monthly": 134.99},
            "amazon_prime": {"monthly": 39.0}
        },
        "us": {
            "netflix": {"standard": 15.49, "premium": 22.99},
            "spotify": {"individual": 11.99}
        },
        "uk": {
            "netflix": {"standard": 10.99},
            "spotify": {"individual": 11.99}
        }
    }

    # BURASI KRİTİK: Sadece regions değil, tüm prices_data'yı yazıyoruz
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(prices_data, f, indent=2, ensure_ascii=False)
    
    print(f"Monease: Fiyatlar başarıyla mühürlendi -> {OUTPUT_PATH}")

if __name__ == "__main__":
    get_latest_prices()
