# -*- coding: utf-8 -*-
"""
while 0:
    print("bir")
print("outside while")

number = 0
while number<6:
    print(number)
    number +=1
print("now")


number = 0
while number<6:
    print(number)
    number +=2
print("now")
"""

# yaşı doğru girdiren bir kod.
""" 
age = input("Enter your age : ")
while not age.isdigit() :
    print("You entered incorrectly!")
    age = input("Enter your age correctly please : ")
    
print("Great! You entered valid age :", age)
"""

# sayı tahmin oyunu
""" 

answer = 66

while True:
    numb = int(input("bir sayi giriniz: "))
    if numb < answer:
        print("little up")
    elif numb >answer:
        print("little down")
    else:
        print(f"you are mindreader correct {numb}")
        break
"""

# the most frequent number

numbers = [-1,3,7,4,3,0,6,6,6,6,6,6,6,6,6,3,16,3,7,0,0,1]
sequence = [1,1,1,1,2,2,2,3,3,4]
# print(max(sequence))
# print(sequence.count(1))
# print(sequence.count(2))

frequent = max(numbers, key = numbers.count)
print(frequent, numbers.count(frequent))

print(numbers.count(max(numbers, key=numbers.count)))


# empty = []
# print(max(empty,default="bos"))



i = 1
while i<=100:
    i +=1   

    if (i%2==1):
        print("tek sayi: ",i)
    else:
        print("cift sayi",i)
        
username = ""
while not username:
    username = input("kullanıcı adınız: ")

print("girilen kullanıcı adı: ",username)
