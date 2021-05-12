# -*- coding: utf-8 -*-
"""
sonuc = 3+4
sonuc = 3*4+2
sonuc = 3+4.0*8
sonuc = 3*5.0+4/2
sonuc = 3*5/2+11
sonuc = 5/2 + 3*88 -12 * (66//2)
sonuc = 3**2
sonuc = 2**5


print(sonuc)
"""
"""
urunA = 5000
urunB = 7500
kdv = 0.18

print(urunA + (urunA * 0.18))
print(urunA * 1.18)

print(urunB * 1.18)
"""
"""
maasAli = 5000
maasAhmet = 3000
vergi = 0.18

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

"""

"""
musteriAdi = "murat"
musteriSoyadi = "aykurt"
musteriAdSoyad = musteriAdi + " " + musteriSoyadi
musteriCinsiyet = True #erkek
TcKimlik = "1154447782"
musteriAdres = "Kırklareli"
DogumYili = 1992
yas = 2021 - DogumYili


siparis1 = 110
siparis2 = 1100.5

siparis3 = 394.5

print(siparis1+siparis2+siparis3)

print(110+1100.5+356.95)

"""
"""

celc = float(input("kac c derece : "))


fahr = (celc*1.8) + 32

print(f"{celc}'c {fahr} fahrenait e eşittir")



km = int(input("kac km : "))

mil = (km / 1.609344)

print(f"{km} km  {mil} mil eder")

"""
"""
name = str(input("what is your name?"))
print("hello" + name)
age = int(input("how old are you"))
if age >= 70:
  print("you are aged to perfection")
else:
    print("your are a spring chiccken")
"""
"""
def maas_hesapla():
    hafta_ucret=200 # haftalık ücreti 200 dolar
    hafta_saat=int(input("Mary hanım bu hafta kaç saat çalıştı= ")) # Mary hanım bu hafta kaç saat çalıştı giriniz.
    if hafta_saat<40: # eğer bu hafta izin kullanıp 40 saatten az çalıştıysa 50 dolar eksik alır.
        print(hafta_ucret-50)
    elif hafta_saat == 40: # eğer bu hafta 40 saat çalıştıysa normal haftalık ücreti alır.
        print(hafta_ucret)
    elif hafta_saat > 40:  # eğer 40 saatten fazla çalıştıysa, çalıştığı 40 saat sonrası için saat başı 15 dolar fazla alır.
        for i in range(41,hafta_saat+1):
            i+=15
        print(i+hafta_ucret)
    elif hafta_saat>=100:
        print("İşletmeniz su işlemektedir. Bir çalışan bu kadar çalıştırılamaz")
"""
"""
x = input("1.sayi: ")
y = int(input("2.sayi: "))

toplam = int(x) + y
print(toplam)
  """

"""
x = 5
y = 2.3
name = "murat"
isOnline = True

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))


x = float(x)
print(x)
print(type(x))

y = int(y)
print(y)
print(type(y))

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
"""
"""
pi = 3.14
r = float(input("yaricap nedir : "))

alan = pi * r**2
cevre = 2 * pi * r

print("alan: "+str(alan))
"""
"""
name = "murat"

print(name[-5],name[0],)
"""

"""
print("")
print("first")
print()

print("second")
print()
"""
"""
text = "www.clarusway.com"
print(text.endswith(".om"))


email = "clarusway@clarusway.com is my e-mail address"

print(email.startswith("r",3))


text = "myemailaddress@clarusway.com"

print(len(text))
print(text.startswith("@", 14))
print(text.endswith(".", 15, 24))

sentence = "I live and work in Virginia"

print(sentence.upper())
print(sentence.capitalize())
print(sentence.swapcase())
print(sentence.replace("live", "born"))

"""

"""

name = "murat"
surname = "aykurt"
age = 29

greeting = "my name is " + name + " " + surname + " and \n I am " + str(age)+ " years old"

print(greeting)
print(len(greeting))
print(greeting[len(greeting)-1])
print(greeting[-1])
print(greeting[::-1])


result =200/700
print(f"the result is {result:1.5}")
"""
"""
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

sonuc = len(website)
sonuc = website[7:10]
sonuc = website[-3:]
sonuc = course[0:15]
sonuc = course[-15:]
sonuc = course[::-1]

name, surname, age, job = "Bora","yılmaz",32,"mühendis"

print(f"Benim adım {name} {surname} , yaşım {age} mesleğim {job}")

print("Hello world".replace("w", "W"))

print("abc "*3)
"""
"""
message = "Hello there. My name is Murat Aykurt"

sonuc = message.capitalize()




isFound = message.startswith("H")

print(isFound)

"""
"""
sayaç = 0  
i_num = "" #  index numaralarını burada saklayalım
ifade = input("bir kelime ya da cümle giriniz: ") 
ara = input("aramak istediğiniz harfi giriniz: ")
for i in ifade:
    if i == ara:
        i_num += str(ifade.index(ara, sayaç))+", "
        #print(f"{ifade} ifadesinde {ara} harfinin index numaraları {ifade.index(ara,sayaç)}")
    sayaç += 1
print("{} ifadesinde {} harfinin index numaraları: {}".format(ifade, ara, i_num))
"""
"""
number = 200/700

print("the result is {n:1.5}".format(n=number))

msg = "Python Kursumuza hoşgeldiniz. Ben murat aykurt"


sonuc = msg.replace("h", "H").replace(" ", "-").replace(".", "").title().capitalize().title().upper().replace("I", "i")

print(sonuc)
"""

"""
website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama"

sonuc = " HELLO WORLD  "
sonuc = " HELLO WORLD  ".lstrip()
sonuc = " HELLO WORLD  ".rstrip()

sonuc = website.strip("/:pthw.com")

sonuc = kursAdi.upper()
sonuc = kursAdi.lower()

sonuc = website.count("a ")
sonuc = website.startswith("www")
sonuc = website.find(".com")
sonuc = website.index(".com")
sonuc = website.endswith(".com")
sonuc = kursAdi.isalpha()
sonuc = "kursadi".isalpha()
sonuc = "contents".center(50,"*")


sonuc = kursAdi.replace(" ", "-") 
sonuc ="hello world".replace("world", "there")
sonuc = kursAdi.split(" ")





print(sonuc)
"""

"""
diller = ["Python","C#","Java","JavaScript",]

sonuc = diller
sonuc = type(diller)
sonuc = diller[0][0:3]
sonuc = diller[0:2]
sonuc = diller[2:]
# diller[0] = "html"
diller[-1] = "html"
sonuc = len(diller)
sonuc = diller +["angular"]
sonuc = diller + ["vueJS"]
"""
"""
deger = input("deger giriniz: ")

if deger in diller:
    print("deger listesinin bir elemanı")
else:
    print("deger listenin elemanı değil")
   
 """ 
 
"""
telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8","Samsung S9",]

sonuc = len(telefonlar)
sonuc = telefonlar[0]
sonuc = telefonlar[-1]
telefonlar[0] = "Samsung s10"
sonuc = telefonlar.index("Samsung S6")
sonuc = telefonlar[-3]
sonuc = telefonlar[0:2]
telefonlar[-2:] = "Samsung S10","Samsung S11"
sonuc = telefonlar + ["İphone X","İphone XR"]
del telefonlar[-1]
sonuc = telefonlar
sonuc = telefonlar[::-1]


for a in telefonlar:
    print(a)
    """
    
    
"""

ogrenciA = ["Yigit","Bilgi",2010,[70,60,70]]
ogrenciB = ["Sena","Turan",1999,[80,60,80]]
ogrenciC = ["Ahmet","Turan",1998,[100,20,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]


for ogrenci in ogrenciler:
    ortalama = [(ogrenci[3][0]+ogrenci[3][1]+ogrenci[3][2]) / 3]
    print(f"{ogrenci[0]} {ogrenci[1]} {2021-ogrenci[2]} {ortalama}")
    

"""
"""
apples = 5
oranges = 10
while apples < oranges:
    print("True")
    apples = apples + 1
    print(apples)
print("code executed")
    
"""
"""
sayilar = [1,3,6,8,9,12,12,12,15,17,2,3]
harfler =  ["a","b","c","s","a","y,","e"]

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)

sayilar.append(4)
sayilar.insert(3,5)
sayilar.insert(99, 99)

sayilar.pop()
sayilar.pop(-1)
sayilar.pop(1)
sayilar.remove(12)
harfler.pop()


sayilar.sort()
sayilar.reverse()

print(sayilar.count(12))
print(sayilar.count(2))
print(sayilar.index(1))

sonuc = sayilar.sort()

print(sonuc)
"""
