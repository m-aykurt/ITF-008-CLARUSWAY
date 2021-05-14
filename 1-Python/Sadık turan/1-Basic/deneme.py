"""

website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri : Sıfırdan İleri Seviye Python Programlama"

sonuc = len(kursAdi)

sonuc = website[7:10]

karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]
sonuc = kursAdi[0:16]
sonuc = kursAdi[-15:]
sonuc = kursAdi[::-1]

sonuc="hello world".replace("w", "W")

sonuc = "abc "*3

name, surname, age, job = "murat", "aykurt", 29, "IT"  
sonuc = "benim adım {n} {s}, yaşım {a} , mesleğim {j}".format(n=name, s=surname, a=age, j=job)

print(sonuc)
"""









"""




msg = "Python Kursumuza Hoş Geldiniz.Ben Murat Aykurt"


sonuc = msg.islower()
sonuc ="   aaa    -222".strip()
sonuc ="aaa  --- -    333   ".split("3")
sonuc = msg.split(" ")
sonuc = "---".join(sonuc)
sonuc = msg.index("Hoş")
sonuc = msg.endswith('T')


sonuc = msg.replace("Murat", "kj").replace(" ", "-")


sonuc = msg.count("z")
sonuc = msg.index("H")
sonuc = msg.isspace()

print(sonuc)



"""


website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri : Sıfırdan İleri Seviye Python Programlama"

result = "  hello world  ".strip()

result = "www.sadikturan.com".strip("w, ., c, o, m")

result = kursAdi.lower()

result = website.count("a")

result = website.startswith("www")


result = kursAdi.isdigit()
result = kursAdi.isalpha()

result = "contents".ljust(50,"-")

result = kursAdi.replace(" ", "-")

result = "hello world".replace("world", "there")

result = kursAdi.lower().split()

print(result)














