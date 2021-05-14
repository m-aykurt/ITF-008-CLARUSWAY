# -*- coding: utf-8 -*-

numbers = [1,3,7,4,3,0,6,3]

numb = max(numbers, key=numbers.count) # max fonksiyonunun key parametresini en cok olanın(tekrar edenin) en buyuğu şeklinde değiştirdik

print(f"in the numbers list most frequent numbers is {numb} ")

print(
      "(----------------------------------)")

# kullanıcıdan değer alarak yapılan yöntemi

how_many = int(input("kac defa sayi girmek istiyorsunuz : "))
list1 = []
for i in range(how_many):
    numb = int(input("bir sayi giriniz: "))
    list1.append(numb)
    
numb_max = max(list1, key=list1.count)
print(f"in the numbers list most frequent numbers is {numb_max} ")

   
