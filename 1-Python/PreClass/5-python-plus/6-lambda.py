# -*- coding: utf-8 -*-
# fazladan argüman tanımlamak için  (*args)
def brothers(bro1, bro2, bro3):
    print("here are the names of the brothers")
    print(bro1, bro2, bro3,sep=("\n"))
family = ["tom","sue","tim"]
brothers(*family)
brothers(family,family,family)


genius = ["bill","rossum","guido van","gates"]

def merger(par1,par2,par3,par4):
    print(f"for me, {par1} {par4} and {par3} {par2} are geniuses")
    
merger(*genius)

#kwargs ile yapılan

dict_couple = {"bride": ["mary","bella","linda"],
               "groom": ["rye","fred","roland"]}

def couples(bride,groom):
    couple_list = []
    for i in zip(bride,groom):
        couple_list.append(i)
    return couple_list
print(couples(**dict_couple))

def couples(bride,groom):
    return [x for x in zip(bride,groom)]

couples(**dict_couple)

friend = {"names":["yakup","mali","burak","turgut"],
           "ages": [29,30,31,33]}
friend1 = {"ayşe":25,"murat":32,"hasan":33}

def friends(names,ages):
    friends_l = []
    for i in zip(names,ages):
        friends_l.append(i)
    return friends_l


print(friends(**friend))
print(friends(["murat","selin"], [30,29]))

friend = {"ayse":25,"murat":32,"hasan":33}

def meaner(ayse,murat,hasan):
    average = (ayse + murat + hasan)/3
    return average

print(meaner(**friend))

#### LAMBDA

#1

numb = [1,3,66,72,3,23,54,21,20]
lambda x: "odd" if x%2 != 0 else "even"

print((lambda x: "odd" if x%2 != 0 else "even")(5))
print((lambda x: "odd" if x%2 != 0 else "even")(6))

#2

x = "clarusway"
reverser = (lambda x: x[::-1])(x)
print(reverser)

#3

numb = [1,3,66,72,3,23,54,21,20]

for i in numb:
    print(i, ":", (lambda x: "odd" if x%2!=0 else "even")(i))

#4 hipotenus

hipo = (lambda x,y: x**2 + y**2)
print(hipo(3, 4))

#5 reverser 

reverser = lambda x:x[::-1]

print(reverser("clarusway"))

# MAP Fonks.

iterable = [1,2,3,4,5,6]

result = map(lambda x: x**2, iterable)
print(list(result))
print(*map(lambda x: x**2, iterable))
print(type(result))
print(type(list(result)))

def kare_al(x):
    return x**2
result = map(kare_al, iterable)
print(*result)

iterable_2 = ["ahmet","mehmet ve abisi","hasan hüseyin"]
result_2 = map(len, iterable_2)
print(*result_2)

# birden fazla iterable kullanılabilir

letter1 = ["o","s","t","t"]
letter2 = ["n","i","e","w"]
letter3 = ["e","x","n","o"]

numbers = map(lambda x,y,z: x+y+z, letter1, letter2, letter3)
print(list(numbers))

yapistir = map(zip, letter1,letter2,letter3)

for i in yapistir:
    for j in i:
        print(j)
        
        
number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: True if x%2 !=0 else False, number_list))
print(result)


words1 =["you","much","hard"]
words2 =["i","love","he"]
words3 =["love","ate","works"]

sonuc = list(map(lambda x,y,z: x + " "+y+" "+z, words2,words1,words3))

print(sonuc)


### FİLTER FONKS.

words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

sonuc = filter(lambda x: len(x)<5, words)
sonuc = filter(lambda x: len(x)>=5, words)

print(list(sonuc))



# first_ten = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# sonuc = filter(lambda x: True if x in first_ten, first_ten)

# print(list(sonuc))

# üs alma

def modular_function(n):
    return lambda x: x ** n
power_of_2 = modular_function(2)  # first sub-function derived from def
power_of_3 = modular_function(3)  # second sub-function derived from def
power_of_4 = modular_function(4)  # third sub-function derived from def
print(power_of_2(2))  # 2 to the power of 2
print(power_of_3(2))  # 2 to the power of 3
print(power_of_4(2))  # 2 to the power of 4


# repeater

def repeater(n):
    return lambda x: x * n
repeat_2_times = repeater(2)  # repeats 2 times
repeat_3_times = repeater(3)  # repeats 3 times
repeat_4_times = repeater(4)  # repeats 4 times
print(repeat_2_times('alex '))
print(repeat_3_times('lara '))
print(repeat_4_times('linda '))

# Emoji tanımlama

def functioner(n):
    return lambda x:f"{x} {n}"
smile = functioner(":)")
sad = functioner(":(")
neutral = functioner(":|")
print(smile("hello"))
print(sad("merhaba"))
print(neutral("hello"))
print(smile([1,2,3]))

# joseph hoca çözümü 

def functioner(emoji = None):
    return lambda message: print(message, emoji)
(lambda message: print(message, ":)"))(66)
(lambda message: print(message, ":)"))([66])
print_smile = functioner(":)")
print_sad = functioner(":(")
print_neutral = functioner(":|")
print(print_smile("Hello"))
print(print_sad("bugünkü dersteki yüz ifadem -->"))
print(print_neutral("Hello"))

def func_gen(func_name):
    return lambda x : func_name(x)

murat_print = func_gen(print)
murat_max = func_gen(max)
murat_bool = func_gen(bool)
murat_sorted = func_gen(sorted)

print(murat_sorted([12,15,1,2,376,9]))

num1 = [9,6,7,4]
num2 = [3,6,5,8]

sonuc = map(lambda x1,x2: (x1+x2)/2, num1,num2)
print(list(sonuc))



letter1 = ["o","s","t","t"]
letter2 = ["n","i","e","w"]
letter3 = ["e","x","n","o"]

sonuc = map(lambda x1,x2,x3: x1+""+x2+""+x3, letter1,letter2,letter3)

print(list(sonuc))

words1 =["you","much","hard"]
words2 =["i","love","he"]
words3 =["love","ate","works"]

sonuc = map(lambda x1,x2,x3:x1+" "+x2+" "+x3, words2,words3,words1)

for i in sonuc:
    print(i)
print(list(sonuc))

words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

sonuc = filter(lambda x: len(x)<5, words)
print(list(sonuc))

first_ten = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
vowel = ["a","e","i","u","o"]
sonuc = filter(lambda x: x in vowel, first_ten)

print(list(sonuc))

def functioner(emoji=None):
    return lambda message: print(message, emoji)
 
(lambda message: print(message, ":)"))(66)
(lambda message: print(message, ":)"))([66])

print_smile = functioner(":)")
print_sad = functioner(":(")
print_neutral = functioner(":|")
print(print_smile("Hello"))
print(print_sad("bugünkü dersteki yüz ifadem -->"))
print(print_neutral("Hello"))


def func_gen(func_name):
    return lambda x: func_name(x)
murat_print=func_gen(print)
murat_max = func_gen(max)
murat_bool= func_gen(bool)
murat_sorted = func_gen(sorted)

print(murat_print("merhaba dünya"))
print(murat_max([22,1,67,8112]))
print(murat_bool("22"))
print(murat_bool(0))
print(murat_sorted([1,22,2,3,4,5,6,78,90]))
    