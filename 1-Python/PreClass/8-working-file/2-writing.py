# -*- coding: utf-8 -*-
"""
## append "a" modu ile sona ekleme yaparız-- cursor un yeri önemli değil
with open("newfile.txt","w",encoding=("utf-8")) as file:
    file.write("murat aykurt \n")
    file.write("selin")
    file.close
    print(file)
with open("newfile.txt") as file:
    print(file.read())
    

with open("msg1.txt","r+") as file:
    file.write("yeni satir")
"""

"""
with open("benim_ilk_dosyam.txt","w",encoding=("utf-8")) as dosyam:
    dosyam.write("bu benim ilk satırım. \n")
    dosyam.write("ikinci satır \n")


with open("benim_ilk_dosyam.txt","w",encoding=("utf-8")) as dosyam:
    dosyam.write("bu benim ilk satırım.\n ama aslında ikinci satır \n")
    
with open("benim_ilk_dosyam.txt","w",encoding="utf-8") as dosyam:
    dosyam.write("yeni satirlar \n")

with open("benim_ilk_dosyam.txt","w",encoding="utf-8") as dosyam:
    dosyam.write("yeni satirlar-2 \n")
    
with open("benim_ilk_dosyam.txt","a",encoding="utf-8") as dosyam:
    dosyam.write("yeni satirlar-3 \n")
with open("benim_ilk_dosyam.txt","a",encoding="utf-8") as dosyam:
    dosyam.write("yeni satirlar-4 \n")

# dummy file

with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')
with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())


# liste içinden nesne ilave etme
    
fruits = ["banana","orange","apple","strawbery","cherry"]    
with open("fruits.txt","w",encoding=("utf-8")) as fruit:
    for meyve in fruits:
        fruit.write(meyve + "\n")

with open("fruits.txt","r") as fruit:
    print(fruit.read())
    
"""

# ders -2 
"""
fruits = ["banana","orange","apple","strawbery","cherry"]    
with open("fruits.txt","w",encoding=("utf-8")) as file:
    for meyve in fruits:
        file.write(meyve + "\n")

with open("fruits.txt","r") as fruit:
    print(fruit.read())
    fruit.seek(0)
    print(fruit.readlines())
    
flowers = ["jasmine \n","rose\n","lily\n","daisy\n","tulip\n"]

with open("flowers.txt","w",encoding=("utf-8")) as flower:
    flower.writelines(flowers)
    
with open("flowers.txt","r") as flower:
    print(flower.read())    
    
with open("fruit.txt","a",encoding="utf- 8") as file:
  file.write("melon")
  
with open("fruit.txt","r",encoding="utf- 8") as file:
  print(file.read())
"""
"""
fruits = ["banana\n","orange\n","apple\n","strawbery\n","cherry\n"]    
with open("fruits.txt","w",encoding=("utf-8")) as file:
        file.writelines(fruits)

with open("fruits.txt","r") as file:
    print(file.read())
with open("fruits.txt","a") as file:
    file.write("melon\n")
with open("fruits.txt","r") as file:
    print(file.read())
"""
# istiklal marşını kıtalara bölme
"""
with open("istiklal.txt","r",encoding=("utf-8")) as file:
    lines = file.readlines()


counter = 0
with open("istiklal.txt", "w", encoding="utf-8") as march :
    for line in lines :
        counter += 1
        if counter % 4 == 0 :
            march.write(line + "\n")
        else :
            march.write(line)
with open("istiklal.txt", "r", encoding="utf-8") as march :
    print(march.read())

count = 0
with open("istiklal.txt","a", encoding="utf-8") as file:
    for i in line:
        if count%5 ==0:
            del i
            count += 1
        else:
            file.write(i)
"""

word = {1 : "1", 2 : "2"}
keys = word.keys()
print(keys)

word_1 = {}
word_1[3] = 1
print(word_1)
word_1[1] = 1
print(word_1)
word_1[3] +=1
print(word_1)

string = "bir berber, bir'e berber"

word_dict = {}

for n in string:
    keys = word_dict.keys()
    if n in keys:
        word_dict[n] += 1
    else:
        word_dict[n] = 1
print(word_dict)

veri = ["a","b",True,(False,1), {"1":2},[1,2],{"2":"two"},{2,"3"},"c",23,0]
toplam = {"int":0,"str":0,"bool":0,"tuple":0,"dict":0,"set":0}

for i in range(len(veri)):
    if type(veri[i])==int: toplam["int"] +=1
    elif type(veri[i])==str: toplam["str"] +=1
    elif type(veri[i])==bool: toplam["bool"] +=1
    elif type(veri[i])==tuple: toplam["tuple"] +=1
    elif type(veri[i])==dict: toplam["dict"] +=1
    elif type(veri[i])==set: toplam["set"] +=1
        
print(toplam)  

import os #----------------------------

print(os.listdir())

import glob #------------------------------

for file in glob.glob("*.txt"):
    print(file)
    
import shutil #----------------------------

shutil.copy("fruit.txt", "../fruits_24_copy.txt")



# ---- def 

def my_factorial(n):
    if n == 0:return 1
    else:
        return n * my_factorial(n-1)
print(my_factorial(5))


