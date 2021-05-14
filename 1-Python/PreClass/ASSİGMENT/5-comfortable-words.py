# -*- coding: utf-8 -*-
word = input("kelimeniz: ")
word1 = set(word)

left = {'q', 'w', 'e', 'r', 't', 'y', 'a', 's', 'd', 'f', 'g', 'h', 'z', 'x', 'c', 'v', 'b'}

right = {'ü', 'ğ', 'p', 'o', 'ı', 'u', 'j', 'k', 'l', 'ş', 'i', 'ç', 'ö', 'm', 'n'}

# comfortable_word = left.intersection(word1) == word1 and right.intersection(word1) == word1

leftchechk = bool(left.intersection(word1))
rightcheck = bool(right.intersection(word1))

comfortable_word = leftchechk and rightcheck

print(comfortable_word)

