"""
< küçüktür
> büyüktür
<= küçük eşit
>= büyük eşit
== esşitti
!= eşit deildir
"""
cinsiyet=input(" Bir harf giriniz:")


if cinsiyet=="e" or cinsiyet=="E":
    print("Cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet== "k" or cinsiyet=="K":
    print("cinsiyet olarak Kadın girdiniz")
    print("şuanda elif bloğu içinden mesaj veriyorum")
else:
    print("ben sana e ya da k gir demedim mi")
print("şuanda if dışıda")
