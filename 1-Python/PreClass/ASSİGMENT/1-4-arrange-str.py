# -*- coding: utf-8 -*-

str1 = "PyNaTive"

lower = ""
upper = ""

for i in str1:
    if i.islower():
        lower += i
    else:
        upper += i
print(lower+upper)

