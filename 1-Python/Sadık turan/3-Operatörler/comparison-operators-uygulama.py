

"""
x1 = int(input("x1 sayisini giriniz"))

x2 = int(input("x2 sayisini giriniz"))

sonuc = (x1 > x2)
"""




not1 = float(input("1.sınav notunu giriniz: "))
final = float(input("final : "))
ortalama = (((not1 + not2)/2) * 0.6 ) + (final * 0.4)

sonuc = (ortalama > 50)

print(f"{ortalama} ile gecti. : {sonuc}")



"""
email = "info@sadikturan.com"
parola = 12345
mail = input("email giriniz: ")
password = input("sifre giriniz: ")

sonuc = (mail == email)
print(sonuc)
"""

sayi = int(input("sayi giriniz: "))

# sonuc = (sayi % 2 == 0)
sonuc = (sayi > 0)
print(f"{sayi} pozitif sayidir. : {sonuc}")
