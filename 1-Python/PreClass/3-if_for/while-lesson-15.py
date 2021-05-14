# -*- coding: utf-8 -*-
# cümledeki kelimenin uzunluğunu bulan kod
"""
sentence = input("bir cümle giriniz: ").split()
uzunluk = []

i = 0
while (i<len(sentence)):
    uzunluk.append(len(sentence[i]))
    i+=1
    
print(max(uzunluk))

names = ["ahmed","aisha","adam","joseph","gabriel"]

for i in names:
    print(f"hello {i}")

list1= []
for i in range(1,6):
    list1.append(i)
print(list1)




course = "clarusway"

for i in course:
    print(i,end=("//"))

# verilen kelimeyi ayırıp aralarına işleyen kod
# join ile de kullanılabilir.

word = input("give me a word: ")
count = 0
for i in word:
    count +=1
    if count < len(word):
        i = i + "-"
        print(i,end=(""))
"""
"""
samanlık = ["yumurta","yaba","inek","iğne","saman","tezek","tırmık"]

print(samanlık.index("inek"))
print(samanlık.count("inek"))


v = ("five",5,True)
(x,y,z) = v

print(x,y,z)

a,b,c = 1,2,3

print(a,b,c)

(monday, tuesday, wednesday, thursday, friday, saturday, sunday) = list(range(1,8))

print(friday)
print(*range(1,5))

print([1,2,3,4])
print(type([1,2,3,4]))

print([1,2,3,4]+["11","22",33])

tt = (1,2,[1,3,5])
print(tt)
print(type(tt))

tt[2].append(4) # tuple ın list olan değerine ulaşıp ona işlem yapabiliyoruz
print(tt)


a, _, b, _ = (10,20,30,40)
print(a,b)

x, y, *z = (11,22,33,44,55,66,77,88)
print(x,y,z)
print(z)


x, y, *_ = (11,22,33,44,55,66,77,88)
print(x,y)


x, y, *z, t,x= (11,22,33,44,55,66,77,88)
print(t)
print(x,y,z,t,x)

user = {
        "name":"daniel",
        "surname":"smith",
        "age":"35"
        }
for i in user:
    print(i)

user = {
        "name":"daniel",
        "surname":"smith",
        "age":"35"
        }
for i in user.values():
    print(i)
    
    user = {
        "name":"daniel",
        "surname":"smith",
        "age":"35"
        }   
for a,b in user.items():
    print(a,b)
    
user = {
        "name":"daniel",
        "surname":"smith",
        "age":"35"
        }
for i in user.items():
    print(i)
print(type(i))


times = int(input("how many times should i say 'i love you'"))    

for i in range(times):
    print("i love you")
    
    

x = int(input("hangi sayıyı carpim tablosunda gösterelim: "))

for i in range(1,11):
    print(f"{i} * {x} = {i * x}")
"""
"""
print(*range(5))
print(*range(10,0,-2))

print(*range(10,-3,-2))

# ZİP fonksiyonu

text = ["one","two","three","four","five","six"]
numbers = [1,2,3,4,5,6,7]

for x,y in zip(text,numbers):
    print(x,":",y)
    
isimler = ["tarık","sevda","selim"]
yaslar = [11,22,33]

xx = zip(isimler,yaslar)
print(type(xx))

print(list(xx))


sentence = input("bir cümle giriniz: ").split()
uzunluk = []

i = 0
while (i<len(sentence)):
    uzunluk.append(len(sentence[i]))
    i+=1
    
print(max(uzunluk))


sentence = input("give me a sentence: ")
words = sentence.split()
i=0
longest = 0
while i<len(words):
    if len(words[i]) > longest:
        longest = len(words)
    i +=1
    
print(longest)
"""

print([1,2,3,4]+["11","22","33"])

tt = (1,2,[1,3,5])
tt[2].append(4)
print(tt)

(a,_,b,_)= (10,20,30,40)
print(a,b)










