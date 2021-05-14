# -*- coding: utf-8 -*-

# all-- fonks.-------kapsadığı collectionda herhangi bir değer varsa True eğer boşsa False verir

names = ["susan","murat","kemal"]
mood = ["good","sad",0]
empty = []

print(all(names),all(mood),all(empty),sep=("\n"))

# any ----------bir true bile true verir tamamı false olursa false döner , empty ise false verir

names = ["susan","murat",False]
mood = [None,(),0]
empty = []

print(any(names),any(mood),any(empty))

# filter() parameters--- Fonksiyon neyi true döndürüyorsa ardından gelen iterable ifadeler öyle geçer.-- YANİ İTERABLEDAKİ TRUE LARI DÖNDÜRÜYOR

list_a = ["susan","tom",False,0,"0"]

filtered_list = filter(None, list_a) # None koyduğumuzda iterable in true larını döndürür

print(*filtered_list)


# enumerate

grocery = ["bread","water","olive"]
enum_grocery = enumerate(grocery,)

print(type(enum_grocery))
print(*enum_grocery)
print(list(enum_grocery)) # yukaruda enum_grocery kullandııgmız için altta gözükmüyor

# max-min fonks.

print(max("ahmet"))
print(ord("t"))

for i in "ahmet":
    print(i,ord(i))
    
# sum(iterable,start) - iterableları toplama yapar.

print(sum([1,2,3,4,5,6]))

# round(numbers, ndigits) -- yuvarlama-

print(round(12))
print(round(10.8))
print(round(3.665,2))
print(round(3.675,2))

