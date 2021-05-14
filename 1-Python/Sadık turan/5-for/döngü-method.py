# -*- coding: utf-8 -*-

r = range(10)
r = range(5,50,2)
r = range(10,90,10)
r = range(0,-10,-2)


sonuc = list(r)

print(sonuc)

liste = []
for i in range(10):
    liste.append(i)
    #  print(liste)
    # print(i,end=(" "))
    
# ENUMERATE

markalar = ["opel","bmw","mercedes","toyota","mazda","ford"]

for i in markalar:
    print(i)


obj1 = enumerate(markalar)
print(type(obj1))
print(list(obj1))


for index,value in enumerate(markalar,2): # , den sonraki int deger nereden baslayacagını söyler
    print(index,value)

    
# ZİP  METODU

liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e","f"]
liste3 = [100,200,300,400,500,600,700,800,900]

print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2):
    print(item)
    
for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)
    
"""  
# carpim tablosu

x = int(input("hangi sayının carpim tablosunu görmek istersiniz: "))

for i in range(11):
    print(f"{i} x {x} = {i*x} dir")
    

for i in range(1,11):
    print("--------------")
    for k in range(1,11):
        print(f"{i}x{k}={i*k}")
"""  
    
sayi = int(input("sayi giriniz: "))
asalmi = True

if (sayi == 1):
    asalmi = False
    
for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break
    
if asalmi:
    print(f"{sayi} asaldir")
else:
    print(f"{sayi} asal degildir")