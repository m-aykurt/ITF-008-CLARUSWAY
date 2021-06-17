# -*- coding: utf-8 -*-

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""
def kare_al(num):
    st = str(num)
    new_st = ""
    for i in st:
        new_st += str(int(i)**2)
    return int(new_st)
print(kare_al(9119))

# 2 nci çözüm

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
"""

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
"""
def isogram(string):
    s= string.lower()
    j = 0
    while j<len(s):
        if len(s)==0 or s =="":
            return True
        elif s.count(i)>1:
            return False
        elif s.count(i)<=1:
            return True
print(isogram("bollka"))
"""
l = ('AAAABBBCCDAABBB')
def l(l):
    new_l = []
    for i in list(l):
        if new_l.count(i)<1:
            new_l.append(i)
        elif new_l.count(i)>1:
            pass
    return new_l
print(l(('AAAABBBCCDAABBB')))

def itr(l):
    for i in list(l):
        a=l.split("i")
    return a
print(itr(('AAAABBBCCDAABBB')))
