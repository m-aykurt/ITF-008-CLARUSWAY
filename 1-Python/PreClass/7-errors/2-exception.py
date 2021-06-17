# -*- coding: utf-8 -*-

try :
    a = 10
    b = 2
    print("The result of division is :", c)
except Exception as e:
    print("The error message is : ", e)
    
count = 3
while count>0:
    fruits=["banana","mango","pear","apple","kiwi","grape"]
    try:
        x = int(input("indeks numarası giriniz: "))
        print(f"benim favori meyvem {fruits[x]}'dir")
        
    except IndexError:
        count -=1
        print(f"Böyle bir index bulunmamaktadır.{count} adet giriş hakkınız kaldı")
        
    except ValueError:
        count-=1
        print(f"lütfen sayı giriniz.{count} adet giriş hakkınız kaldı")
        
    else:
        print("tebrikler. doğru giriş yaptınız.")
        break
    finally:
        print("bizim meyvelerimiz her zaman tazedir.")

    