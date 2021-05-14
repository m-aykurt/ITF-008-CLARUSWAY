# -*- coding: utf-8 -*-
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
        
