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

for letter in word:
    if letter != " ":
        my_space += mors[letter] # + " " -------- harfler arasına boşluk istersek
    else:
        my_space += " "

print(my_space)
"""

# Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: 
    
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


