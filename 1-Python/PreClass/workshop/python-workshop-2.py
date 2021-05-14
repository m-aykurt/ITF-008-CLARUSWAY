# -*- coding: utf-8 -*-

# task-1
adet = int(input("kac adet sayi girmek istersiniz: "))

sayilar = []
i = 0
while (i<adet):
    sayi = int(input("bir sayi giriniz: "))
    sayilar.append(sayi)
    i +=1

print(sayilar)
sayilar.sort(reverse=True)
print(sayilar) 
print(f"Girdiğiniz sayilardan en büyüğü {sayilar[0]} dür.")

# task-2

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
list_c = []
list_n = []
list_b = []
list_e = []
for i in strs:
  for j in i:
    if j == "c":
      list_c.append(i)     
for i in strs:
   for j in i:
     if j == "n":
       list_n.append(i)
for i in strs:
   for j in i:
     if j == "b":
       list_b.append(i)  
for i in strs:
   for j in i:
     if j == "e":
       list_e.append(i) 
last_list = [list_e, list_n, list_b, list_c]
print(last_list)

# task-3




