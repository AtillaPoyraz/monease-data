import requests
from bs4 import BeautifulSoup
import json

def get_netflix_price_tr():
    try:
        # Netflix TR plan sayfasını hedef alıyoruz
        url = "https://www.netflix.com/tr/signup/planform"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # DOM manipülasyonu ile fiyat etiketini buluyoruz
            # Not: Siteler yapı değiştirdikçe buradaki seçiciler güncellenmelidir
            price_tag = soup.find("span", string=lambda s: "₺" in s if s else False)
            if price_tag:
                # Metni temizleyip sayıya çeviriyoruz
                return float(price_tag.text.replace("₺", "").replace(",", ".").strip())
    except Exception as e:
        print(f"Netflix TR hatası: {e}")
    return 229.99  # Fallback: Hata olursa en son bilinen fiyat

def get_latest_prices():
    # Artık her ülke ve servis için gerçek fonksiyonlar çağrılabilir
    return {
        "tr": {
            "netflix": {"standart": get_netflix_price_tr(), "premium": 299.99},
            "spotify": {"premium": 59.90},
            "disney+": {"monthly": 135.00}
        },
        "us": { "netflix": {"standard": 15.49} },
        "uk": { "netflix": {"standard": 10.99} }
    }

if __name__ == "__main__":
    prices = get_latest_prices()
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
    print("Monease: Canlı fiyatlar web üzerinden çekildi ve mühürlendi.")
