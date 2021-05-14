# -*- coding: utf-8 -*-

# mors alfabesi çözümü
"""
mors= {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


word = input("enter a message: ").upper()
    
my_space = ""

for i in word:
    if i != " ":
        my_space += mors[i]  + " " 
    else:
        my_space += " "

print(my_space)

"""
# Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: 
"""  
a=input("Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`:")
b=[]
c=("{[()]}")
left=set("{[(")
dict={"(" : ")", "[" : "]", "{" : "}"}
stack=[]
for i in a:
    if i in c:
        b.append(i)
print(b)

for i in b:
    if i in left:
        stack.append(i)
    elif stack and i == dict[stack[-1]]:
            stack.pop()
    else:
        print(False)
if stack==[]:
    print(True)

# joseph hoca çözüm

s = "{[[()]]}"

def is_valid(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]","").replace("{}","")
    return s == ""
print(is_valid("{[]}"))
print(is_valid("{[[]}{"))
"""    
# max profit 
"""
def buy_and_sell(arr):
    max_profit = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            buy_price, sell_price = arr[i], arr[j]
            max_profit = max(max_profit, sell_price - buy_price)
    return max_profit

print(buy_and_sell([1,15,30]))
"""
"""
def parrot_trouble(talking,hour):
    if 0<hour<24:
        if talking == True and (hour<6 or hour>21):
            return True
        else:
            return False
    else:
        return f"your hour value is wrong, enter hour 0-23"
    
print(parrot_trouble(True, 15))
print(parrot_trouble(True, 32))
"""
liste = []
for i in range(24):
    liste.append(i**2)
    
print(liste)