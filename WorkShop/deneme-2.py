# -*- coding: utf-8 -*-
"""

isimler = ["ada","yigit","hasan","beril"]
yaslar = [1998,2000,1998,1987]


isimler.append("cenk")
isimler.insert(0, "sena")
isimler.remove("yigit")
sonuc = isimler.index("beril")

isimler.sort()
isimler.reverse()
yaslar.sort()
tel = ["İphone X","İphone XR"]




sonuc = min(yaslar)
sonuc = max(yaslar)
sonuc = yaslar.count(1998)
yaslar.clear()

print(yaslar)
"""
"""
arabalar = []
marka = input("araba markasını giriniz: ")
arabalar.append(marka)
marka = input("araba markasını giriniz: ")
arabalar.append(marka)
marka = input("araba markasını giriniz: ")
arabalar.append(marka)


for araba in arabalar:
    print(araba)
"""
"""
plakalar = {34:"istanbul",41:"kocaeli"}

print(type(plakalar))
print(plakalar[34])

plakalar[53] = "rize"
print(plakalar)

plakalar[35] = "izmir"
print(plakalar)

print(plakalar[35])
"""

"""
ogrenciler = {
    
     100:{
         "ad":"murat",
         "soyad":"aykurt",
         "numara":"329",
         "dogumYili":1992,
         "yas":"dogumYili",
         "meslek":"IT"
         },
        
     101:{
         "ad":"SELİN",
         "soyad":"aykurt",
         "numara":"1329",
         "dogumYili":1993,
         "yas":"dogumYili",
         "meslek":"OGRETMEN"
         }
                 }
    
print(type(ogrenciler))


print(ogrenciler[101]["meslek"])
"""
# dictionary 
""" 
urunler = {}

id = input("urun id giriniz: ")
ad = input("urun adı nedir: ")
fiyat = int(input("urun fiyatı nedir: "))

urunler[id] = {
    "ad" : ad,
    "fiyat": fiyat
    }

id = input("urun id giriniz: ")
ad = input("urun adı nedir: ")
fiyat = int(input("urun fiyatı nedir: "))

urunler[id] = {
    "ad" : ad,
    "fiyat": fiyat
    }


id = input("urun id giriniz: ")
ad = input("urun adı nedir: ")
fiyat = int(input("urun fiyatı nedir: "))

urunler[id] = {
    "ad" : ad,
    "fiyat": fiyat
    }


print(urunler)
"""
"""
opel_obj = {
    "marka" : "opel",
    "model" : "corsa",
    "yil" : 2020
    }

sonuc = opel_obj["marka"]
sonuc = opel_obj["model"]
sonuc = opel_obj["yil"]
sonuc = opel_obj.get("marka")

for x in opel_obj.values():
    print(x)
    
for x in opel_obj.items():
    print(x)

for x,y in opel_obj.items():
    print(x,y)
    
sonuc = "marka" in opel_obj
sonuc = "corsa" in opel_obj
sonuc = len(opel_obj)
opel_obj["renk"] = "kırmızı"
# sonuc = opel_obj.pop("renk")

# obj = opel_obj
obj = opel_obj.copy() 
opel_obj.update({
    "marka":"renault"
    })

"""

players = {'100': {'adı': 'ronaldo', 'dogumYili': '1985', 'takimi': 'juventys', 'ülkesi': 'portekiz', 'geçmişTakım': 'madrid'}, '102': {'adı': 'messi', 'dogumYili': '1987', 'takimi': 'barcelona', 'ülkesi': 'arjantin', 'geçmişTakım': 'barca'}}
"""
id = input("oyuncu id: ")
name = input("oyuncu adı: ")
dogumYili = input("oyuncu dogum yili: ")
takim = input("oyuncu takımı: ")
nationality = input("oyuncu ülkesi: ")
history = input("oyuncu eski takımları: ")


players.update({
    id:{
        "adı":name,
        "dogumYili":dogumYili,
        "takimi":takim,
        "ülkesi":nationality,
        "geçmişTakım":history
        
        }
    
    })

id = input("oyuncu id: ")
name = input("oyuncu adı: ")
dogumYili = input("oyuncu dogum yili: ")
takim = input("oyuncu takımı: ")
nationality = input("oyuncu ülkesi: ")
history = input("oyuncu eski takımları: ")


players.update({
    id:{
        "adı":name,
        "dogumYili":dogumYili,
        "takimi":takim,
        "ülkesi":nationality,
        "geçmişTakım":history
        
        }
    
    })
"""
"""
# id = input("id giriniz: ")
# sonuc = players.get(id)

id = input("silmek istediğiniz oyuncu bilgisi: ")
players.pop(id)

print(players)

"""
"""
aile = {}

id = input("id giriniz: ")
name = input("ad giriniz: ")
surname = input("soyadı: ")
age = int(input("yas giriniz: "))
city = input("sehir giriniz: ")
job = input("meslek nedir: ")

aile.update(
    id = {
     "ad":name,
     "soyadi":surname,
     "yas":age,
     "sehir":city,
     "meslek":job
      }
    
    ),

id = input("id giriniz: ")
name = input("ad giriniz: ")
surname = input("soyadı: ")
age = int(input("yas giriniz: "))
city = input("sehir giriniz: ")
job = input("meslek nedir: ")

aile.update(
    id = {
     "ad":name,
     "soyadi":surname,
     "yas":age,
     "sehir":city,
     "meslek":job
      }
    
    )
print(aile)
"""

age = (input("Sigara içen  ve 70 yaşının üzerinde bir insan mısınız seçiniz: True or False ").capitalize())
chronic = (input("kronik hastalığınız var mı seçiniz: True or False ").capitalize())
immune = (input("immun sisteminiz zayıf mı seçiniz: True or False ").capitalize())



risk = age or chronic or immune


print(f"ölüm riski vardır: {risk}")


"""
print("Please if it is true enter yes but if it is not leave it blank and press enter!")

age = bool(input("Are you a cigarette addict older than 75 years old?"))
chronic = bool(input("Do you have a severe chronic disease?"))
immune = bool(input("Is your immune system too weak?"))

result = age or chronic or immune

print(f"risk vardır {result}")
"""