# -*- coding: utf-8 -*-

print(all("merhaba"))
print(any("merhaba"))
print(*enumerate("merhaba"))
print(*zip("merhaba","hello"))
print(frozenset("merhaba 12"))

"""
def fib(n):
    a,b = 0,1
    while a < n:
        a,b = b, a+b
        print(a,end=(""))     
fib(100)
"""

def my_function(a,b):
    area = a*b
    return area
    
print(my_function(3,2))


