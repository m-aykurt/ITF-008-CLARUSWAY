# -*- coding: utf-8 -*-
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError as e:
    print("bölen sıfır olamaz.",e)
except ValueError as v:
    print("değer sayı olmalıdır.",v)
except Exception as ex:
    print("hata",ex)
else:
    print("hata oluşmadı")
finally:
    print("çıkış yapılıyor")
"""

def colorize(text,color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır")
    
    if type(color) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    
    if color not in colors:
        raise ValueError("geçersiz renk ismi.")
    
    print(f"{text} {color} olarak yazdırıldı")
"""        
try:
    colorize("selam", "yellow")
except Exception as e:
    print(e)
"""

try:
    colorize("selam", "red")
except:
    print("hata")
else:
    print("hata yok")

list()