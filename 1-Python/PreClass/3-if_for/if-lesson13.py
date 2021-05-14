# -*- coding: utf-8 -*-

if True:
    print("it is true")

if False:
    print("it is false")

if 1:
    print("ben")
    
if None:
    print("ahmet")
if 0:
    print("mehmet")
if {}:
    print("veli")
if ():
    print("hasan")

# hamburger algoritması
minced = True
bread = True

lettuce = False
pepper = True

store = True

hamburger = (minced and store and bread) and (lettuce or pepper)

if hamburger:
    print("bon apetite")
    
    
# set karşılaştırma Task ı

a = set("twelve plus one")
b = set("eleven plus two")

if a == b:
    print("they are same")
else:
    print("they are not same")

# x = input("Yes or No: ")

# if x=="Yes":
 #   print("You entered True")
#else:
 #   y=="No"
  #  print("You entered No")
  
# convert = input("Yes or No: ").title().strip() == "Yes"

# print(f"You entered {convert}")
""" 
x = int(input("bir sayi giriniz: "))

if x % 2 ==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

x = int(input("bir sayi giriniz: "))

if x > 0:
    print(f"{x} is positive number")
else:
    print(f"{x} is negative number")
"""      
# büyük kücük task ı
# x = int(input("bir sayi giriniz: "))
# y = int(input("bir sayi giriniz: "))

#if x > y:
 #   print(f"The large number is {x}")
# else:
  #  print(f"the large number is {y}")
  

bool_value = True 

if bool_value :
    print("Yes")
else:
    print("No")
"""

x = int(input("bir sayi giriniz: "))
y = int(input("bir sayi giriniz: "))
z = int(input("bir sayi giriniz: "))

if (x>y) and (x>z):
    print(f"{x} en büyük sayıdır")
elif (y>x) and (y>z):
    print(f"{y} en büyük sayıdır")
elif (z>x) and (z>y):
    print(f"{z} en büyük sayıdır")
else:
    print("your number is wrong")
"""
"""
x = int(input("bir sayi giriniz: "))

if x<0:
    print(f"{x} negatif sayıdır")
elif x>0:
    print(f"{x} pozitif sayıdır")
else:
    print(f"{x} sıfırdır")
x ="b">"a"
print(x)


 """   
    
audience_group = 'kid', 'teen', 'adult'
audience = "teen"
if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")


note = int(input("your note : "))

if note >= 90:
    if note >= 95:
        print("your degree A+")
    else:
        print("your degree A")
elif note >= 80:
    if note >=85:
        print("your degree B+")
    else:
        print("your degree B")
else:
    print("your degree B-")

