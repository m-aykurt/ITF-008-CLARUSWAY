"""
website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri:Sıfırdan İleri Seviye Python Programlama"
"""
"""
sonuc = len(kursAdi)
sonuc = website[7:10]
sonuc = website[-15:]
sonuc = kursAdi[:15]
sonuc = kursAdi[::-1]
sonuc = "Hello world".replace("w", "W")
sonuc = "abc "*3


name, surname, age, job = "murat","aykurt",29,"IT",

print("Benim adım {0} {1}, yaşım {2} ve mesleğim {3}.".format("murat","aykurt",29,"IT"))
"""
"""

sonuc = "   hello world.     ".strip()
sonuc = website.strip("/:htpw.com")

sonuc = website.upper()
sonuc = website.count("a")
sonuc = website.startswith("htt")
sonuc = website.endswith(".com")
sonuc = kursAdi.isdigit()
sonuc = "contents".center(50,"*")
print(sonuc)
"""
"""
diller = ["python","c#","java","javascript","react"]


sonuc = diller
sonuc = type(diller)
sonuc = diller[:2]


sonuc = diller.append("angular")

if "python" in diller:
    print("evet")
    
for x in diller:
    print(x)
    
    
del diller[0]

print(diller)


print(sonuc)

"""
"""
isimler = ["ada","yigit","hasan","beril"]
yaslar = [1998,2000,1998,1997]


isimler.append("cenk")
isimler.insert(0, "sena")
isimler.remove("yigit")
sonuc = isimler.index("sena")
sonuc = isimler.count("beril")
sonuc = isimler[::-1]

sonuc = isimler.sort()
isimler.reverse()
yaslar.sort()
yaslar.reverse()

st = ["iphone x","iphone xr"] 

print(st)

print(min(yaslar))
print(max(yaslar))

sonuc = yaslar.count("1998")
sonuc = yaslar.clear()

print(sonuc)




print(isimler)
print(yaslar)



markalar = []

marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)


print(markalar)
"""
"""
plakalar = {"kocaeli":41,"istanbul":34}

plakalar["rize"] = 53


print(plakalar)
"""
"""
ogrenciler = {
            100:{
              "ad":"murat",
              "soyad":"aykurt",
              "yas":29,
              "meslek":"IT"
              
            }
              ,
              101:{
              "ad":"selin",
              "soyad":"aykurt",
              "yas":28,
              "meslek":"ogretmen"
              }
                  }

for x in ogrenciler[100].items():
    print(x)
for x in ogrenciler[101].items():
    print(x)

# print(ogrenciler[100]["yas"])
"""


"""
id = input("urun id giriniz: ")
ad = input("adı giriniz: ")
fiyat = input("fiyatı giriniz: ")

urunler[id] = {
    "ad": ad,
    "fiyat":fiyat}
id = input("urun id giriniz: ")
ad = input("adı giriniz: ")
fiyat = input("fiyatı giriniz: ")

urunler[id] = {
    "ad": ad,
    "fiyat":fiyat}

id = input("urun id giriniz: ")
ad = input("adı giriniz: ")
fiyat = input("fiyatı giriniz: ")

urunler[id] = {
    "ad": ad,
    "fiyat":fiyat}
"""
"""
id = input("sorgu için id giriniz: ")
sonuc = urunler[id]

print(sonuc)

"""
"""
cigarette = False # i dont smpke cigarette
chronic = False # i dont have chronic ill
immune = False # i have strong immune system

risk = cigarette or chronic or immune




print(f"There are risks for Covid-19 {risk}")
"""
"""
# a, b, c = 2,5,10

# x = int(input("x: "))
# y = int(input("y: "))

# sonuc = (x*y) - (a+b+c)
#sonuc = c//b
#  sonuc = (a+b+c) % 3
# sonuc = b ** a

sayilar = 1,5,7,10,3

a, *b,  c= sayilar

print(b[0]+b[1]+b[2])
"""

"""
a, b, c, d =5, 5, 20, 4
username = "sadikturan"
password = "12345"

sonuc = (a == b)
sonuc = (a != b)
sonuc = (a == c)
sonuc = (username == "sadikturan")
sonuc = (a > c)
sonuc = (c >= a)
sonuc = (a >= b)
 

print(sonuc)
"""
"""
sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi 2: "))

sonuc = (sayi1>sayi2)
sonuc = (sayi1>0)


print(sonuc)
"""
"""
vize1 = int(input("vize 1: "))
vize2 = int(input("vize 2: "))

final = int(input("final: "))

ortalama = (vize1+vize2/2)*0.6 + (final*0.4)

if (ortalama>=50):
    print(f"not ortalamanız {ortalama} ve sonuc geçtiniz")
else:
    print(f"not ortalamanız {ortalama} ve Kaldınız")
"""


"""
email = "info@sadikturan.com"
parola = "12345"

mail = input("mail adresiniz: ")
password = input("parola: ")

if mail == email:
    print("parola giriniz: ")
    if parola == password:
        print("giris basarılı")
    else:
        print("parola yanlıs")
else:
    print("mail yanlıs")
 """
"""
hak = 1
devam = "e"

sonuc = (hak>0) and (devam =="e")

print(sonuc)
"""

"""
x = int(input("bir sayı giriniz: "))

sonuc = (50<x<100)
sonuc = (x>0) and (x % 2 == 0)

print(sonuc)
"""
"""
username = "maykurt92"
password = "1152"

mail = input("mail giriniz: ")
parola = input("parola giriniz: ")

sonuc = (username == mail) and (password == parola)

print(sonuc)
"""
"""
x = int(input("x: "))
y = int(input("y: "))

z = int(input("z: "))


sonuc = (x > y) and (x > z)
print(f"x en buyuk {sonuc}")
sonuc = (y > x) and (y > z)
print(f"y en buyuk {sonuc}")
sonuc = (z > x) and (z > y)
print(f"z en buyuk {sonuc}")
"""
"""
vize1 = int(input("vize 1: "))
vize2 = int(input("vize 2: "))

final = int(input("final: "))

ortalama = (vize1+vize2/2)*0.6 + (final*0.4)
"""
"""
if (ortalama>=50):
    print(f"not ortalamanız {ortalama} ve sonuc geçtiniz")
else:
    print(f"not ortalamanız {ortalama} ve Kaldınız")
  """ 
"""
if (ortalama >= 50):
    if (final >= 50):
        print(f"basarılı geçtiniz")
    else:
        print(f"final notunuz 50 altında kaldınız ")
else:
    print(f"ortalamanız 50 altında kaldınız")
"""
"""
ad = input("adınızı giriniz: ")
kilo = float(input("kac kg: "))
boy = float(input("boy: "))

vki = kilo / (boy**2)

if (0< vki <=18.4):
    print("zayıf")
elif (18.5<vki<24.9):
    print("normal")
elif (25<vki<29.9):
    print("fazla kilolu")    
elif (30<vki<35):
    print("obez")
else:
    print("girdiginiz degerler yanlıs")
"""

"""
tekrar = list(range(5))

print(tekrar[0:5:2])
"""
"""
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])
print(len([[12, 34, 56]][0]))


odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



print(odd_no[6:2:-1])
"""
"""
print(format("Welcome", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.2f"))


print('*', "abcdef".center(7), '*')

print(not 0 and "write me")
"""
"""
city = ["new york","london","istanbul","seoul","sydney"]
city.append("kırklareli")
city.insert(1,"kırklareli")
# city.remove("kırklareli")
# city.pop(0)
city.sort()
city.reverse()
city.sort()
city[1] = "edirne"

sonuc = city[0:2]
sonuc = city[2::-1]
sonuc = city[0:2]

print(sonuc)

"""


# print("abc".ljust(15,"-"))





text = "           deneme--22 istanbul-eskişehir-izmir"

print(text.strip(" "))
print(text.split())
print(text)
