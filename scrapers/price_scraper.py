import requests
import json
import os

# Veri yolları yeni klasör yapısına göre mühürlendi
PRICES_PATH = 'data/prices/global_prices.json'
DEALS_PATH = 'data/deals/tr.json'

def update_data():
    # 1. Mevcut fiyat çekme mantığın buraya gelecek (Mevcut kodunu koruyoruz)
    # 2. Çıktı klasörünün varlığını kontrol et
    os.makedirs(os.path.dirname(PRICES_PATH), exist_ok=True)
    
    # Örnek veri (Senin scraper'ın burayı dolduracak)
    prices_data = {
        "last_update": "2026-02-01",
        "regions": ["tr", "us", "uk"]
    }

    # Dosyayı yeni yerine kaydet
    with open(PRICES_PATH, 'w', encoding='utf-8') as f:
        json.dump(prices_data, f, indent=2, ensure_ascii=False)
    
    print(f"Başarılı: Veriler {PRICES_PATH} konumuna mühürlendi!")

if __name__ == "__main__":
    update_data()
