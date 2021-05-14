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

    