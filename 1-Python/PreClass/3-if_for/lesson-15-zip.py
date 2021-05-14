# -*- coding: utf-8 -*-

# ZİP YÖNTEMİ BİRLEŞTİRME
text = ['one','two','three','four','five']
numbers = [1, 2, 3, 4, 5]
city = ["tokyo","kiev","mekke","istanbul","wahsington"]
for x, y,z in zip(text, numbers,city):
    print(x, '=', y,z)
    
    
print(*zip(text,numbers,city))

# TEK VE CİFT SAYI BULMA

numb = list(range(1,11))
even = []
odds = []
for i in numb:
    if i%2==0:
        even.append(i)
    else:
        odds.append(i)
        
print(even)
print(odds)


# TEK CİFT SAYI LİSTESİ UZUNLUĞU BULMA
list1 = [11,2,2,61,48,33,22,76,28,21,77,82,1]

even = []
odds = []
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odds.append(i)
        
print(f"the numbers length of even is {len(even)}")
print(f"the numbers length of odds is {len(odds)}")

# TEK CİFT SAYI LİSTESİ UZUNLUĞU BULMA - DİGER YÖNTEM

even_count = 0
odd_count = 0
example_list = [11,2,24,61,48,33,3]
for i in example_list:
    if i%2 == 0:
        even_count +=1
    else:
        odd_count +=1
print(even_count)
print(odd_count)

numbers = [11,2,24,61,48,33,3,44,12,56,893,84,22,11,90,126,77,43,]
evens = 0
odds = 0
for i in numbers :
    if not i%2 :
        evens += 1
    else:
        odds += 1
print("The count of even numbers : ", evens)
print("The count of odd numbers : ", odds)


# STR OLARAK SAYI YAZDIRMA PİRAMİT

numb = list(range(1,10))
for i in numb:
    print(str(i) * i )
    
print("---------")

# SUM İLE YAPILAN TOPLAMANIN FOR İLE YAPILMASI

x = list(range(1,75))
print(sum(x))

toplam = 0
for i in range(1,75):
    toplam = toplam + i
print(toplam)

# NESTED FOR LOOPS
    
for i in range(1,6)    :
    for ii in range(1,11):
        print(i + ii)
    
    
names = ["susan", "tom", "edward"] 
mood = ["happy", "sad"]

for i in names:
    for ii in mood:
        print(i +" is " + ii)
        

# LİST COMPHERENSİON

# [expression for item in iterable]

# ÖNCEKİ HALİ

my_list = [1,2,3,4,5,6]

new_list = []

for i in my_list:
    if i % 2 == 1:
        new_list.append(i ** 2)
        
print(new_list)

listem = []
for i in range(5):
    listem.append(i)
print(listem)

# list comph.

print([i for i in range(5)])
print([i**2 for i in range(5)])
print([i %2 ==1 for i in range(5)])


# if list comph.

condition = True

if condition:
    a = 1
else:
    a = 0
    
print(a)
print("---------")
a=1 if 2<4 else 0
print(a)

print("---------")

print(1 if 2 > 4 else 0)


# ternary İF condition yapısı

    # execute-body1 if condition else execute-body2

my_list = [1,2,3,4,5,6,7,8]

a = (i **2 for i in my_list if i % 2)

print([i**2 for i in my_list]) # code body

print([i**2 for i in my_list if i%2])
print([i**2 for i in my_list if not i%2])
print(*a)

a = (i**2 for i in my_list)

print(next(a))
print("-")
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


numb = range(11)
even = []
odd = []
for i in numb:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(even)
print(odd)


list1 = [11,2,24,61,72,78,21,73]
even = 0
odd = 0

for i in numb:
    if not i % 2:
        even += 1
    else:
        odd += 1
        
print(f"The count of even numbers: ",even)
print(f"The count of odd numbers: ",odd)
    

# piramit yöntemiyle string

for i in range(1,10):
    print(str(i) * i)
for i in range(9,0,-1):
    print(str(i) * i)
    
    # toplamları gösterme alt alta
toplam = 0
for i in range(1,75):
    toplam = toplam + i 
print(toplam)


sayi = range(1,10)
harf = ["a","b","c","d"]

for i in sayi:
    for ii in harf:
        print(i,ii)
        
# NESTED FOR - 

my_list = [1,2,3,4,5,6,7,7]
new_list = []

for i in my_list:
    if i % 2:
        new_list.append(i**2)
        
print(new_list)

# LİST COMPHRENSİON

print([i ** 2 for i in my_list])

print(1 if 2 > 4 else 0)
print(23 if 3/3 == 1 else 0) 
print("doğru" if 3<5 else "yanlis")

print([i ** 2 for i in my_list if not i % 2]) # cift sayilara ulasmak için
print([i ** 2 for i in my_list if i % 2]) # tek sayiların karesi

a = [i * 2 for i in my_list]

print(a)


numb = input("bir sayi giriniz: ")

print(list(numb))
