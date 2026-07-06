import binascii

def xor_islem(metin, anahtar):
    sonuc = ""
    for karakter in metin:
        sonuc += chr(ord(karakter) ^ anahtar)
    return sonuc

print("====================================")
print("   🔒 XOR + HEX ŞİFRELEME ARACI 🔓   ")
print("====================================\n")

secim = input("1 - Metin Şifrele\n2 - Şifre Çöz\nSeçiminiz (1 veya 2): ")

if secim == "1":
    mesaj = input("\nŞifrelenecek mesajı girin: ")
    pin = int(input("Şifreleme anahtarı girin (1-255 arası bir sayı): "))
    
    # 1. Önce XOR ile şifreliyoruz
    ham_sifreli = xor_islem(mesaj, pin)
    
    # 2. Görünmeyen karakter hatasını engellemek için HEX formatına çeviriyoruz
    hex_sifreli = binascii.hexlify(ham_sifreli.encode('utf-8')).decode('utf-8')
    
    print(f"\n[+] Şifrelenmiş Metin (HEX): {hex_sifreli}")
    print("(!) Bu şifreyi çözmek için yukarıdaki HEX koduna ihtiyacınız var.")

elif secim == "2":
    hex_metin = input("\nÇözülecek HEX kodunu girin: ")
    pin = int(input("Şifre çözme anahtarını (PIN) girin: "))
    
    try:
        # 1. Önce HEX formatından geri çözüyoruz
        ham_sifreli = binascii.unhexlify(hex_metin.encode('utf-8')).decode('utf-8')
        # 2. Sonra XOR işlemini tersine çeviriyoruz
        cozulen = xor_islem(ham_sifreli, pin)
        print(f"\n[+] Çözme İşlemi Tamamlandı: {cozulen}")
    except Exception:
        print("\n[-] Hata: Geçersiz HEX formatı veya yanlış veri girdiniz!")

else:
    print("\n[-] Geçersiz seçim yaptınız.")
