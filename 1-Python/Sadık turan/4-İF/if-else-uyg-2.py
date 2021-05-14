# -*- coding: utf-8 -*-

benzin = 7.5
dizel = 6

aracYakitTipi = input("arac yakıt tipi : ")
kacKmYol = float(input("kac km yol yaptınız:s ")) 

kmYakit = float(input("aracınız 100 km de kac litre yakıt harcıyor :"))

formulBenzin = (( kmYakit /100) * kacKmYol) * benzin
formulDizel = (( kmYakit  /100) * kacKmYol) * dizel

if (aracYakitTipi == benzin):
    print("aracın yakıt masrafı : ",formulBenzin)
else:
    print("aracın yakıt masrafı : ",formulDizel)