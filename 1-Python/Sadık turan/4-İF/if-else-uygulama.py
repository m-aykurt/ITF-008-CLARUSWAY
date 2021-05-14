# -*- coding: utf-8 -*-

#sayi int(input("sayi giriniz : "))

# if (sayi>50) and (sayi<100):
   # print("sayi 50 ile 100 arasındadır")
# else:
    # print("sayi 50 ile 100 arasında değildir")
"""    
if (sayi>0) and (sayi % 2==1):
    print("sayi pozitif tek sayıdır")

else:
    print("sayı pozitif tek sayı DEGİLDİR")
"""
"""
username = "sadikturan"       
password = "1234"

id1 = input("id giriniz: ")


if (username == id1):
    print("parola giriniz")
else:
    print("kullanıcı adı hatalı")
parola = input("parola giriniz")
if (password == parola):
        print("uygulamaya hosgeldiniz")
else:
            print("parola hatalı")
"""
"""
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x>y) and (x>z):
    print("x en büyük sayıdır.")
if (y>) and (x>z):
    print("x en büyük sayıdır.")
if (x>y) and (x>z):
    print("x en büyük sayıdır.")    
    
"""
"""
vize1 = int(input("vize1 : "))
vize2 = int(input("vize2 : "))
final = int(input("final : "))

ortalama = (((vize1+vize2)/2)*0.6)+(final*0.4)
"""
#if (ortalama>=50):
#    print("ogrenci basarılı notu:",ortalama)
#else:
#    print("ogrenci basarısız notu: ",ortalama)
    
# if (ortalama>=50):
 #   if (final>=50):
 #       print("ogrenci basarılı notu:",ortalama)
 #   else:
 #       print("ogrenci basarısız.Finalden en az 50 almalıdır. notu :", ortalama)
# else:
 #   print("ogrenci basarısız notu: ",ortalama)
 
"""
if (ortalama>=50):
    print("ogrenci basarılı gecti notu: " ,ortalama)
else:
    if (final>=70):
        print("ogrenci gecti cünkü final puanı 70 ve üzerinde. notu: ", ortalama)
    else:
        print("ogrenci kaldı notu: ",ortalama)
 """

ad = input("ad giriniz : ")
kilo = int(input("kilo giriniz : ")) 
boy = float(input("boy giriniz : ")) 

formul = (kilo/(boy**2))

if (0<formul<=18.4):
    print("kişi zayıftır, vki: " , formul)
else:
    if(18.5<formul<=24.9):
        print("kişi normal kiloludur. vki: " , formul)
    else:
        if(25<formul<=29.9):
            print("kişi fazla kiloludur. vki: " , formul)
        else:
             if(30<formul<=34.9):
                 print("kişi obezdir. vki: " , formul)
             else:
                 print("degerleriniz yanlıs")

        










"""
zayif = (formul>0) and (formul<18.4)
print("kisi zayıftır" , zayif)
normal = (formul>18.5) and (formul<24.9)
print("kisi normal kiloludur" , normal)
fazlaKilolu = (formul>25) and (formul<29.9)
print("kisi fazla kiloludur" , fazlaKilolu)
obez = (formul>30) and (formul<35)
print("kisi obezdir" , obez)
"""

    