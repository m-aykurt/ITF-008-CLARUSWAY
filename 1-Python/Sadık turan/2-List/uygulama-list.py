# -*- coding: utf-8 -*-

liste = ["samsung s5","samsung s6","samsung s7","samsung s8"]

result = liste
result =len(liste)
result = liste[0]
result = liste[-1]

liste[0] = "samsung s9"
result = liste
"""
if "samsung s6" in liste:
    print("evet liste elemanı")
"""

result = liste[0:2]


liste[2] = "iphone x"
liste[3] = "iphone xr"

result = liste

result = liste + ["samsung 10"] + ["samsungs11"]

del liste[-1]
result = liste

result = liste[::-1]
"""

for a in liste:
    print(a)

print(result)
"""

ogrenciA = ["yigit","bilgi",2010,[72,60,80]]
ogrenciB = ["sena","turan",1999,[73,100,80]]
ogrenciC = ["ahmet","kahya",2001,[55,10,80]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]
    
for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2021-ogrenci[2]
    puan = (ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) / 3
    print(f"{ad} {soyad} {puan} {yas}")


