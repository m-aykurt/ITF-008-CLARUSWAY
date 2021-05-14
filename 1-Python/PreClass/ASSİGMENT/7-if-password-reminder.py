# -*- coding: utf-8 -*-

password = "12345"
name = "murat"

isim = input("isminiz: ")
parola = input("parola giriniz: ")

if parola == password and name == isim:
    print(f"merhaba {name} parolanız is {password} ")
else:
    print(f"merhaba {isim}, see you later ")