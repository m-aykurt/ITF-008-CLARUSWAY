# -*- coding: utf-8 -*-

try:
    x = 4/1
except:
    print("something went wrong")
else:
    print("nothing went wrong")
finally:
    print("always execute this code..  ")
    

try:
    x = 2/0
except ZeroDivisionError:
    print("attempt to divide by zero")
except:
    print("something else went wrong")
    
try:
    x = int("ben")
except ZeroDivisionError:
    print("attempt to divide by zero")
except:
    print("something else went wrong")
    
    

try:
    
    x = 4/2

except:
    print("unknown exception")
    
try:
    
    x = 4/0

except:
    print("unknown exception")
    
    
    
    # x = int(input('x '))
# y = int(input('y '))

# print(x / y)

# SyntaxError => yazım yanlışı

# hlkhlk;;
# def yazdir((:
#     pass
# print('merhab'a)

# NameError => tanımlanmamış bir değişken kullanımı
# print(ad)

# TypeError => hatalı parametre kullanımı
# len(5)
# 4 + 'a'

# IndexError => yanlış indeks numarası
# liste = ['merhaba']
# liste[1]

# ValueError => hatalı tip kullanımı
# int('10a')

# KeyError => key hatası
# d = {}
# d['ad']

# AttributeError => olmayan bir özelliğe ulaşmak istediğimizde
# "merhaba".upper()
# "merhaba".Upper()


# 1

"""
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('hata oluştu.')
        print(e)
    except Exception as e:
        print('bilinmeyen bir hata oluştu.')
        print(e)
    else:
        break
    finally:
        print('finally bloğu çalıştı.')
"""
# 2
"""
liste = ["1","2","5a","10b","abc","10","50"]

for i in liste:
    try:
        sonuc = int(i)
        print(sonuc)
    except:
        continue
    
while True:
    sayi = input("sayi : ")
    if (sayi == "q"):
        print("cıkılıyor")
        break
    try:
        sonuc = float(sayi)
        print(f"girilen sayi: {sonuc}")
        break
    except Exception as e:
        print(f"hatalı giriş sebebi: {e}")
        
"""

# 3

urun = {"urun_adi":"samsung s10"}

def get(d,key):
    try:
        return d[key]
    except Exception as e:
        return None
    
print(get(urun,"fiyat"))
print(get(urun,"urun_adi"))
print(get(urun,"fiyat"))


 # raise -- hata fırlatma
 
 # print(10 / 0)

# x = 10

# if x > 5:
#     raise ValueError('x 5 den büyük olamaz.')

def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır.")

    if type(color) is not str:
        raise TypeError("renk str tipinde olmalıdır.")

    if color not in colors:
        raise ValueError("geçersiz bir renk ismi.")

    print(f"{text} {color} olarak yazdırıldı.")

# try:
#     colorize("selam","yellow")
# except Exception as ex:
#     print(ex)

try:
    colorize("selam","red")
    colorize("selam","yellow")
except (TypeError,ValueError) as ex:
    print(ex)
    
    
def fakt(x):
    x = int(x)
    
    if (x<0):
        raise ValueError("negatif deger olamaz")
        
    sonuc = 1
    for i in range(1,x+1):
        sonuc *=i 
        
    return sonuc

for i in [2,5,3,"3",6,"2a",12,"10a"]:
    try:
        print(fakt(i))
    except TypeError as ex:
        print(ex)
    except Exception as e:
        print(e)
        
        
# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

# def faktoriyel(x):
#     x = int(x)

#     if (x<0):
#         raise ValueError("Negatif değer")

#     sonuc = 1
#     for i in range(1, x+1):
#         sonuc *= i

#     return sonuc

# for i in [5,7,'a',2,-4,'10a']:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.

def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

    print('geçerli parola')

parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
    
    
### pdb ##########
# import pdb

# one = "one"
# two = "two"
# pdb.set_trace()
# sonuc = one + two

# three = "three"

# sonuc += three

# print(sonuc)

def add_numbers(a,b,c):
    import pdb; pdb.set_trace()
    return a+b+c

add_numbers(1,2,3)

# l => list
# n => next line
# p => print
# c => continue