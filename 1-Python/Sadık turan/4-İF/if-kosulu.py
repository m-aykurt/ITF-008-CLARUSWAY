# -*- coding: utf-8 -*-
"""
username = "murataykurt"
password = "1152"



if (username == "murataykurt"):
    if  (password == "1152"):
        print("uygulamaya hosgeldiniz")
else:
    print("hatali giris")
  
id = input("id giriniz : ")
parola = input("parola giriniz: ")

if (username == id):
    if (password == parola):
        print("uygulamaya hosgeldiniz")
    else:
        print("sifre hatalı")
else:
    print("hatali giris")
"""

"""
x = 30
y = 30

if (x>y):
    print("x y den büyüktür")
elif (x==y):
    print("x y eşittir")
else:
    print("y x den büyüktür.")
"""  
"""

sayi = int(input("sayi : ")) 

if (sayi>0):
    print("sayi pozitif.")
elif (sayi==0):
    print("sayi sıfırdır")
else:
    print("sayi negatif")
"""
"""
x = int(input("bir sayi giriniz: "))    

if (50<x<100):
    print(f"{x} girilen sayı 50 ile 100 arasındadır")
else:
    print(f"{x} 50 ile 100 arasında değildir")
    """
"""    
x = int(input("bir sayi giriniz: "))

if x>0 and (x % 2 == 1):
    print("girilen sayı pozitif tek sayıdır")
else:
    print("girilen sayı pozitif tek sayı değildir")
"""
"""
email = input("mail adresi giriniz: ")
parola= input("parola giriniz: ")

mail = "maykurt92"
password = "1152"

if (mail == email):
    if (parola == password):
        print(f"uygulamaya hosgeldiniz")
    else:
        print("parola yanlıs")
else:
    print("mail yanlıs")
"""
"""
ad = input("isim giriniz: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

vki = kg / (hg**2)

if (0<vki<=18.4):
    print("kişi zayıf")
elif (18.5<vki<=25):
    print("kisi normal")
else:
    print("degerler yanlıs")
"""
"""
yakitTipi = input("aracınızın yakıt tipi: ")
arac100km = float(input("aracınız 100 km de kac litre yakıt harcıyor: "))
kacKmYol = float(input("kac km yol yaptınız: "))

benzin = ((arac100km * 7.2)/100) * kacKmYol
dizel = ((arac100km * 6)/100) * kacKmYol

if (yakitTipi == "benzin"):
    print(benzin)
elif (yakitTipi == "dizel"):
    print(dizel)
else:
    print("degerler yanlıs")
"""

# ehliyet sorusu
"""
isim = input("isminiz: ")
yas = int(input("yasınız: "))
egitim = input("egitim durumunuz:  ")

if (yas>=18):
    if (egitim == "lise") or (egitim == "üniversite"):
       print(f"{isim}  ehliyet almaya hak kazandınız ") 
    else:
        print("egitim seviyeniz yeterli degil veya yanlış girdiniz")
else:
    print("yasınız uygun degil")

"""
"""
import datetime


tarih = input("aracınızı hangi tarihte aldınız: ")
tarih = tarih.split("/")

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days



print(simdi)
 """

sermaye = 1000
sermaye *= 1.07
while 0<7:
    print(sermaye)




