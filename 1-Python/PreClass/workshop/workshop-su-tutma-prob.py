# -*- coding: utf-8 -*-

# given = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
given = []
while True:
    num = input("Type 'ok' when you are done: ")
    if num != "ok":
        given.append(int(num))
    else:
        break
width = len(given) # sütunlardan oluşacak olan tablonun genişliği
height = max(given) # sütunlardan oluşacak tablonun max. yüksekliği
indx = 0 # girilen sayıların index değeri
p = 0   # girilen sayının index deerini bulabilmek için oluşturduğumuz değişken.
        # şöyle ki listede aynı sayıdan iki adet mevcut ise indexini hesaplarken -->
        # --> girdiğimiz sayıyı ilk gördüğü indexini yazmasını engellemek için
areas = 0 #suyun birikeceği toplam alan
list1 = [] # o satırda yer alan sayıalrın index numaralarının yer aldığı liste
for i in range(1,height+1): #en alt satırdan başlayarak üste doğru çıkıyoruz.
  p = 0
  list1 = []
  for j in given:
    indx = given.index(j, p, p+1)
    if j-i >= 0: #girilen sayıların o satırda yer işgal edip etmedğini kontrol ediyoruz. edenleri belirliyoruz.
      list1.append(indx)
    p += 1
  areas += (max(list1) - min(list1) - len(list1) + 1)
print("Rain-trapped area : ", areas)