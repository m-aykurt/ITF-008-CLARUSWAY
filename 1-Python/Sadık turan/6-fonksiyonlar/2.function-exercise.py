# -*- coding: utf-8 -*-

def kackez(text, adet):
    return text * adet

print(kackez("murat\n", 5))

# dikdörtgen alan fonksiyonu

def dikd_alan(a_kenari, b_kenari):
    return a_kenari * b_kenari

print(dikd_alan(5, 2))

def dikd_cevre(a_kenari , b_kenari):
    return 2 * (a_kenari + b_kenari)

print(dikd_cevre(5, 2))

# random metodu

def yazi_tura():
    import random
    sayi = random.random()
    
    if sayi>0.5:
        return "TURA"
    else:
        return "YAZI"

print(yazi_tura())


# gönderilen 2 sayı arasındaki asal sayıları bulma fonks.

def asal_sayi_bul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if (sayi>1):
            for i in range(2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

# asal_sayi_bul(10, 42)

# sayının tam bölenlerini bulma

def tam_bolenleri_bul(sayi):
    tam_bolenler = []
    
    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolenler.append(i)
            
    return tam_bolenler
    
print(tam_bolenleri_bul(15))    
    