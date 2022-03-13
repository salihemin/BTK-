tuttugumsayi = 3
while True :
    sayi = int(input("sayı tahmin edin"))

    if sayi==tuttugumsayi:
        print("aferin")
        break
    elif sayi < tuttugumsayi:

        print("daha büyük bir sayı tahmin et")
    elif sayi > tuttugumsayi:
        print("daha küçük bir sayı tahmin et")
