# -*- coding: utf-8 -*-

# 1 
"""
a = "Python"
b = "Workshop"
c = "-1"

print(f"{a} {b}{c}")
"""
# 2
"""
weight = float(input("kilonuz : "))
height = float(input("boyunuz : "))

bodyMassIndex = weight / (height ** 2)

print(bodyMassIndex)

# 3
"""
"""
budget = 200
piece = 11

result = budget // piece
result = budget % piece

print(result)
"""
# 4

"""
sayi1 = int(input("sayi 1 : "))
sayi2 = int(input("sayi 2 : "))

sayi1,sayi2 = sayi2,sayi1


print(sayi1,sayi2)

# 5

x = 2 
y = 3

solving = (x-y) * (x+y)
print(solving)
"""
"""
# 6----?

word = input("kelimeniz: ")
seperator = input("kelimeler ne ile ayrılsın: ")
repetition = int(input("kac defa yazdırılsın: "))

# result = (((word) * (repetition)), sep = seperator)

print(result)




# 7  print(True and False and (not True and False) and not (True or False))print(True and False and not "False" and None and ("None" or None))

# 8 print(True and False and not "False" and None and ("None" or None))
# 9 print("clarusway" and 0 and not "" and False and (" " or None))
"""


word = input("kelimeniz: ")

rep = int(input("kac defa yazdırılsın: "))

result = (*(word) * (rep), sep="-")

print(result)


