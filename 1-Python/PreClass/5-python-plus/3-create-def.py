# -*- coding: utf-8 -*-

def ben(parametre1, parametre2):
    print(parametre1 + parametre2)
    
ben("parametre1 ", " parametre2") # burdaki parametrelere girdiğimiz değerler de argüman.

def multiply(a,b):
    print(a*b)

multiply("amazing ", 3)
multiply(3, -2)

def motto():
    print("dostlar beni hatırlasın,")
    
motto()

def add(a,b):
    print(a+b)
    
add(2, 5)


def calculator(a,b,c):
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "/":
        print(a/b)
    elif c =="*":
        print(a*b)
    else:
        print("you entered wrong operator...")
        
calculator(2, 3, "+")

print(type(print("hello"))) # non type
print(type(print(max(2, 3, 5))))


# return


def calculator(a,b,c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "/":
        return a/b
    elif c =="*":
        return a*b
    else:
        return "you entered wrong operator..."
    

# absolute

def absolute(a):
    return abs(a)

print(absolute(-22))



# joseph hoca çözümü

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