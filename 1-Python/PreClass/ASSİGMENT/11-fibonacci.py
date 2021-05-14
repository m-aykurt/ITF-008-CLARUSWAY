# -*- coding: utf-8 -*-
# fibonacci sayıları

sayi = int(input("sayi giriniz: "))

numb_list = []

numb1 , numb2 = 0,1


if sayi>0:
    while numb2 < sayi:
        numb_list.append(numb2) 
        numb1,numb2 = numb2,numb1+numb2 # numb1 numb1 ve numb2 nin toplamına eşit olup devam ediyor.
else:
    print("enter a positive numbers")

print(numb_list)



