# -*- coding: utf-8 -*-

sayilar = [4,6,9,10,35,57,89,125,244]

# sayilar listesini while ile ekrana yazdırın

for i in sayilar:
    print(i)
    
i = 0
while (i<len(sayilar)):
    print(sayilar[i])
    i +=1
    
#  başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tek sayıları yazdırın
"""
baslangic = int(input("baslangic: "))
bitis = int(input("bitis: "))

i = baslangic
while i < bitis:
    i +=1
    if (i % 2 == 1):
        print("tek sayi",i)


i = 100
while i > 1:
    i -=1
    print(i)

sayilar = []
i = 0
while (i<5):
    sayi = int(input("bir sayi giriniz: "))
    sayilar.append(sayi)
    i +=1

sayilar.sort()
print(sayilar)



urunler = []

adet = int(input("kac adet ürün girmek istersiniz: "))
 
i=0
while (i<adet):
    i +=1
    urun_adi=input("urun adi: ")
    fiyat = int(input("urun fiyatı:"))
    urunler.append({
        "urun_adi":urun_adi,
        "fiyat":fiyat
        })
    
print(urunler)

for urun in urunler:
    print(f"urun adi: {urun['urun_adi']}, urun fiyati: {urun['fiyat']}")
    


isim = "murat aykurt"

for harf in isim:
    if (harf == "a"):
        continue
    print(harf)

isim = "murat aykurt"

for harf in isim:
    if (harf == "a"):
        break
    print(harf)
"""





