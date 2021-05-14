# -*- coding: utf-8 -*-


sayi = int(input("sayi giriniz: "))
asalmi = True

if (sayi == 1):
    asalmi = False
    
for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break
    
if asalmi:
    print(f"{sayi} asaldir")
else:
    print(f"{sayi} asal degildir")

# joseph hoca çözümü

n = int(input("enter a number: "))
count = 0

for i in range(1,n+1):
    if not n % i : 
        count +=1
    
if (n == 0) or (n==1) or count>=3:
    print(n," is NOT prime number")
else:
    print(n," is a prime number")