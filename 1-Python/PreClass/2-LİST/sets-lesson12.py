# -*- coding: utf-8 -*-
"""
set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
set2 = set(colors)
print(set_1)
print(set2)

letter = "a b c d e f g h i j k l m n o p r s t u v y z".split()
print(letter)

letter1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z']

letter2 = set(letter1)
print(letter2)
print(letter2)
letter1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z']
print(set(letter2))

x = {}
print(type(x))

y =set() 
print(y)

a = {'carnation', 'orchid', 'rose', 'violet'}
b = {'rose', 'orchid', 'rose', 'violet', 'carnation'}

print(a==b)
"""

a = set("philedelphia")
b = set("dolphin")

print(a.intersection(b)) # kesişim
print(b.intersection(a))

print(a-b) # a fark b - sadece a da olanlar
print(a.difference(b))

print(b-a) # b fark a - sadece b de olanlar
print(b.difference(a)) 

print(a | b) # a bileşim b
print(a.union(b))

print(a | b) # b bileşim a
print(b.union(a))

date = "14/04/2021"
x = set(date)
y = list(date)
print(y)
print(x)

date1 = {"14/04/2021"}
print(date1)

given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]
uniq = set(given_list)
print(uniq)

usa_capt = set("washington")
nz_capt = set("wellington")

print(usa_capt.intersection(nz_capt))
print(usa_capt.union(nz_capt))
print(usa_capt.difference(nz_capt))
print(nz_capt.difference(usa_capt))