# -*- coding: utf-8 -*-

def freq(str):

    sozluk = {}
    for i in str:
        if i in sozluk:
            sozluk[i] += 1
        else:
            sozluk[i] = 1

    for i in str:
 
        if sozluk[i] != 0 and i != " ":
            print("{}:{}".format(i,sozluk[i]), end =" ")
            sozluk[i] = 0
            
freq("merhaba ben murat")