# -*- coding: utf-8 -*-

numb = list(range(12))
sonuc = numb.sort()
print(sonuc)
print(numb[0:7:2])

print(len([[12, 34, 56]][0]))

number = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

print(number)

try_tuple = ("love",)
print(try_tuple)
print(type(try_tuple))

planets = "mercury", "jupiter", "saturn"

print(planets)
print(type(planets))

empty = ()
print(empty)
print(type(empty))

my_tuple = (1,2,3,5,7,8,9)
my_list = list(my_tuple)

print(type(my_list),type(my_tuple),my_list,my_tuple)



mountain = tuple("alps",)
print(type(mountain))
print(mountain)


numb = (2,3,5,8,7)
print(numb[4:0:-1])
print(numb[:3])
print(numb[3:])
print(numb[::2])



my_list = list(range(11))

my_list.reverse()
my_list.pop()
print(my_list)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

# print(grocer[1][1][1],[1][1][3],[1][1][5])


flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = f"My two favorite are flowers {flowers[0][2]} and {flowers[0][1][1]}, two favorite colors are {colors[1][0]} and {colors[1][1][1]}."
print(text)
