# -*- coding: utf-8 -*-
"""
sayi = int(input("sayi: "))

if (sayi>50):
    if (sayi<=100):
        print(f"{sayi} Sayi 50 ile 100 arasındadır")
    else:
        print(f"{sayi} 50 ile 100 arasında DEĞİLDİR")
else:
    print(f"{sayi} 50 ile 100 arasında değilgir")
  """
"""
sayi = int(input("sayi giriniz: "))      

if (sayi>0):
    if (sayi % 2 == 1):
        print(f"{sayi} pozitif ve tek sayidir.")
    else:
        print(f"{sayi} pozitif ancak Tek Sayi DEĞİLDİR")
else:
    print(f"{sayi} Pozitif ve tek sayı DEĞİLDİR")
"""
"""
username = "murataykurt"
password = "1152"

id = input("kullanıcı adı giriniz: ")
parola = (input("parola giriniz: "))

if (username == id):
    if (password == parola):
        print("uygulamaya hosgeldiniz")
    else:
        print("parola yanlıs")
else:
    print("kullanıcı adı yanlış")
"""
"""
x = int(input("sayi 1 giriniz: "))
y = int(input("sayi 2 giriniz: "))
z = int(input("sayi 3 giriniz: "))

if (x>y) and (x>z):
    print("x en buyuk degerdir")
elif (y>z) and (y>x):
    print("y en buyuk degerdir")
elif (z>y) and (z>x):
    print("z en buyuk degerdir")
else:
    print("degerler yanlıstır")
"""
"""
vize1 = int(input("vize 1 notunuz: "))
vize2 = int(input("vize 2 notunuz: "))
final = int(input("final notunuz: "))

ortalama = (((vize1+vize2)/2)*0.4) + (final*0.6)
"""
"""
if (ortalama>=50):
    print(f" ortalamanız {ortalama} ve sınıfı gectiniz. ")
else:
    print(f" ortalamanız {ortalama} ve sınıfta KALDINIZ")
"""
"""
if (ortalama>=50):
    if (final>=50):
        print(f"ortalamanız {ortalama} ve sınıfı gectiniz")
    else:
        print(f"ortamalanız {ortalama}, ancak final notunuz yetersiz")
else:
    print(f"ortalamanız {ortalama} ve sınıfta kaldınız")
"""
"""
if (ortalama>=50) or (final>=70):
    print(f"{ortalama} sınıfı gectiniz")
else:
    print(f"{ortalama} sınıfta kaldınız")
"""
"""
kilo = float(input("kilonuz: "))
boy = float(input("boyunuz metre cinsinden: "))

kiloEndeks = kilo / (boy**2)

if (0<kiloEndeks<18.5):
    print(f"kilo endeksin: {kiloEndeks} ve kilo değerlendirmen ZAYIF")
elif (18.5<kiloEndeks<25):
    print(f"kilo endeksin: {kiloEndeks} ve kilo değerlendirmen NORMAL") 
elif (25<kiloEndeks<30):
    print(f"kilo endeksin: {kiloEndeks} ve kilo değerlendirmen KİLOLU")
elif (30<kiloEndeks<34.9):
    print(f"kilo endeksin: {kiloEndeks} ve kilo değerlendirmen OBEZ")
else:
    print(f"{kiloEndeks} degerleriniz yanlış")
"""
benzin = 7
dizel = 6.2

yakit100Km = float(input("aracınızın 100 km de yaktığı yakıt litresi: "))
kacKmYol= int(input("kac km yol gittiniz: "))
yakitTuru = (input("aracın yakit turu nedir: "))
formul = (yakit100Km / 100) * kacKmYol

if (yakitTuru == benzin):
    print(formul * benzin)
elif (yakitTuru == dizel):
    print(formul * dizel)
else:
    print("girdiğiniz yakıt tipi yanlış")





