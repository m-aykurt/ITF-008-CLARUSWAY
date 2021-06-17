# -*- coding: utf-8 -*-
"""
x = range(1,11)
my_list = list(x)
my_list.sort(reverse=True)
print(my_list)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

print(grocer[1][1][1::2])

print("My two favorite flowers are {flowers[1][2]} and {flowers[1][1][1]}, two favorite colors are {colors[1][1]} and {colors[1][1][2]}.")

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for i in words:    
    if i[-1] == 'e':
        past_tense.append(words[i] + 'd')
    else:
        past_tense.append(words[i] + 'ed')
        
"""

dict_by_dict = {'animal': 'dog',
               'planet': 'neptun',
               'number': 40,
               'pi': 3.14,
               'is_good': True,
               'is_bad': False}

del dict_by_dict['animal']

print(dict_by_dict) 


school_records={
    "personal_info":
        {"kid":{"tom": {"class":"intermediate", "age":10},
                "sue": {"class":"elementary", "age":8}
               },
         "teen":{"joseph":{"class":"college", "age":19},
                 "marry":{"class":"high school", "age":16}
               },               
        },
}

print(school_records['personal_info']['teen']['marry']["class"])

print(len(set('listen to the voice of enlisted')))
print(set('listen to the voice of enlisted'))

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

most_freq_num = max(set(numbers), key = numbers.count)

frequency = numbers.count(most_freq_num)

print("the most frequent number is {} and it was {} times repeated".format(most_freq_num, frequency))

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
profit = (sales["sell_value"]-sales["cost_value"])*sales["inventory"]

print(round(profit))

x = 3


flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1>0 :
    print(flowers[:])
    count1 -= 1
    count2 += 1
    
for i in {'n1' : 'one', 'n2' : 'two'} : print(i) 

num = input("Please enter a positive integer number : ")

if num.isdigit() :

    a = num.split()

    b=0

    for i in range(len(a[0])) :

        b+=int(a[0][i])**len(a[0])

    if b==int(num):

        print(num, "is an Armstrong number")

    else:

        print(num, "is not an Armstrong number")

else:

    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
    
    
num=int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")