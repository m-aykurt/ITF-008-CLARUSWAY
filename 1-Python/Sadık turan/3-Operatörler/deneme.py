# -*- coding: utf-8 -*-
"""
a,b,c = 2,5,10


# sayi1 = int(input("sayi 1 : "))
# sayi2 = int(input("sayi 2 : "))

# sonuc = ((sayi1 * sayi2) - (a+b+c))
sonuc = c // b
sonuc = (a+b+c) % 3
sonuc = b**a

sayilar = 1,5,7,10,3

a,*b,c = 1,5,7,10,3

print(a,b,c)
"""
"""
sayi1 = int(input("sayi 1 giriniz: ")) 
#sayi2 = int(input("sayi 2 giriniz: ")) 

# sonuc = (sayi1) % 2
sonuc = (sayi1) > 0


#print(f"{sayi1} , {sayi2} den büyüktür : {sonuc}")

print(sonuc)
"""
"""
vize1 = int(input("vize 1 giriniz: "))
vize2 = int(input("vize 2 giriniz: "))
final = int(input("final giriniz: "))

ortalama = (((vize1 + vize2)/2)*0.6) + final*0.4

sonuc = (ortalama >= 50)

print(f"{ortalama} ile  başarılı oldunuz {sonuc}")

"""
email = input("e mail giriniz: ")
parola = input("parola giriniz: ")

mail = "info@sadikturan.com"
password = 12345

sonuc1 = (email == mail)
sonuc2 = (parola == password)

print(f"mail adresi {sonuc1}, parolası {sonuc2}")

