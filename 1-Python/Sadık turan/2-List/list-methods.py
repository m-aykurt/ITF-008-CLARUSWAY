# -*- coding: utf-8 -*-

sayilar = [1,3,6,5,8,92,11,45,22,92,36,6,8,4]
harfler = ["a","b","c","k","j","b","y","m"]

sonuc = min(sayilar)
sonuc = max(sayilar)

sonuc = max(harfler)
# ekleme
sayilar.append(10)
sayilar.insert(2,22)

sayilar.insert(4,60)

harfler.insert(1,"j")

# cıkarma
sayilar.pop(0)
sayilar.remove(22)
sayilar.remove(60)


harfler.remove("y")
sonuc = harfler


#sıralama
"""
sayilar.sort()

harfler.sort()
sayilar.reverse()
harfler.reverse()
sonuc = harfler


"""

sonuc = sayilar.count(6)  # arama



sayilar.clear()


sonuc = sayilar


print(sonuc)