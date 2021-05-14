# -*- coding: utf-8 -*-

list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

sorted_list = []
result = []

for i in list1:
    if sorted(i) not in sorted_list:
        sorted_list.append(sorted(i))
print(sorted_list)
for ii in sorted_list:
     result.append([i for i in list1 if sorted(i)==ii])
print(result)

"""
Önce listedeki her bir elemanı alıp harflerine ayırarak sorted_list listesine atıyor. (ilk for döngüsü)
Sonra sorted_list listesinde bulunanlar ile listenin elemanlarınını harflere ayırdıklarınız aynı ise sonuç listesine liste olarak ekliyor.
Yani aynı harfleri olan elemanları bir liste yapıp onu sonuç listesinin elemanı yapıyor (ikinci for döngüsü ve append fonksiyonunun içi)
"""