import requests
import time
ALARM_SINIRI = 46.0
print("Dolar Takip Botu Başlatıldı.. Çıkmak İçin CTRL+C apabilirsin.\n")
url = "https://open.er-api.com/v6/latest/USD"

while True:

    cevap = requests.get(url)
    veri = cevap.json()

    dolar_tl_kuru = veri['rates']['TRY']

    print("Güncel Dolar Kuru", dolar_tl_kuru)

    if dolar_tl_kuru >= ALARM_SINIRI:
        print(f"ALARM! Dolar belirlediğiniz {ALARM_SINIRI} sınırının üstünde! Anlık: {dolar_tl_kuru}")

    print("--------------------------------------------------")

    time.sleep(5)
