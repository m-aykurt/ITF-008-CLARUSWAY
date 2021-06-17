# -*- coding: utf-8 -*-
"""
def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()
    
    with open(yeni_dosya_ismi,"w") as new_file:
        new_file.write(icerik)
dosya_kopyala("msg.txt", "yeni_msg.txt")
"""
"""
def ters_cevir(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()
    
    with open(yeni_dosya_ismi,"w") as new_file:
        new_file.write(icerik[::-1])
ters_cevir("msg.txt", "ters_msg.txt")
"""

def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()
        
    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(" ")) for satir in satirlar),
        "karakter_sayisi": sum(len(satir) for satir in satirlar)
        }
    return sonuc
print(bilgilendir("msg.txt"))
print(bilgilendir("newfile.txt"))
print(bilgilendir("markalar.txt"))


