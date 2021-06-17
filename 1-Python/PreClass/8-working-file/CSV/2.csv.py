# -*- coding: utf-8 -*-

with open("fruits.csv","r",encoding="utf-8") as file:
    print(file.read())
    file.seek(0)
    print(file.readlines())

import pandas

print(dir(pandas))

print(pandas.read_csv("fruits.csv"))


with open('fruits.csv', 'w', encoding = 'utf-8') as file:
    file.write('no,fruit,amount,\n1,Banana,4 lb,\n2,Orange,5 lb,\n3,Apple,2 lb,\n4,Strawberry,6 lb,\n5,Cherry,3 lb)\n')
with open('fruits.csv', 'r', encoding = 'utf-8') as file:
    print(file.read())
    
import csv

with open("fruits.csv","r",encoding="utf-8") as file:
    csv_rows = csv.reader(file, delimiter=":")
    print(file.read())
    
    

import pandas as pd

print(pd.read_csv("1.csv"))
print(pd.read_csv("titanic.csv"))
titanic = pd.read_csv("titanic.csv")
print(titanic[titanic["Survived"]==0])
print(titanic[titanic["Fare"]>1000])
bayanlar = titanic[titanic["Sex"]=="Female"]
bayanlar.to_csv("titanic_bayanlar.csv")

titanic.groupby("Sex")["Survived"].mean()

titanic_vefat = titanic[titanic["Survived"]=0]

vefat = pd.read_csv("titanic_vefat.csv")
print(vefat)