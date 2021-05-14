# -*- coding: utf-8 -*-
# MAP fonks.
sayilar = [1,-2,5,-7,-9,12]
str_sayilar = ["1","2","3","4","5","6"]
isimler = ["ali","deniz","yücel","ahmet"]
kareler = []

for sayi in sayilar:
    kareler.append(sayi**2)

print(kareler)

def kare_al(sayi):
    return sayi**2

sonuc = list(map(lambda sayi: sayi**2, sayilar)) # kare al ı lambda olarak tanımladık
sonuc = list(map(int, str_sayilar))
sonuc = list(map(float, sayilar))
sonuc = list(map(abs, sayilar))
sonuc = list(map(len, isimler))
sonuc = list(map(str.upper, isimler))

print(sonuc)

# FİLTER FONKS. 

yaslar = [5,12,18,24,45]

def yetiskinmi(x):
    if x<18:
        return False
    else: 
        return True

sonuc = list(filter(yetiskinmi, yaslar))
sonuc = list(filter(lambda x: x>=18, yaslar))

sayilar = [0,1,25,6,8,9]
sonuc = list(filter(lambda x: x%2!=0, sayilar))

isimler = ["çınar","yiğit","sena","ada","ali"]
sonuc = list(filter(lambda n: n[0]=='a',isimler))

filteredResult = filter(lambda n: n[0]=='a',isimler)
sonuc = list(map(lambda n: n.upper(), filteredResult))

users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"]},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": ["tweet 1"]}
]

sonuc = list(filter(lambda u: len(u["tweets"])>0, users))
sonuc = list(map(lambda  u: u["username"].upper(), filter(lambda u: len(u["tweets"])>0, users)))

sonuc = [user["username"].upper() for user in users if len(user["tweets"])>0]

print(sonuc)


# ANY-ALL Fonksy.

sonuc = all([True,True,False])
sonuc = all([True,True,True])
sonuc = any([True,False,False])

# And => True and True => True => All()
# Or  => True or False => True => Any()

sayilar = [0,1,3,6,8,9,10]

sonuc = any([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = all([sayi%2==0 for sayi in sayilar])
sonuc = any([sayi%2==0 for sayi in sayilar])

kisiler = ["ali","ahmet","çınar"]

sonuc = any([kisi[0]=='a' for kisi in kisiler])
sonuc = all([kisi[0]=='a' for kisi in kisiler if kisi[0]=='a'])

print(sonuc)

# SORTED Fonks.

sayilar = [1,53,45,67,97,5,7]

sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,53,45,67,97,5,7))

users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"],"mail":"info@gmail.com"},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": ["tweet 1"],"name":"","phone":"54421126t6t"}
]


sonuc = sorted(users,key=len)
sonuc = sorted(users,key=len,reverse=True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key= lambda user: user["tweets"])
sonuc = sorted(users, key= lambda user: len(user["tweets"]),reverse=True)


kurslar = [
    {"title":"python","students":25000},
       {"title":"web","students":35000},
    {"title":"javascript","students":5000},
 
    ]
sonuc = sorted(kurslar , key=lambda kurs: kurs["students"])
sonuc1 = sorted(kurslar , key=lambda kurs: kurs["students"])
sonuc = list(map(lambda kurs: kurs["title"], sonuc1 ))



print(sayilar)
print(sonuc)

# MİN- MAX

sayilar = [1,5,7,45,25,89]
harfler = ['a','v','h','s']
isimler = ['ahmet','ismail','ada','sena','sadık']

sonuc = min(sayilar)
sonuc = max(sayilar)

sonuc = min(harfler)
sonuc = max(harfler)

sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min([len(isim) for isim in isimler])
sonuc = max([len(isim) for isim in isimler])

sonuc = max(isimler, key=lambda n: len(n))
sonuc = min(isimler, key=lambda n: len(n))

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}
]

sonuc = min(urunler, key=lambda urun: urun['price'])
sonuc = min(urunler, key=lambda urun: urun['price'])['title']
sonuc = max(urunler, key=lambda urun: urun['price'])['title']

max = 0

for urun in urunler:
    if urun["price"]>max:
        max = urun["price"]

print(max)

print(sonuc)

#ABS SUM ROUND

sayilar = [34,2,5,7,98]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 10)

urunler = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
    {"title":"iphone 11 Pro", "price": 0},
]

# toplamFiyat = sum([urun["price"] for urun in urunler])
# sonuc = toplamFiyat / len(urunler)

toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdeti = len([urun for urun in urunler if urun["price"]>0])
sonuc = toplamFiyat / urunAdeti

sonuc = round(10.2)
sonuc = round(10.6)
sonuc = round(10.5)
sonuc = round(1.424242, 2)
sonuc = round(1.426242, 2)
sonuc = round(1.426242, 4)

print(sonuc)
print(toplamFiyat)
    