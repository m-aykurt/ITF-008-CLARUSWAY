# -*- coding: utf-8 -*-
"""
reef = ["swordfish","shark","whale","jellyfish","lobster","squid","octopus"]
print(reef[-3:])

print(reef[:-3])

print(reef[:])

print(reef[5:1:-1])

print(reef[::-1])

harfler = "a b c d e f g h i j".split()

print(harfler)
print(harfler[7:3:-1])
print(harfler[2:6:-1])

print(sorted(["ahmet","mehmet","ceyhan","seyhan"]))
isimler = ['ahmet', 'ceyhan', 'mehmet', 'seyhan']

sorted_isimler = sorted(isimler)
print(sorted_isimler)

sehirler = ["tokyo","addis ababa","rome","istanbul","rio"]

print(sehirler)

print(sorted(sehirler))

print(sorted(sehirler, key=len, reverse=True))

sehirler = ["tokyo","addis ababa","rome","istanbul","rio"]

sehirler.sort(key=len, reverse=True)
print(sehirler)
print(sehirler)
"""
"""
x = ["a","b","c"]

ben_tuple = tuple(x)
print(ben_tuple)
print(type(ben_tuple))

empty_tuple = ()
print(type(empty_tuple))
print(tuple())

my_tuple = ("solar")
print(my_tuple, type(my_tuple),sep=("\n"))

x = 1,2,3
print(x)
print(type(x))

x = (1)
y = 1
z = 1,
a = 1,2,3
print(type(x))
print(type(y))
print(type(z))
print(type(a))


x = (range(1,11))
print(tuple(x))

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))

print(mix_tuple[-1][1])


sehirler = ["tokyo","addis ababa","rome","istanbul","rio"]

print(sehirler)

print(sorted(sehirler))

print(sorted(sehirler, key = len, reverse=True))
print(sorted(sehirler, key = len, reverse=False))
"""

x = ([1,2,3], 6,8,22)

x[0][1] = 66
print(type(x))
print(type(x[0][1]))
print(type(x[0]))
print(x)

import sys

x = [1,2,3]
y = 1,2,3

print(sys.getsizeof(x))
print(sys.getsizeof(y))

word = "happy"

x = tuple(word)
print(x)

benim = ["a","b","c"]
ben_tuple = tuple(benim)
print(ben_tuple)
print(type(benim))

x = 1, 2, 3
print(type(x))

x = "a","b","c"
print(type(x[0]))
print(type(x))


x = 1
print(x)
x = 1,
print(x)


x = tuple(range(1,11))
print(x)
print(type(x))


college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))




    
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_freq_num = max(set(numbers), key = numbers.count)
frequency = numbers.count(most_freq_num)
print("the most frequent number is {} and it was {} times repeated".format(most_freq_num, frequency)) 









