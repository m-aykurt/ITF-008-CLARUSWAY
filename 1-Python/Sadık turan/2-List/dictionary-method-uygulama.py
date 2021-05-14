# -*- coding: utf-8 -*-
"""
players = {
    {
     "id":1,
     "name":"Ronaldo",
     "yearBirth":1985,
     "nationality":"portugal",
     "team":"juventus",
     "history":"juve,real madrid,man u"
     },
    {
      "id":2,
     "name":"Messi",
     "yearBirth":1987,
     "nationality":"Argentina",
     "team":"Barcelona",
     "history":"Barcelona,Argentina"
     }
    }

print(players)
"""


players = {
    '1': 
        {'name': 'ronaldo', 'birth': '1985', 'nationality': 'portugal', 'team': 'juve', 'history': ['madrid']
         }
    ,
    '2': {'name': 'messi', 'birth': '1086', 'nationality': 'argentina', 'team': 'barcelona', 'history': ['barca']
          }
    }
"""
id = input("oyuncu id: ")
name = input("oyuncu adi : ")
birth = input("oyuncu dogum yili: ")
nationality = input("oyuncu uyrugu: ")
team = input("takımı: ")
history = input("oynadığı takımlar: ")

players.update({
    id:{
        "name": name,
        "birth": birth,
        "nationality":nationality,
        "team":team,
        "history":history.split(",")
        }
    
    
    })

id = input("oyuncu id: ")
name = input("oyuncu adi : ")
birth = input("oyuncu dogum yili: ")
nationality = input("oyuncu uyrugu: ")
team = input("takımı: ")
history = input("oynadığı takımlar: ")

players.update({
    id:{
        "name": name,
        "birth": birth,
        "nationality":nationality,
        "team":team,
        "history":history.split(",")
        }
    
    
    })
"""
"""
id = input("id giriniz: ")
player = players.get(id)
"""
"""
id = input("silmek istenilen oyuncu id: ")
players.pop(id)


print(players)

"""

phrase = "myemailaddress@clarusway.com"
sonuc = phrase[14]
print(phrase.endswith(".", 15, 24))
print(sonuc)

print("Actions speaks louder than words".upper().swapcase().title())


"""
firstName = input("isminiz ?").upper()
lastName = input("soyadınız ?").capitalize()
"""
# print("Benim adım "+ firstName.capitalize() +" " +lastName.upper())
"""
print(f"Benim adım {firstName} {lastName}")
"""


x = False
y = not x

print(not (x and y))

print(float("140" * int(input("Enter a number:" ))))