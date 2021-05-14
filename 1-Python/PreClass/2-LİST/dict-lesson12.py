# -*- coding: utf-8 -*-
"""
first_dict = {1:"one",2:"two"}
print(first_dict)

grocer1 = {"fruit":"apple","drink":"water"}
grocer2 = dict(fruit="apple",drink="water")
print(grocer2)

sehir1 = "istanbul"
sehir2 = "ankara"
sehirler = {1:sehir1,2:sehir2}
print(sehirler)
print(sehirler[2])

print(type(sehirler[2]))

state_capitals = {
    "arkansas":"little rock",
    "colorado":"denver",
    "california":"sacramento",
    "georgia":"atlanta",
    }

state_capitals["virginia"] = "richmond" # dict e ekleme yapılabilir
print(state_capitals)

state_capitals["california"] = "istanbul" # sözlük içindeki değerleri değiştirmemize imkan sağlıyor
print(state_capitals)

mix_values = {
    "animal":("dog","cat"),
    "planet":["neptın","saturn","jupiter"]

    }
print(mix_values)


family = {
    "name1" : "murat",
    "name2" : "ali",
    "name3" : "veli"
    }
print(family)

family["name4"] = "hasan"
print(family)

dict_by_dict = dict(animal = "dog", planet = "neptun", number = 40, is_good = True)
print(dict_by_dict)

x = dict(name1 = "murat", name2 = "ahmet" ,name3 = "mehmet")
print(x)

dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)

print(dict_by_dict)

x = {'animal': 'dog', 'planet': 'neptun', 'number': 40, 'pi': 3.14, 'is_good': True}
print(x.items())
print(x.keys())
print(x.values())

my_family = {'name1': 'murat', 'name2': 'ali', 'name3': 'veli', 'name4': 'hasan'}

print(my_family.items())
print(my_family.keys())
print(my_family.values())
print(list(my_family.items()))
print(list(my_family.keys()))
print(list(my_family.values()))
my_family.update({"name1":"ben","name5":"yusuf"})
print(my_family)

x = {'animal': 'dog', 'planet': 'neptun', 'number': 40, 'pi': 3.14, 'is_good': True}
x.update({"is_bad" : False})
print(x)
x.update({"animal":"cat"})
print(x)

del dict_by_dict["animal"]
print(dict_by_dict)

my_family = {'name1': 'murat', 'name2': 'ayşe', 'name3': 'fatma', 'name4': 'hasan'}
del my_family["name2"],my_family["name3"]
print(my_family)

my_family = {'name1': 'murat', 'name2': 'ayşe', 'name3': 'fatma', 'name4': 'hasan'}
del my_family["name1"]

print(my_family)

my_family = {'name1': 'murat', 'name2': 'ayşe', 'name3': 'fatma', 'name4': 'hasan'}

print("name1" in my_family)

my_family = {'name1': 'murat', 'name2': 'ayşe', 'name3': 'fatma', 'name4': 'hasan'}
x = "murat" in my_family.values()
x = "Murat" in my_family.values()

print(x)
"""
school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },
        },
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },
        },
}
"""
print(len(school_records))
print(school_records["grades_info"]["kid"]["tom"])
print(school_records["personal_info"]["kid"]["tom"]["class"])
print(type(school_records["personal_info"]["kid"]["tom"]["class"]))
print(type(school_records["personal_info"]["kid"]["tom"]))
"""
school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },
        },
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },
        },
}
print(school_records["personal_info"]["teen"])
print(school_records["personal_info"]["kid"])
print(school_records["personal_info"]["teen"]["joseph"])
print(school_records["grades_info"]["teen"]["joseph"])
print(list(school_records["grades_info"]["teen"]["joseph"].items()))

friends = {
    "friends1" : {
        "name":"yakup",
        "age":29
        },
    "friends2" : {
        "name":"burak",
        "age":30
        }
    }
print(friends)
print(list(friends.items()))
print(list(friends.values()))


favourite = {
"friends":
        {
    "friends1" : {
        "name":"yakup",
        "age":29
        },
    "friends2" : {
        "name":"burak",
        "age":30
        }
        },
"family":
    {
    "dad":{
        "name":"ahmet",
        "age":60
        
        },
    "mom":{
        "name":"ayse",
        "age":59
        }
    }
}
print(favourite)









