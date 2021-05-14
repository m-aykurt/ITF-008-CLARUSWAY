# -*- coding: utf-8 -*-

numb = int(input("enter a integer value : "))

fact = 1
process = list(range(1, numb+1))

for i in process:
    fact *= i
print(fact)



