# -*- coding: utf-8 -*-

isimler = ["ahmet","ali","çınar","deniz"]
string = "hello 1234 world"
yillar = [1983,1999,2008,1956,1986]
dereceler = [20,5,15,-2,0,-6]

sonuc = [i for i in range(101) if i%12==0]
print(sonuc)

sonuc = [i.lower()[::-1] for i in isimler]
print(sonuc)

sonuc = [i for i in string if i.isdigit()]
print(sonuc)

sonuc = [2021-i for i in yillar]
print(sonuc)

sonuc = [i if i>0 else "BUZLANMA" for i in dereceler]
print(sonuc)



number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x:x>=6, number_list))  
print(result)

print((lambda x: x**3)(5))
multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))