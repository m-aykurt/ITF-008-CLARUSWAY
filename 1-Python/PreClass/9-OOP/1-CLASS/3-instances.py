# -*- coding: utf-8 -*-

class Person:
    # yapıcı metotlar
    def __init__(self,name,surname,year):
        
        #object attribute
        
        self.name = name
        self.surname = surname
        self.year = year
    
    # instance methods
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}, dogum yilim {self.year} dir."
    def calculate_age(self):
        return f"{2021-self.year}"

# object instance
p1 = Person("Murat", "Aykurt", 1992)
p2 = Person("Selin", "Aykurt", 1993)

print(p1.intro())
print(p2.intro())
print(p1.calculate_age())
print(p2.calculate_age())