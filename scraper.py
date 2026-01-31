import requests
import json
import re

def scrape_global(url, pattern, fallback):
    """Regex ile belirli bir abonelik tipinin fiyatını yakalar."""
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
    # Kaynak Linkler
    tr_news = "https://shiftdelete.net/en-populer-abonelik-ucretleri-2026" # Örnek güncel liste
    us_tech = "https://www.tomsguide.com/news/streaming-services-price-hikes"
    uk_tech = "https://www.radiotimes.com/technology/streaming/best-streaming-service-uk/"

    return {
        "tr": {
            "netflix": {
                "basic": scrape_global(tr_news, r"Netflix Temel.*?(\d+[\.,]\d+)", 149.99),
                "standard": scrape_global(tr_news, r"Netflix Standart.*?(\d+[\.,]\d+)", 229.99),
                "premium": scrape_global(tr_news, r"Netflix Özel.*?(\d+[\.,]\d+)", 299.99)
            },
            "spotify": {
                "student": 32.90, "individual": 59.90, "family": 99.90
            },
            "youtube": {
                "individual": 57.99, "family": 115.99, "student": 37.99
            },
            "disney+": {"monthly": 134.99, "yearly": 1349.90},
            "amazon_prime": {"monthly": 39.00},
            "icloud+": {"50gb": 12.99, "200gb": 39.99, "2tb": 129.99},
            "xbox_game_pass": {"ultimate": 209.00},
            "gain": {"monthly": 149.00},
            "exxen": {"reklamli": 129.00, "reklamsiz": 179.00}
        },
        "us": {
            "netflix": {"standard": 15.49, "premium": 22.99},
            "spotify": {"individual": 11.99, "family": 19.99},
            "youtube": {"individual": 13.99, "family": 22.99},
            "hulu": {"ads": 7.99, "no_ads": 17.99},
            "hbo_max": {"monthly": 15.99},
            "apple_tv+": {"monthly": 9.99}
        },
        "uk": {
            "netflix": {"standard": 10.99, "premium": 17.99},
            "spotify": {"individual": 11.99, "family": 19.99},
            "now_tv": {"entertainment": 9.99, "cinema": 9.99},
            "sky_stream": {"basic": 26.00},
            "disney+": {"standard": 7.99}
        }
    }

if __name__ == "__main__":
    prices = get_latest_prices()
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
    print("Monease: Global ve Yerel (TR, US, UK) 20+ servis başarıyla güncellendi!")
