# -*- coding: utf-8 -*-
### 1
"""
Proje sorumlusu olarak  genis  katilimli bir projede calisiyorsunuz ve coronadan dolayi tum toplantilarinizi online yapiyorsunuz. Toplantiya katilan 200 personelden bazilari toplantiya gecikmeli katilim gostermeye basladi. Siz de proje sorumlusu olarak bunu toplantiyi bolmeden ve kisileri topluluk icerisinde rencide etmeden bireysel olarak personelinize bildirecek basit bir otomatik message program yazmayi planladiniz. Toplantiya gec kalan kisi toplantiya katildiginda, sizin yazdiginiz mesaj ozel olarak kendisine ulasiyor.
Ornek : “Merhaba Kaya, toplantiya bugun 10 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
Gec kalan personel listesi:
 Isimler = [‘Kaya’, ‘Sinem’, ‘Peker’, ‘Jale’, ‘Fikret’, ‘Necmi’]
·     Gec kalma zamani, her personel toplantiya 10 dk gecikme artarak katiliyor.
Ornek: Kaya 10 dk gecikiyor, Sinem 20 dk, Peker 30dk, ….


isimler = ["Kaya", "Sinem", "Peker", "Jale", "Fikret", "Necmi"]

count =1
while count < len(isimler):
    for i in isimler:
        print(f" merhaba {i} toplantiya bugun {count * 10} dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.")
        count+=1
        
word = input("word: ")
count = 0
for i in word:
    count +=1
    if count < len(word):
        i = i + "-"
    print(i,end="")
"""
### 2
"""
Gorev:
Verilen Numara listesindeki hangi iki rakamin toplami hedef sayiyi verirse bu sayilarin index numaralarini almak istiyoruz.
Ornek:
num_list = [8,2,4,7,1,5,6,9]
hedef = 16
Verilen listeden 7 +9 =16 yi saglar. Index numalari 3 ve 7
Istenilen sonuc:  3 , 7
TEST Degerleri:
test1 = [8,2,4,7,1,5,6,9]  hedef = 16    istenilen sonuc = 3, 7
test2 = [22,5,11,7,19,4,12]   hedef = 24 istenilen sonuc = 1 ,4

liste = [8,2,4,7,1,5,6,9]
hedef = 16
ind = []
for i in range(len(liste)):
    for ii in range(i+1,len(liste)):
        if liste[i] + liste[ii] == hedef:
            if i not in ind:
                ind.append(i)
            if ii not in ind:
                ind.append(ii)
print(ind)


test1 = [8,2,4,7,1,5,6,9] 
item = []
for i in test1 :
    for j in test1 :
        if i + j == 16:
            if test1.index(i) == test1.index(j):
                pass
            else:
                item.append(test1.index(i))
print("şartı sağlayan index numaraları: ",*item, end = " ")
"""
# 3 girilen sayıların çarpımlarını bulma
"""
kac_adet = int(input("kac defa sayi girmek istersiniz: "))

carpim = 1

for i in range(kac_adet):
    sayi = int(input("sayi giriniz: "))
    carpim = carpim * sayi
print(carpim)
"""
# 4 max-min def
"""
def enbuyuk(*args):
    x=max(args)
    y=min(args)
    print(f"En büyük sayı = {x} , en küçük sayı = {y}")
    
enbuyuk(22,15,100)
"""

### 5 Mesaj :
"""
'Canim migicabab her namaz aklimdasin. migicabaB seni koc ozledim, ines cok ama cok .muroyives'
Ipucu:
-      Size verilen text te yer alan her ikinci kelime ters cevrilmis.
2. Bolum:
Challenge isteyenler icin:
Mesaj:  '   Gungectikce        iyamaldok   daha  koc    seviyorum.   '


list1 =  'Gungectikce iyamaldok daha koc seviyorum.'
list2 = list1.split()
sentence = ""
for i in range(len(list2)):
    if i % 2:
        sentence += list2[i][::-1] + " "
    else:
        sentence += list2[i]+" "
        
print(sentence)
"""     
# 6 mülakat sorusu
"""
bir şirketin iş görüşmesinde sormuş olduğu algoritma sorusu

örnek bir liste yaptım onu da atayım

numbers_list = [2,3,4,12,11,2,3,5,12,2]
Elinde içinde sayılardan oluşan bir dizi var. Bu dizi içinde çift sayıda olmayan elemanları (tek sayıda olan elemanları) listeleyen algoritmayı yaz.

def tek_sayi(*args):
    numb = list(args)
    tek = []
    for i in range(len(numb)):
        if numb.count(numb[i])%2!=0:
           tek.append(numb[i]) 
    return set(tek)
    

print(tek_sayi(2,3,4,12,11,2,3,5,12,2))
"""
### 7 carpanlara ayırma
"""
def asal_mi(n):
    asal_mi = True
    for i in range(2,n):
        if n == 2:
            asal_mi = True
        elif n%i == 0:
            asal_mi = False
    return asal_mi
def carpan(n):
    return [i for i in range(2,n) if not n%i]
def asal_carpan(n):
    return [i for i in carpan(n) if asal_mi(i)]
def asal_sayi(n):
    return [i for i in range(2,n) if asal_mi(i)]

print(asal_mi(12))
print(carpan(12))
print(asal_carpan(12))
print(asal_sayi(12))

def pisagor():
    for a in range(1,1000):
        for b in range(a+1,1000):
            c = 1000 - (a+b)
            if a*a + b*b == c*c:
                print(a,b,c)
pisagor()
"""

# filter - sessiz harfleri bulma
"""
def filter_vowels(letter):
    vowels = ["a","e","i","u","o"]
    if letter.lower() not in vowels:
        return True
    else:
        return False
sentence = "i want to eat cake before dinner"
filtered_sentence = filter(filter_vowels, sentence)
print(set(filtered_sentence))
"""
# tam bölenleri bulma--amicable numbers.
"""
def amic_num(n):
    list_div = []
    for i in range(1,n):
        if n%i==0:
            list_div.append(i)
    return sum(list_div)
list_amic = []
for i in range(2,10000):
    b = amic_num(i)
    
    if amic_num(b)==i and i!=b:
        list_amic.append(i)
print(sum(list_amic))        
"""        

# pisagor üclüsü
"""
def pisagor():
    for a in range(1,1000):
        for b in range(a+1,1000):
            c = 1000-(a+b)
            if a**2+b**2==c**2:
                print(a,b,c)
             
pisagor()
"""
#parola sorgulama,

"""
# parola doğruluğu Kullanıcılar tarafından girilen parola geçerliliğini kontrol etmek için bir Python programı yazın.
#Doğrulama:
#[A-z] arasında en az 1 harf ile [A-Z] arasında 1 harf.
#[0-9] arasında en az 1 sayı.
#[$ # @] 'Den en az 1 karakter.
#Minimum uzunluk 6 karakter.
#Maksimum uzunluk 16 karakter.

harf = set("qwertyuıopğüişlkjhgfdsazxcvbnmöç")
harf_b = set("QWERTYUIOPĞÜIŞLKJHGFDSAZXCVBNMÖÇ")
rakam = set("0123456789")
krktr = set("$#@!^")

password = set(input("parola giriniz: "))

if len(harf.intersection(password))>0 and len(harf_b.intersection(password))>0 and len(rakam.intersection(password))>0 and len(krktr.intersection(password))>0 and len(password)>=6 and len(password)<=16:
    print("parolanız doğru")
else:
    print("parolanız yanlış")
    
    
    
    
### diğer çözüm



print("Parolunuzu olustururken: \n1- En az bir kücük harf,\n2- En az \
 büyük harf,\n3- En az bir rakam,\n4- $, #, @ karakterlerinden en az birini\
  kullanin!\n5- Sifre uzunlugu en az 6 maksimum 16 karakter olmalidir!")
while True :
  parola= input("\nLütfen parolanizi giriniz: ")
  harf= "abcdefghijklmnopqrstuvwxyz"
  buyuk= "ABCDEFGHIJKLMNOPRSTUQVYZWX"
  sayi="0123456789"
  special="$#@"
  harf_ctrl = set(parola).intersection(harf)
  buyuk_ctrl= set(parola).intersection(buyuk)
  sayi_ctrl= set(parola).intersection(sayi)
  spe_ctrl= set(parola).intersection(special)
  if (harf_ctrl and buyuk_ctrl and sayi_ctrl and spe_ctrl and len(parola)<17 and len(parola)>5): 
     print("Parola basariyla olusturuldu!")
     break
  else :
    print("Tekrar deneyiniz!")
    
"""
# def ile sayıları ters çevirme
"""
def ters_liste(a,b):
    a.reverse()
    b.reverse()
    str1 = "".join([str(i) for i in a])
    str2 = "".join([str(i) for i in b])
    c = int(str1) + int(str2)
    c = list(map(int, list(str(c)[::-1])))
    return c
a = [2,7,6,2,5,9]
b = [1,5,2,3,6,8,7,0,2]

print(ters_liste([2,7,6,2,5,9],[1,5,2,3,6,8,7,0,2] ))
"""

# ·     Encode isimli bir fonksiyon olusturacagiz.
#     Bu fonksiyonla, bize verilen string de yer alan tum kucuk sesli harfleri numaralarla degistirecegiz.
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# Ornek: string = ‘hello’  istenilen sonuc ‘h2ll4’
"""
def encode(text):
    sozluk = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    for i in text:
        for key,value in sozluk.items():
            if i == key:
                text = text.replace(i,value)
            elif i == value:
                text = text.replace(i,key)
    return text

print(encode("merhaba"))
print(encode("h3 th2r2"))
                
### 

def digits(n):
  basamak=len(str(n))
  sonuc=0
  for i in range(1,basamak):
    sonuc += 9*i*10**(i-1)
  sonuc+=(n-(10**(basamak-1)))*basamak
  return sonuc
print(digits(100))
"""
## Write a function that selects all words that have all the same vowels (in any order and/or number) as the first word, including the first word.
"""
def same_vowel(liste):
    l1 = set()
    z = ["a","e","i","o","u"]
    [l1.update(x) for x in liste[0] if x in z]
    output = [liste[0]]
    
    for x in liste[1:]:
        if set([i for i in x if i in z]) == l1:
            output.append(x)
    return output

print(same_vowel(["ahmet","mehmet","ahmetahmet", "ali","veli","ihsan","tehma"]))        
"""
#SIFIRLARI SONA ALMA
"""
def sıfırlar_sona(liste):
    for i in liste:
        if i == 0:
            liste.remove(i)
            liste.append(i)
    return liste
    
print(sıfırlar_sona([0,2,0,0,3,0,1]))

import itertools 
print(*itertools.permutations([1,2,3,4]),sep="\n")

liste = ['A', 'B', 'C']
mylist = []
for i in liste:
    for x in liste:
        for y in liste:
            mylist.append([i,x,y])
newlist = []
for m in mylist:
    if m not in newlist and len(set(m)) == len(liste):
        newlist.append(m)
print(newlist)
"""
# is_weird
"""
while True:
    n= int(input("1 ile 100 arasında  bir sayı giriniz: "))
    if n % 2 !=0:
        print("weird")
    elif n%2==0 and n in list(range(2,5)):
        print("not weird")
    elif n%2==0 and n in list(range(6,20)):
        print("weird")
    elif n%2==0 and 20<n<100:
        print("not weird")
    else:
        break
"""
# sayilardan liste olusturup indeksleme
"""
n = int(input("kac defa sayı girmek istersiniz: "))
count = 0
l = []
if n>1 and n<=10:
    while count<n:
        sayi=int(input("sayi: "))
        if sayi >= -100 and sayi<=100:
            l.append(sayi)
            l.sort(reverse=True)
            count+=1
        else:
            print("girilen değer yanlis")
else:
    print("2 ile 10 arasındaki miktarda sayi giriniz")
print(l[1])
"""        
# SAYİ OBEB LERİNİ BULMA
"""
a,b = 256,960
l1 = []
l2 = []
[l1.append(i) for i in range(1,a+1) if a%i==0]
[l2.append(j) for j in range(1,b+1) if b%j==0]

ortak = set(l1).intersection(set(l2))
son_l = sorted(ortak)[-1]
print(f"{int(a/son_l)}/{int(b/son_l)}")
"""
# PATH CHOİCE
"""
from random import choice
# Are you ready for choice your path
# best wishes ---- mehmetfatihdata
path = ['Data Science', 'DevOps/AWS', 'Full Stack']
ch = []
count = 0
while count < 100:
    ch.append(choice(path))
    count += 1
DS_say = []
DO_say = []
FS_say = []
for i in ch:
    if i == 'Data Science':
        DS_say.append(i)
    elif i == 'DevOps/AWS':
        DO_say.append(i)
    else:
        FS_say.append(i)
        
DataScience = " % " + str(len(DS_say)) + " Your Path is " + "DataScience"
DevOpsAWS = " % " + str(len(DO_say)) + " Your Path is " + "DevOpsAWS"
FullStack = " % " + str(len(FS_say)) + " Your Path is " + "FullStack"
print(
    f' Canguralations and reinvent yourself. ******\
{max(DataScience, DevOpsAWS, FullStack)}******'
)
"""

# CÜMLEDEKİ SESLİ HARFLER
"""
# 1 inci çözüm
def sesli_harf(cumle):
    c = list(cumle)    
    vowel = ["a","e","i","o","u"]
    say = []
    [say.append(i) for i in c if i in vowel]
    return len(say)
    
print(sesli_harf("merhaba ben murat"))
# 2 nci çözüm

def counter(x):
    vowel = ["a","e","i","o","u"]
    num = [i for i in x.lower() if i in vowel]
    return len(num)
print(counter("merhaba ben murat"))
# 3 uncu çözüm
print(len(list(filter(lambda x: x in list("aeıioöuü"),"merhaba ben murat"))))
"""
#####

"""
def gcd_euclid_theorem(a, b):
  if a % b == 0:
    return b
  else:
    return gcd_euclid_theorem(b, a % b)
def simplify(frac):
  num, den = map(int, frac.split("/"))
  gcd = gcd_euclid_theorem(num, den)
  return str(num // gcd) + (("/" + str(den // gcd)) if den // gcd != 1 else "")
"""

### can see stage
"""
def can_see():
    n = int(input("kac defa liste gireceksiniz: "))
    count = 0 
    x = []
    while n < count:
        x.append(input("lsite: "))
        
    for i in x:
        l_0 = [] 
        for j in x[0]:
            l_0.append(j)
            if  max(l_0) == l_0[0]:
                return "l_0 True"
            else:
                return "l_0 False"
        l_1 = [] 
        for j in x[1]:
            l_0.append(j)
            if  max(l_1) == l_1[0]:
                return "l_1 True"
            else:
                return "l_1 False"
        l_2 = [] 
        for j in x[2]:
            l_2.append(j)
            if  max(l_2) == l_2[0]:
                return "l_2 True"
            else:
                return "l_2 False"
        l=[]
        l.append(l_0)
        l.append(l_1)
        l.append(l_2)

        
    return all(l)
            
print(can_see())

for k in range(len(i)-1):
      if i[k]>=i[k+1]:
          print(False)
      else:
          print(True)

# kaan bey çözümü

def see(l):
    for x in range(len(l)-1,0,-1):
        for y in range(len(l)-1,-1,-1):
            if l[x][y] <= l[x-1][y]:
                return False
    return True
print(see([[1,2,3],[2,3,4],[4,5,6]]))

# raife hanım çözümü

liste = [[1,2,3],[2,1,4],[4,5,6]]
for i in zip(*liste):
    for k in range(len(i)-1):
      if i[k]>=i[k+1]:
          print(False)
      else:
          print(True)
"""

# Create a function that takes a number as an argument. Add up all the numbers from 1 to the number you passed to the function. For example, if the input is 4 then your function should return 10 because 1 + 2 + 3 + 4 = 10. Examples
"""
def add(n):
    count = 0
    for i in range(n+1):
        count += i 
    return count
print(add(4))
"""
# raife hanım çözümü
"""
def indexle(cumle):
  sozluk={}
  yeni=""
  for i in cumle.split():
    for k in i:
      if k.isdigit():
        sozluk[int(i[i.index(k):])]=i[:i.index(k)]
        break
  for i in sorted(sozluk) :
    yeni+=(sozluk[i]+" ")
  return yeni.strip().lower().capitalize()
print(indexle("merhaba1 murat3 ben2"))
"""
"""
s =  'Bir3 bu1 test4 kolay2'.split()
liste = []
for i in s:
    liste.append(i[::-1])
sort = sorted(liste)
lis = []
sentence = ""
for j in sort:
    lis.append(j[::-1])
    sentence += " "+ j[::-1]
test = ''.join( filter(lambda x:  not x.isnumeric(), sentence))
print(test.strip().capitalize())
"""
# perfect number
"""
def perf(n):
    return True if sum([i for i in range(1,n) if not n%i]) == n else False

print(perf(6))
print(perf(28))
print(perf(496))
print(perf(497))

def per(n):
    return sum(filter(lambda x: n % x == 0, range(1, n))) == n
print(per(25))
"""
"""
# palindrom
def same_word(s):
    new_text = "".join(filter(str.isalpha,s)).lower()
    return new_text == new_text[::-1]

print(same_word("nurses run"))
"""
# letter frequency 
"""
def freq(str):
    sozluk = {}
    for i in str:
        if i in sozluk:
            sozluk[i] += 1
        else:
            sozluk[i] = 1
                
            for i in str:
                if sozluk[i] != 0:
                    return f"{i} : {sozluk[i]}"
                    sozluk[i] = 0

print(freq("merhaba ben murat"))
print(freq("merhaba ben murat"))
print(freq("merhaba ben murat"))

                
    
"""
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
