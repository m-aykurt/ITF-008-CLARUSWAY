# -*- coding: utf-8 -*-

answer = 43

question = 'What number am I thinking of?  '
print ("Let's play the guessing game!")

while True:
    guess = int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        print('Are you a MINDREADER!!!')
        break

"""
for i in {'n1' : 'one', 'n2' : 'two'} : print(i)

iterable = [1, 2, 3, 4]

for x in iterable:
    print(x**2 , sep= "\n")
   """ 
# n = int(input('enter a number between 1-10'))

# for i in range(11):
#    print('{}x{} = '.format(n, i), n*i)

#n = int(input("enter a name 1-20: "))

# for i in range(1,21):  # -this code is modulus 
 #   print(f"{n} % {i} = {n%i} ")

"""
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')
total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")
    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")

"""
"""


saved_amount = int(input("Please enter your saved amount: "))
ps4_price = 400
if (saved_amount < (ps4_price/2)):
    print("You must save more, keep saving!")
elif ((ps4_price/2) <= saved_amount < ps4_price):
    print("You saved more than half, keep saving!")
else:
    print("Yippee! You can buy your PS4")

math_mark = int(input("Please enter the mark: "))

if (84< math_mark <= 100):
    print("A (Excellent)")
elif (70< math_mark <= 84):
    print("B (Good)")
elif (60< math_mark <= 70):
    print("C (Medium)")
elif (45< math_mark <= 60):
    print("D (Not Bad)")
elif (0<= math_mark <= 45):
    print("F (Failed)")    
else:
    print("your mark is wrong")
"""
"""
a=998
if a >= 999 :
    print(a ** 0)  

else :
    print(a * 2)

x = int(input("Please enter a number: "))

y = 0

while y < x:
    print(y**2)
    y += 1
"""

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
    print(f"The type of {i} is {type(i)}")









