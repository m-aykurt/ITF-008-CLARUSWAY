# -*- coding: utf-8 -*-


def selamlama(isim, mesaj="gunaydın"):
    print(f"{mesaj} {isim}")

selamlama("murat", "gunaydın")
selamlama("murat", 3)
selamlama("murat", "hello")


def us_alma(taban, us=3):
    return taban ** us

sonuc = us_alma(3, 2)
sonuc = us_alma(5,)
sonuc = us_alma(5,4)
sonuc = us_alma(5)

print(sonuc)

def toplam(a,b):
    return a+b

def cikarma(a,b):
    return(a-b)

def islem(a,b,fn):
    return fn(a, b)

def islem(a,b,fn = toplam):
    return fn(a, b)


sonuc = islem(4, 6)
print(sonuc)

# Coklu Parametre Tanımlama-İNT

def toplam(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(22,51,23))

def toplam(*args):
    print(type(args))
    print(args)
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(2,5,1))



# Coklu Parametre Tanımlama-STRİNG

def full_name(first_name, last_name="aykurt"):
    return f"your name is {first_name} {last_name}"

sonuc = full_name("murat", "aykurt")
sonuc = full_name(last_name = "aykurt", first_name = "murat" )

print(full_name("murat"))


def display_user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print("\n")

    
display_user(username = "murataykurt",email = "maykurt92@gmail.com")
display_user(username = "murataykurt",email = "maykurt92@gmail.com",country = "turkey")

# 

def my_func(a,b,c,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    
my_func(1,2,3,22,66,key1 = "value1", key2 = "value2")



