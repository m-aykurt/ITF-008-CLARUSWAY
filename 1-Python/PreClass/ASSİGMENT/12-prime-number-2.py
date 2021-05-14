# -*- coding: utf-8 -*-

# prime numb append list

limit = int(input("enter a limit number"))
prime_numb = []
for num in range(2,limit+1):
    for b in range(2,num):
        if num%b==0:
            break
    else:
        prime_numb.append(num)
print(prime_numb)