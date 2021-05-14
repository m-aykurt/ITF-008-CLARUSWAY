# -*- coding: utf-8 -*-

num = input("Please enter a positive integer number : ")
if num.isdigit() :
    a = num.split()
    b=0
    for i in range(len(a[0])) :
        b+=int(a[0][i])**len(a[0])
    if b==int(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
#Diğer yöntem -While ile

while True:
    number = input("Enter a number: ")  # Kullanıcıdan bir girdi istedik.
    try:
        converted_num = int(number)  # Bu girdiyi integer değere çevirdik.
        if converted_num < 0:  # Eğer bu integer değer sıfırdan küçükse.
            print("Sorry, input must be a positive integer (yours is negative), try again!")  # Çıktısını aldık.
            continue  # Tekrardan kullanıcıdan bir girdi almaya gönderdik.
        elif converted_num == 0:  # Eğer bu integer değer sıfır ise.
            print("Sorry, input must be a positive integer (yours is neutral), try again!")  # Çıktısını aldık.
            continue  # Tekrardan kullanıcıdan bir girdi almaya gönderdik.
        elif converted_num > 0:  # Eğer bu integer değer sıfırdan büyük ise.
            a = converted_num  # Bu değeri aşağıda (if içinde) kullanmak için bir değişkene eşitledik (işlem dönsün diye).
            order = len(str(a))  # Değerimizi stringe çevirip uzunluğunu alarak basamak sayısını bulduk.
            summation = 0  # Aşağıdaki while döngüsünde toplamı döndürmek için referans atadık.
            b = a  # While içinde if den farklı olması için değerimizi yine bieğişkene atadık.
            while b > 0:  # Değerimiz sıfırdan büyük ise.
                digit = b % 10  # Son basamağı yakalamak için bölme işleminden kalan operatörü kullandık.
                summation += digit ** order  # Değerimizi sıfırdan büyük olduğu müddetçe toplama ekledik.
                b //= 10  # Sondaki basamağı atıp, en son basamağı bir soldaki basamak olması için.
            if a == summation:  # Eğer değerimiz döngüdeki değerin basamaklarının basamak sayısı kuvveti toplamına eşitse.
                print(a, "is an Armstrong number")  # Çıktısını aldık.
                break  # Prosesi bitirdik.
            else:
                print(a, "is not an Armstrong number")  # Armstrong değilse kullanıcıdan bir girdi almaya gönderdik.
    except ValueError:  # Girilen değer float veya string ise hata alırdık.
        print("That's not an integer try again!")  # Çıktısını aldık.
        
        
        
# joseph hoca çözümü

while True :
    number = input("enter a positive number.")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break
        

def amstrong_number():
    for i in range(0,1):
        sayi=int(input("Lütfen bir sayı giriniz : "))
        if sayi<=0:
            print("pozitif bir sayı giriniz.")
            break
        elif sayi>0:
            basamak=len(str(sayi))
            if basamak==1:
                print("Tek basamklı sayı giremessiniz.")
                break
            elif basamak>1:
                toplam=0
                for i in str(sayi):
                    toplam=toplam+(int(i)**basamak)
                print(f"sayıların rakamlara ayırıp basamak sayısı kadar üssünü alıp toplayınca çıkan sonuç = {toplam}")
                if toplam==sayi:
                    print(f"Girilen sayi = {sayi} bir amstrong sayısıdır.")
                elif toplam!=sayi:
                    print(f"Girilen sayi = {sayi} bir amstrong sayısı değildir.")