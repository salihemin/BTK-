def kontrol(kullanici , sifre):
    if kullanici == "admin" and sifre == "123456":
        return True
    else:
        return False
kullanici=input("kullanici adınız:")
sifre=input("şifreniz")
sonuc=kontrol(kullanici,sifre)
if sonuc==True:
    print("dogru girniz")
else:
    print("kullanici adı veya sifre yanlıs")










# def cevrehesaplama(a,b):
#     return a+b
# a=int(input("uzun kenar"))
# b=int(input("kısa kenar"))
# print("dörtgenin çevresi",cevrehesaplama(a,b)*2)
# def alan(a,b):
#     return a*b
# print("dörtegnin alanı", alan(a,b))







# def toplama(a,b,c,d):
#     return a+b+c+d
# a=toplama(3,4,5,6)
# print(a/4)







#  def selamla(isim):    print("selamlaaaar" ,isim)
# isim=input("isminiz")
# selamla(isim)








# def selamla():
#     print("hoşgeldin")
# def ortalama(a,b):
#     print((a+b)/2)
# selamla()
# ortalama(3,5)
# ortalama(50,12)
# sayi1=int(input("1.sayıyı giriniz"))
# sayi2=int(input("2.sayıyı giriniz"))
# ortalama(sayi1,sayi2)