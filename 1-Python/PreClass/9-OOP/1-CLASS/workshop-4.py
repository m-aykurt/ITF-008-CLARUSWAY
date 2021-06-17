# -*- coding: utf-8 -*-

"""
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
"""

# sudoku format değişimi
"""
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

count = 0
print("- - - - - - - - - - - - - - - ")
for i in sudoku:
    for j in range(9):
        print(i[j], " ", end="")
        if (j+1) == 9 : 
            print()
            count+=1
            if count%3==0 and count!=0 :
                print("- - - - - - - - - - - - - - - ")
        if (j+1) % 3 == 0 and j != 0 and j!=8: 
             print("| ", end="") 
"""
"""
x = [([1], [2, 3], [4,5,6])]
l = []
for i in x:
    for j in i:
      for k in j:
          l.append(k)
print(l)
"""

x = [([1], [2, 3], [4,5,6])]
result = [k for i in x for j in i for k in j]
print(result)    

x = [[1], [2, 3], [4,5,6]]
result= list(zip(x[0],x[1],x[2]))

yList = "selvi vahit ayşe".split()
yList

xList = "elma armut muz".split()
xList

result = []
for i in xList:
    for j in yList:
        result.append(i+j)
print(result)

print({i + j for i in xList for j in yList})

result = []
for i in range(4):
    if i %2 ==0:
        for j in ["bir","iki","üç"]:
            result.append(str(i)+"-->"+j)
print(result)

def equal(*num):
    numbers = list(num)
    result = max(numbers, key= numbers.count)
    sonuc = numbers.count(result)
    return f"{result}  {sonuc} defa tekrar etmiştir"

print(equal(5, 1, 1,1,1,2,2,2,22,2,2,2,22,2,2,2))

l = ["right 20","right 30","left 50","up 10","down 20"]
x=y=0
for i in l:
    if i.split()[0]=="right": x = x + int(i.split()[1])
    elif i.split()[0]=="left": x = x - int(i.split()[1])
    elif i.split()[0]=="up": y = y + int(i.split()[1])
    elif i.split()[0]=="down": y = x - int(i.split()[1])
print(x,y)


ops = {"+":(lambda x,y:x+y), "-":(lambda x,y:x-y), "/":(lambda x,y: x/y), "*": (lambda x,y:x*y)}

print(ops['+'](3*5))
    
    