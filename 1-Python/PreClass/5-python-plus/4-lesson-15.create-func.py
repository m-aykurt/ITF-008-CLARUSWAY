# -*- coding: utf-8 -*-

# filter fonks.

def filterVowels(letter): # önce fonks.
    vowels = ["a","e","i","o","u"]
    if letter in vowels:
        return True
    else:
        return False

print(filterVowels("b"))

sentence = "the clarusway is the best"
filtered_vowels = filter(filterVowels, sentence)

print(*filtered_vowels)

# absolute fonks.

def absolute(a):
    """the function return absolute value""" # ürettiğimiz fonksyiona acıklama girebiliriz.
    if a >= 0:
        return a
    else:
        return (-a)

print(absolute(-6))
print(absolute.__doc__)
print("-------------------------------------------------------")


def texter(c,a,b):
    return f"{c} {a} {b}"

print(texter("i", "love", "you"))

def texter(text1,text2,text3):
    print(f"{text2} {text3} {text1}")

texter("merhaba", "dunya", "hello")
texter(text1="murat", text2 = "my name ", text3 = "is " )

def func(x = "ali ",y=11):
    return x * y
print(func())
print(func(x = "mehmet ", y=3))
print(func(y = 2, x = "hasan "))
print(func(y =3))

def default(a="ali",b=33):
        print(a,"is",b,"years old")
        
default("mehmet", 55)

def default(x, a="ali", b=33):
        print(x,a,"is",b,"years old")

default("hasan")


def parrot(voltage, state="a stiff", action="voom", typed="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", typed)
    print("-- It's", state, "!")
    
parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000000, action="VOOOOOOOMMM")
parrot(action="VOOOOOOOOOOOMMMMMM",voltage= 10000000000)
parrot(10000000000,"222222222222",333333333)
parrot("a thousand",state = "pushing up the dasises")
parrot(5000000000, typed=3333333333)

"""
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""
# def argu(a,b="dunya",c,d="saturn"): # hatalı kullanım-- önce positionallar gelmeli ardından defaultlar keyword arg. geliyor
 #  print(a,b,c,d)
    
def argu(a,c,b="dunya",d="saturn"): 
    print(a,b,c,d)
    
argu("uranus", "jupiter")
# argu("uranus",a="dunya", c="saturn")  fonksiyonu çağırırken değişkene 2 defa değer atanamaz.


# *args

def fruiterer(*fruit) : # * kullandıktan sonra sınırsız sayıda value girilebiliyor
    print("I want to get :")
    for i in fruit :
        print('-', i)
fruiterer('orange', 'banana', 'melon', 'ananas')

fruiterer("melon")

def slicer(*list1):
    even = []
    odd = []
    for i in list1:
        if i %2 ==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)            
    print(odd)
            
slicer(2,3,4,5,6,7)

# joseph hoca çözümü

def slicer(*num) :
    print("evens :", [i for i in num if i%2 == 0])
    print("odd :", [i for i in num if i%2 != 0])
slicer(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def organizer(**people):
    names = []
    ages = []
    for key,value in people.items():
        names.append(key)
        ages.append(value)
    print(names,ages,sep=("\n"))
    
organizer(ahmet = 35,mehmet=42,veli=12,hasan=18)

        
