# -*- coding: utf-8 -*-

"""
x = ["false", 0, True] # all - any
y = [] 
z = [0,()]
print(all(y))

x = list(filter(lambda x: x%2==0, range(5))) # filtreleme
print(x)

x = enumerate(range(5),10) # numaralandırma
print(*x)


def calculator(a,b,opr):
    if opr == "+":
        print(a+b)
    elif opr == "-":
        print(a-b)
    elif opr == "/":
        print(a/b)
    elif opr == "*":
        print(a*b)
    else:
        print("hatalı islem girdiniz.")
    
calculator(3, 5, "*")

while True :
    number = input("enter a positive number.")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break
"""

def filtervowels(word):
    vowel = ["a","e","i","u","o"]
    if word.lower() in vowel:
        return True
    else:
        return False
    
def vowels1(word):
    vowel = ["a","e","i","u","o"]
    if word.lower() not in vowel:
        return True
    else:
        return False

sentence = "the claruısway is the best"
filtered_vowels = filter(filtervowels,sentence)
print(*filtered_vowels)


filter_v = filter(vowels1, sentence)
print(*filter_v)


