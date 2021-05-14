# -*- coding: utf-8 -*-

sayilar = [1,5,15,35,57,72,75,10,4,20]
"""
for i in sayilar:
    print(i)

for (i) in sayilar:
    if (i%5==0):
        print(i)
toplam = 0
for i in sayilar:
    toplam = toplam + i
print(toplam)

for i in sayilar:
    if (i % 2 == 0):
        print(i**2)

"""
"""
urunler = ["iphone 8","iphone x","iphone xr","samsung s10",]

for x in urunler:
    print(x[1])
    
for x in urunler:
    print(x.count("iphone"))
count=0  
for x in urunler:
    index = x.find("iphone")
    if (index > -1):
        count +=1
        
print(count)
"""
urunler = [
    {"name":"iphone 8","price":"4000"},
    {"name":"iphone 8 plus","price":"5000"},
    {"name":"iphone x","price":"6000"},
    {"name":"iphone xr","price":"7000"},
    {"name":"iphone 11","price":"8000"},
    {"name":"samsung s10","price":"6000"}
    ]

for urun in urunler:
    print(urun)

toplam = 0    
for urun in urunler:
    toplam = toplam + int(urun["price"])
print(toplam)

for urun in urunler:
    if int(urun["price"])<=6000:
        print(urun)
        
ad = input("urun adı: ")

for urun in urunler:
    if (urun["name"].count(ad)):
        print(urun)
    else:
        print("boyle bır urun yok")