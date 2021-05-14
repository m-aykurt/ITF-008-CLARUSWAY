# -*- coding: utf"-8 -*-

"""
sehirler = ["istanbul","eskişehir"]
plakalar = [34,26]

print(plakalar[0],sehirler[0])
print(plakalar[1],sehirler[1])


print(plakalar[sehirler.index("eskişehir")])
print(plakalar[sehirler.index("istanbul")])
"""
"""
sehirler = ["istanbul","eskişehir"]
plakalar = [34,26]


plakalar = {"istanbul": 34,"eskişehir": 26}


plakalar["rize"] = 53
plakalar["izmir"] = 35



print(plakalar["rize"])

"""


ogrenciler = {
    100 : {
        "ad":"selin",
        "soyad":"aykurt",
        "yas":28,
        "meslek":"ogretmen",
        "notlar":[100,90,60]
        },
    
    101 : {
        "ad":"murat",
        "soyad":"aykurt",
        "yas":29,
        "meslek":"IT",
         "notlar":[100,90,60]
        }
    }
sonuc = ogrenciler[100]["notlar"]

print(sonuc)
