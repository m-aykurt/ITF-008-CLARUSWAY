# -*- coding: utf-8 -*-

#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
"""
list1= []
for i in range(1500,2701):
    if i % 35 == 0 :
        list1.append(i)
print(list1)
"""
# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
"""
fahr = float(input("enter a fahrenait: "))

celc = (fahr - 32) / 1.8
print(f"[{fahr} is {celc}")
"""
# Write a Python program to guess a number between 1 to 9.
"""
x = 26

while True:
    guess = int(input("guess a number from 1 to 100:  "))

    if guess>x:
        print("no, this number is high, lets less")
    elif guess<x:
        print("lets upper")
    else:
        print("You are mindreader...")
        break
 """   
# Write a Python program to construct the following pattern, using a nested for loop.
"""
how_many = int(input("kac defa * yazalım: "))
x = "*"

for i in range(how_many):
    print(i*x)
for i in range(how_many, 0,-1):
    print(i*x)
"""

# Write a Python program that prints each item and its corresponding type from the following list.
"""
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(i , type(i))
    
# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for x in range(15):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
numb_list = []
count = 0
num1 =0
num2 =1

while num2 < 50:
    count = num1+num2
    num1 =num2
    num2 = count
    numb_list.append(num2)
print(numb_list)
# kolay yöntem

x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y


# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,51):
    if i%3 ==0 and i %5 ==0:
        print("FizBuzz")
        continue
    elif i%3 == 0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
        continue
"""
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
"""
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

"""
x = int(input("Input number of rows: "))
y = int(input("Input number of columns: "))
for i in range(x):
    for ii in range(5):
        print(i*ii,sep=(" "),end=(" "))
        

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
"""

# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)
"""
lines = []

while True:
    l = input("enter a lines: ")
    if l:
        lines.append(l.upper())
    else:
        break
print(lines)

for l in lines:
    print(l)
"""
# 14. Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
"""
x = input("bir değer giriniz: ")

x1 = tuple(x)
letters = []
numbers = []

for i in x1:
    if i.isalpha():
        letters.append(i)
    elif i.isdigit():
        numbers.append(i)
    else:
        pass
print(f"letters length is {len(letters)}")
print(f"numbers length is {len(numbers)}")
"""

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence. Go to the editor
"""
list1 = []

for i in range(100,401):
    if i % 2==0:
        list1.append(i)
        
print(list1,sep=(","))
"""
# 31. Write a Python program to calculate a dog's age in dog's years. Go to the editor
"""
year = int(input("hangi yılın köpek yılını istiyorsunuz: "))

if year <0:
    print("year must be positive number")
    exit()
elif year<=2:
    d_age = year * 10.5
else:
    d_age = 21 + (year -2)*4
    
print("the dog's age in human years is",d_age)
"""
# 32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
"""
vowel = ["a","e","i","u","o"]

letter = input("bir harf giriniz: ")

if vowel.count(letter):
    print("your letter is vowel")
else:
    print("your letter is a consonant")
"""
# 33. Write a Python program to convert month name to a number of days. Go to the editor
"""
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ").title()

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 
"""

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor
"""
x = int(input("bir sayi giriniz: "))
y = int(input("diger sayiyi giriniz: "))
z = x+y
if 15<z<20:
    print(20)
else:
    print(z)
"""

#   In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

"""
def is_curzon(numb):
    if (2 ** numb + 1) % (2*numb+1) == 0 :
        return True
    else:
        return False
    

print(is_curzon(5))
print(is_curzon(5))
print(is_curzon(21))
print(is_curzon(10))
"""
"""

my_list = [*range(1,11)]
my_list.sort(reverse=True)
print(my_list)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

print(grocer[1][1][1::2])

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = "My two favorite flowers are {x1} and {x2}, two favorite colors are {x3} and {x4}.".format(x1=flowers[0][2],x2= flowers[0][1][1],x3=colors[1][0],x4=colors[1][1][1])
print(text)


escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]

sentence = "I am 40 years old. {x1}I have two children. {x2}Data Science is my IT domain.".format(x1="\n\t",x2= "\n\t\t",x3= ["\n", "\n\t\t"])

print(sentence)


def my_function(a,b):
    print(a*b)
    
my_function(10,20)

def myfunc1():
  x = "hi"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())

x = 'My name is Richard'
def my_function_1(): 
    x = 'My name is John'
    
print(x)
  
city = "I love Paris!"

def my_function(): 
    city = "I love London!"
    print(city) 

my_function()
"""

# 36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
"""
def triangle(a,b,c):
    if a==b==c:
        return "this triangle is equilateral"
    elif a==b or a==c or b==c:
        return "this triangle is isosceles triangle"
    else:
        return "this triangle is scaelene"
    
print(triangle(4,4, 2))
print(triangle(3, 4, 5))
"""
# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. Go to the editor
"""

month = input("Input the month (e.g. January, February etc.): ").title()
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)
"""
# 39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. Go to the editor

"""
kac_defa = int(input("kac defa sayi girmek istersiniz: "))
sayi_list = []
count = 0

while count < kac_defa:
    sayi_list.append(int(input("sayi giriniz: ")))
    count +=1
    sorted_list=sorted(sayi_list)
if kac_defa % 2 ==0:
    print((sorted_list[kac_defa//2-1]+sorted_list[kac_defa//2])/2)
else:
    print(sorted_list[kac_defa//2])
""" 
    
"""   
kac=int(input("Kaç kere girmek istersin "))
liste=[]
i=0
while i<kac:
  liste.append(float(input()))
  i+=1
liste.sort()
if kac%2:
  print(liste[kac//2])
else:
  print(liste[kac//2-1],liste[kac//2])
""" 

print(set("{[("))