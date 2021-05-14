# -*- coding: utf-8 -*-

def leap(year):
    if not year % 4 and year % 100 or not year % 400:
            return f"{year} is a leap year" 
    else:
        return f"{year} is not a leap year"
    
print(leap(2020))
print(leap(2000))
print(leap(2100))
print(leap(2500))