# -*- coding: utf-8 -*-

website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Pythton Programlama"

msg = " Hello World "

sonuc = msg.strip()  # 1




msg1 = "kurs adi"  
sonuc=msg1.upper()  # 3


msg2 = "website"
sonuc = msg2.count("a")  



sonuc = "www.sadikturan.com".strip("w.moc")  # 2


sonuc = website.count("a")  


sonuc = website.startswith("http")
sonuc = website.endswith("com ")
"""

sonuc = website.index(".com")
sonuc = website.find(".com",0,10)

sonuc = kursAdi.rfind("Python")
sonuc = kursAdi.rindex("react")

"""

sonuc = kursAdi.isalpha()
sonuc = kursAdi.isdigit()
sonuc = "123".isdigit()


sonuc = "contents".center(50,"*")
sonuc = "contents".ljust(50,"*")


sonuc = kursAdi.replace(" ", "-")
sonuc = kursAdi.replace("a", "b")


sonuc = kursAdi.join(" ")













print(sonuc)