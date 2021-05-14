# -*- coding: utf-8 -*-

import math

print(math.factorial(3))
print(dir(math))

print(math.log10(1000))
print(math.pi)
print(math.factorial(4))

import string

print(string.punctuation)
print(string.digits)

print(dir(string))

import datetime

print(dir(datetime))
print(datetime.datetime.now().hour)
print("bugünün tarihi:",datetime.date.today())

print(datetime.datetime.now())

birth = datetime.date(571, 4, 22)
death = datetime.date(632, 6, 8)

sonuc = datetime.date.toordinal(death) - datetime.date.toordinal(birth)

print(sonuc/365)

import random
city = ["seoul","istanbul","roma","paris","cape town"]
print(random.choice(city))

