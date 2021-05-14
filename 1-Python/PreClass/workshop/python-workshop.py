# -*- coding: utf-8 -*-

#1 Write a program that multiplies three numbers entered by the user. Print the output.

x1 = int(input("bir sayi giriniz: "))
x2 = int(input("bir sayi giriniz: "))
x3 = int(input("bir sayi giriniz: "))

carpim = (x1*x2*x3)
print(f"sayıların carpimi{carpim} dir.")

#2 Write a program that calculates body mass index from height and weight entered by the user.

weight = float(input("your weight: "))
height = float(input("your height: "))

bmi = (weight / (height **height))

print(f"your bmi is {bmi}")

#3 With your 200 usdollars, how many pieces of material can you get for $ 11 each? How much money do you have left after buying?

budget = 200

material = 11

how_many = budget // material
print(how_many)
left = budget % material
print(left)

#4 Ask the user for two numbers and assign these numbers to variables and replace the values of these variables with each other.

a = [].append("x")

x = int(input("bir sayi giriniz: "))
y = int(input("bir sayi giriniz: "))


print(a)

#5 Write a Python program to solve (x - y) * (x + y).

x = int(input("bir sayi giriniz: "))
y = int(input("bir sayi giriniz: "))


solving = (x**2) - (y**2)
print(solving)



x = "sarajevo"
y ="istanbul"
text = f"I live in {x.capitalize()} {y.upper()}."

print(text)

x = "i live in istanbul, merhaba dünya , merhaba herkese"

print(x.strip(""))


txt = "     banana     "

x = txt.strip()
y = "merhaba"
print(x,y)


sales = {

  "cost_value": 31.87,

  "sell_value": 45.00,

  "inventory": 1000

}  


price = (sales["sell_value"] - sales["cost_value"]) * sales["inventory"]

total_profit = "%.1f" %price

print(f"the profit will be {total_profit} dollars")

print(sales["sell_value"])
print(sales["inventory"])


worker1 = float(input("çalışanın alacağı ödemeyi yazınız: "))

worker2 = float(input("çalışanın alacağı ödemeyi yazınız: "))

worker3 = float(input("çalışanın alacağı ödemeyi yazınız: "))



payrolls = "%.2f" %worker1, "%.2f" %worker2, "%.2f" %worker3



print(f"the workers in company payrolls is here {payrolls}")



numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

most_freq_num = max(set(numbers), key = numbers.count)

frequency = numbers.count(most_freq_num)

print("the most frequent number is {} and it was {} times repeated".format(most_freq_num, frequency)) 





