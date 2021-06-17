# -*- coding: utf-8 -*-
import csv

with open("fruits.csv") as cs:
    print(cs.read())


with open("fruits.csv", 'r', encoding="utf-8") as file:
    print(file.read())


import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows: 
        print(row) 

a=10
globals()['a']=25
print(a)