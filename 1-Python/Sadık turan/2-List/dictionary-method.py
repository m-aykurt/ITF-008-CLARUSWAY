# -*- coding: utf-8 -*-

opelObj = {
    "marka":"opel",
    "model":"corsa",
    "yil":2020
    }
sonuc = opelObj
sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj.values():  # value değerlerini almak için
  #   print(x)
 
for x,y in opelObj.items():
    print(x,y)
    
sonuc = "marka" in opelObj
"""
opelObj["renk"] = "kırmızı"  # renk kırmızı ekler
opelObj.pop("renk")  # renk i siler
opelObj.popitem()  # son item i siler
"""
# del opelObj["marka"]

obj = opelObj  # ikisini de değiştiriyor

obj = opelObj.copy()

# obj["marka"] = "mazda"
opelObj.update({
    "marka":"bmw",
    "model":"3.16",
    "renk":"kırmızı"
    })


print(opelObj)

