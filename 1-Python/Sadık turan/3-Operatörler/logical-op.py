# -*- coding: utf-8 -*-

# x = int(input("sayi 1 giriniz :"))

# sonuc = (x>50 and  x<100)
# sonuc = (x>0 and (x % 2 ==1))
"""
username = input("mail giriniz: ")
password = input("parola giriniz : ")

mail = "maykurt92"
parola = "1152"

sonuc = ((username == mail) and (parola == password))
"""


"""

x = int(input("sayi1 giriniz: "))
y = int(input("sayi2 giriniz: "))
z = int(input("sayi3 giriniz: "))

sonuc = (x>y) and (x>z)  # x en buyuk
print("x en buyuk sayi : " , sonuc)
sonuc = (y>x) and (y>z)  # y en buyuk
print("y en buyuk sayi : " , sonuc)
sonuc = (z>y) and (z>x)  # z en buyuk
print("z en buyuk sayi : " , sonuc)
"""

"""
vize1 = int(input("vize1 : "))
vize2 = int(input("vize2 : "))
final = int(input("final : "))

ortalama = (((vize1+vize2)/2)*0.6)+(final*0.4)

sonuc = (ortalama>50 and final>50) or (final>70)


print(f"ogrenci {ortalama} ile gecti : {sonuc}")
"""

ad = input("ad giriniz : ")
kilo = int(input("kilo giriniz : ")) 
boy = float(input("boy giriniz : ")) 

formul = (kilo/(boy**2))
print(formul)

zayif = (formul>0) and (formul<18.4)
print("kisi zayıftır" , zayif)
normal = (formul>18.5) and (formul<24.9)
print("kisi normal kiloludur" , normal)
fazlaKilolu = (formul>25) and (formul<29.9)
print("kisi fazla kiloludur" , fazlaKilolu)
obez = (formul>30) and (formul<35)
print("kisi obezdir" , obez)


print(formul)
