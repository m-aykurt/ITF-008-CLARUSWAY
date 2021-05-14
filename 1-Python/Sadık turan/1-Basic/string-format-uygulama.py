# -*- coding: utf-8 -*-

website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
len(kursAdi)
len(website)
print(len(kursAdi))
# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.
karakterSayisi = len(website)
print(website[karakterSayisi-3:karakterSayisi])

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
print(kursAdi[0:15])
print(kursAdi[-15:-1])
# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1])



msj = "Hello world"



msj1 = "abc"
print("abc " * 3)""

name, surname, age, job = "murat","aykurt","29","IT"

print("Benim adım " + name,surname + " yaşım " +age + " mesleğim " + job)
print("Benim adım {n} {s} , Yaşım {a}, mesleğim {j}".format(n = name, s = surname, a = age, j = job))
print(f"benim adım{name} soyadım {surname}")

