# -*- coding: utf-8 -*-
"""
liste = [1,2,3]

print(type(liste))
print(liste)

string = "hello"

print(type(string))
print(string)
"""
 # def ile fonksiyon tanımlama
 
def selamlama():
    for i in range(11):
        print("merhaba")



# def ile toplama


def topla():
    a = 10
    b = 20
    print(a+b)
    


# fonksiyondan deger döndürme

def toplam():
    return f"toplam {10+20}"

print(toplam())

def toplam():
    return 10+20

sonuc = toplam() + 50

print(sonuc)

# yas hesaplama

def simdi():
    import datetime
    return datetime.datetime.now().year

print(simdi())

def yas_hesapla():
    return simdi() - 1992

print(yas_hesapla())
    
def saat():
    import datetime
    return datetime.datetime.now().hour

print(saat())

def selamla(isim):
    if (saat() < 12):
        return "gunaydın " + isim
    elif (13<saat()<18):
        return "iyi günler " + isim
    else:
        return "iyi aksamlar " + isim
        
print(selamla("Murat"))
print(type(selamla("murat")))

# parametre tanımlama

def toplam(a,b):
    return a + b

print(toplam(3, 5))


def yas_hesapla(dogum_yili):
    return 2021 - dogum_yili

print(yas_hesapla(1993))


def emeklilige_kac_yil(dogum_yili , isim):
    yas = yas_hesapla(dogum_yili)
    
    kalan_sure = 65 - yas
    
    if kalan_sure > 0:
        print(f"{isim} , emekliliginize {kalan_sure} yil kaldi")
    else:
        print(f"{isim} , zaten {abs(kalan_sure)} yil önce emekli oldunuz")
        
    
emeklilige_kac_yil(1992, "murat")
emeklilige_kac_yil(1924, "murat")


