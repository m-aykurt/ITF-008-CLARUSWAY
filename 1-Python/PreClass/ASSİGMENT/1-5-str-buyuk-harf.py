# -*- coding: utf-8 -*-

test = "iki kelime"
list_second = []
for i in range(len(test)): # 0 dan test uzunluğuna kadar iterable değerlerin tamamını gez
    if test[i].isalpha(): # test in i'nci indeksi harf ise 
        list_second.append(test[:i]+test[i].upper()+test[i+1:])

print(list_second)