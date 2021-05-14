# -*- coding: utf-8 -*-
"""
a="123 poıu-.şis"
b= [a]
print(b)
print(type(b))

country = ["usa","brasil","germany"]
print(country)

print(len([1]))

xx = [[1],[2,3,"cc"]]
print(len(xx))


text = "2020's hard"

a = list(text)
b = [text]

print(a)
print(b)

numbers = [1,4,7]
numbers.append(9)
numbers.append("9")
numbers.insert(1, 11)
print(numbers)

cc = []
cc.append(11)
cc.append(11)

print(cc)

city = ["new york","london","istanbul","seoul","sydney"]
city.append("addis ababa")

print(city)

empty_list = []

empty_list.append(1)
empty_list.append(2)

empty_list.append(3)

empty_list.append(4)

print(empty_list)



city = ["los","beirut","tokyo","berlin"]
city[0] = True
city[1:] = "istanbul"
city[1:] = "istanbul","seul"
city[1:] = "33","55"

print(city)

city1 = ["istanbul","yozgat","erzurum","ankara"]
city1[0:2] = ("a","b")
city1[0:2] = ["abc"]
print(city1)

print("\\\\")
print("\\"*2)

a = 3
b = 4

print(f"{a} + {b}'ün toplamı {a+b}")

text = "{:.2f} , {:.3f} , {:.4f}".format(3.1463,5.367,72.4566)

print(text)


text = "{2:.2s} - {2:.3s} - {2:.4s}".format("3.1463","5.367","72.4566")


print(text)

text = "{:<20}".format("clarusway")
text2 = ")"
print(text+text2)
print(len(text))

text = "{:^20}".format("test")
text2 = "klm"
print(text+text2)


text = "{:10.3}".format("hipopotamus")
print(text)

text = "{:>10.3}".format("hipopatmus")
print(text)

text = "{:.6}".format("3.145676574")
print(text)

"""

list_1 = ["h","a","p","p","y"]
word = "happy"
list_2 = list(word)
print(list_1)
print(list_2 )


list_1 = [235]
list_2 = list(list_1)

print(list_2)

print(list_1)
print(type(list_1))


word = "happy"

new = [word]
print(new)


striking_1 = "i quit smoking"
new_list_1 = list(striking_1)
new_list_2 = [striking_1]

print(new_list_1)
print(new_list_2)

my_list = ["joseph","clarusway",2020]
my_list2 = ["josephclarusway2020"]
new_list1 = list(my_list)
new_list2 = [my_list]
new_list3 = list(my_list2)
new_list4 = list("murat")
print(new_list1)
print(len(new_list1))
print(new_list2)
print(len(new_list2))
print(new_list3)
print(new_list4)


xx = {2,3,"clarusway"}
print(xx)
print(type(xx))
print(len(xx))

x = "2020's hard"
y = list(x)
z = [x]
print(y)
print(z)

[]
list()

x = list()
y = []

print(x)
print(type(x))
print(y)
print(type(y))


numbers = [1,4,7]
numbers.append(9)
numbers.append(5)
numbers.insert(2,2)


print(numbers)



city = ["los angeles","beirut","tokyo"]

city[0] = True
city[1:] = "istanbul","seoul"

print(city)

city1 = ["istanbul","yozgat","erzurum","ankara"]

city1[0:2] = ["abcd"]
print(city1)

print("\\\\\\")

a = 3
b = 4
print("{}+{}'ün toplamı {}'dir".format(a,b,a+b))

text = "{:.2f}, {:.3f}, {:.4f}".format(3.1463542,51.62562652,723.5252678900)
print(text)

text = "{:.5s} - {:.7s} - {:.9s}".format("3.1463542","51.62562652","723.5252678900")
print(text)

text = "{:>20}".format("clarusway")

text ="clarusway"

print(text.center(20,"-"))
print(text.ljust(20,"-"))
print(text.rjust(20,"-"))


text = "{:10.5}".format("hipopotamus")
text = "{:>70.5}".format("hipopotamus")

a = ")"
print(text+a)


print(0xA + 0xB + 0xC),


str1 = "hello"
str2 = ","
str3 = "world"
print(str1[-1:])
str1 = "world"
print(r"\nhello")
print("new" "line" "end" 3)


