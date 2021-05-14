# -*- coding: utf-8 -*-

isimler = ["ada","yigit","hasan","beril"]
yaslar = [1998,2000,1992,1987]


isimler.append("cenk")
isimler.insert(0, "sena")
# isimler.remove("yigit")

isimler.count("yigit")

sonuc = isimler.index("yigit")




if "beril" in isimler:
    print("evet liste elemanıdır")

sonuc = "beril" in isimler

print(sonuc)


isimler.sort()
isimler.reverse()

yaslar.sort()

sonuc = yaslar

"""
telefonlar = ["İphone X","İphone XR"]
sonuc = telefonlar
for telefon in telefonlar:
    print(telefon)
"""


sonuc = min(yaslar)
sonuc = max(yaslar)

sonuc = yaslar.count(1998)

print(sonuc)




markalar = []

marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)


print(markalar)
