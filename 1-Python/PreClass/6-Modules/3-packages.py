# -*- coding: utf-8 -*-

from upper_packages.my_package_1 import my_module_1,my_module_2
from upper_packages.my_package_2 import my_module_3,my_module_4

print(dir(my_module_1))

print(my_module_2.divide(10,5))
print(my_module_1.addition(4,5))
print(my_module_3.repeater("clarusway ",3))
print(my_module_4.sqroot(36))

import upper_packages
print(dir(upper_packages))

from upper_packages.my_package_1.my_module_1 import addition
print(addition(3,5))

from upper_packages.my_package_1.my_module_2 import hello
print(hello())

# syntax error

# hatalı bir yazımda verilen hatadır. kod cevrilmeden önce hata mesajı gelir
"""
print("a')
"""

# exceptions 

# type error

"""
------ tipleri yanlışı (str-int gibi)--------
a = "a"
b= 3

print(a+b) # type error -exceptions

"""

# value error

"""
-----genellikle fonksyionları yanlış değer (value) vermekle olur------

print(int("ten")) # value error

import math 
print(math.sqrt(-25)) # - değerlerin karekökü olmaz yani value error verir

"""

# name error 

"""

------ print daha önce calıstığı için a variable  tanımlanmadığını söylüyor
printt() --- yanlış isimli fonksiyon 
print(a)
a = "a"

"""

# ------------------ Exception Handling -----------------

# zero division error

# print(4/0)
"""
while True:
    a = int(input("ilk sayi: "))
    b= int(input("ikinci sayi: "))
    try:
        c = a/b
        print(c)
        break
    except:
      print("bir seyler ters gitti")
"""
# sınırlı exception

"""
while True:
    a = int(input("ilk sayi: "))
    b= int(input("ikinci sayi: "))
    try:
        c = a/b
        print(c)
        break
    except ZeroDivisionError:
        print("Sıfıra bölünmeme kuralını hatırla")
    except:
        print("birşeyler ters gitti")
"""
# finally kullanımı

try:
    print("4"+"4")
except TypeError:
    print("type hatası var.tipi kontrol et")
else:
    print("aa demek ki exception yükselmemiş.")
finally:
    print("sonunda sıra bana geldi")
    
    
    
# exception --e-- kullanımı

try:
    print("4"+4)
except Exception as e:
    print("type hatası var.tipi kontrol et",e)
else:
    print("aa demek ki exception yükselmemiş.")
finally:
    print("sonunda sıra bana geldi")

# 

try:
    print("4"+4)
except Exception as e:
    print("type hatası var.tipi kontrol et.................",e)
    print(type(e))
else:
    print("aa demek ki exception yükselmemiş.")
finally:
    print("sonunda sıra bana geldi")
    
    # örnek 1    
"""   

while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")
"""       
        
        # örnek-2
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two  # normal part of the program
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")  # executes when division by zero
    except Exception as e:
        print(e)
    else:
        print("The result of the division is : ", division)  # executes if there is no exception
    finally:
        print("Thanks for using our mini divison calculator! Come again!")
        break  # exits the while loop