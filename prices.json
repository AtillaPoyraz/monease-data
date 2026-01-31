import json

def get_latest_prices():
    return {
        "tr": {
            "netflix": {"basic": 149.99, "standard": 229.99, "premium": 299.99},
            "spotify": {"student": 32.90, "premium": 59.90, "family": 99.90},
            "youtube premium": {"individual": 57.99, "family": 115.99, "student": 37.99},
            "disney+": {"monthly": 135.00, "yearly": 1350.00},
            "icloud+": {"50gb": 12.99, "200gb": 39.99, "2tb": 129.99}
        },
        "us": {
            "netflix": {"standard_ads": 6.99, "standard": 15.49, "premium": 22.99},
            "spotify": {"student": 5.99, "premium": 11.99, "family": 19.99},
            "youtube premium": {"individual": 13.99, "family": 22.99},
            "icloud+": {"50gb": 0.99, "200gb": 2.99, "2tb": 9.99}
        },
        "uk": {
            "netflix": {"standard_ads": 4.99, "standard": 10.99, "premium": 17.99},
            "spotify": {"student": 5.99, "premium": 11.99, "family": 19.99},
            "youtube premium": {"individual": 12.99, "family": 19.99}
        }
    }

if __name__ == "__main__":
    prices = get_latest_prices()
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
    print("Global fiyat veritabanı başarıyla mühürlendi.")
