# -*- coding: utf-8 -*-

# break kullanımı
"""
while True:
    isim = input("isim ('cıkmak için q ya basın'): ")
    if isim=="q":
        print("programdan çıkılıyor..")
        break
    print("isminiz:",isim)
print(input("soyisim: "))
"""


# contuniue kullanımı

for i in range(15):
    if (i==3 or i==5):
        continue
    print("i",i)
    
       
#local-global değişkenler

def fonk():
    a=10
    return a
  
print(fonk())


def not_string(word):
    if "not" in word:
        return(word)
    else:
        return("not "+word)
    
print(not_string("murat"))
print(not_string("not hasan"))


def missing_char(word, n):
    string = ""
    string = word[0:n]+word[n+1:len(word)]
    return string

print(missing_char("kitchen", 4))


        

