while True:
    kullaniciadi =input("kullanıcı adı")
    sifre=input("parolannız")
    if kullaniciadi == "admin" and sifre =="123456":
        break
    else:
        print("kullaıcı adı veya parola hatalı")
