# -*- coding: utf-8 -*-

sayilar = [1,5,10,15,16,35,57,72,75,20]
"""
for x in sayilar:
    print(x)

for x in sayilar:
    if (x % 5 == 0):
        print(x)
"""     
"""   
toplam = 0

for sayi in sayilar:
    toplam = toplam + sayi
    
print(toplam)
"""
"""
for sayi in sayilar:
    if (sayi % 2 == 0):
        print(sayi,sayi**2)
"""

urunler = ["İphone 7","İphone 8","İphone X","İphone XR","Samsung S10",]

for urun in urunler:
    print(urun, urun[1])
    
count = 0
for urun in urunler:
    index=urun.find("İphone")
    if (index>-1):
        count += 1 
print(count)