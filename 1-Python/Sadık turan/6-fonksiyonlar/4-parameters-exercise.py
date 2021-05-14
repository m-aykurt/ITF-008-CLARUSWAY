# -*- coding: utf-8 -*-

#hangi sayinin buyuk oldugunu bulma
def buyuk_sayi(a,b):
    if a > b:
        return f"{a} {b}'den buyuktur"
    elif b > a:
        return f"{b} {a}'dan buyuktur"
    else:
        return f"{a} {b}'ye esittir."
    
print(buyuk_sayi(5, 2))
print(buyuk_sayi(2, 2))

# stringin icindeki her karakter kac kez tekrarlanmıs 

def karakter_sayi_bul(text):
    return {letter: text.count(letter) for letter in text}

print(karakter_sayi_bul("ala ki ne ala"))

# listeye istediğimiz yere göre ekleme cıkarma yapma

def update_list(liste,command,position,value = None):
    if (command == "remove" and position == "end"):
        liste.pop()
        return liste
    elif (command == "remove" and position == "beginning"):
        liste.pop(0)
        return liste
    elif (command == "add" and position == "end"):
        liste.append(value)
        return liste
    elif (command == "add" and position == "beginning"):
        liste.insert(0,value)
        return liste
    
print(update_list([1,2,3,4], "remove", "end"))
print(update_list([1,2,3,4,5,6], "add", "beginning","merhaba"))
    
# kendisine gönderilen listede blue varsa true döndüren fonks.

def blue_func(*args):
    color = list(args)
    if color.count("blue")>0:
        return "evet mavi listede"
    else:
        return "listede mavi yok"
    
def blue_func1(*args):
    if "blue" in args:
        return "evet mavi listede"
    else:
        return False
    
print(blue_func("blue","green","white","yellow"))
print(blue_func1("green","white","yellow"))


