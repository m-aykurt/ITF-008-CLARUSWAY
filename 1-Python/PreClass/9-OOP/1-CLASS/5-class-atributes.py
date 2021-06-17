# -*- coding: utf-8 -*-

class User:
    
    active_users = 0
    
    def __init__(self,first,last_name,age):
        self.first = first
        self.last_name = last_name
        self.age = age
        User.active_users += 1
        
    def full_name(self):
        return f"{self.first} {self.last_name}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan cikis yapti"
    
        
        

print(User.active_users)    
userA = User("murat", "aykurt", 29)
userB = User("selin", "aykurt", 28)
print(User.active_users)
userC = User("ali", "veli", 15)
print(User.active_users)
print(userC.logout())
print(User.active_users)

#print(userA.full_name())
#print(userB.full_name())


class Pet:
    cinsler = ["kedi","köpek","kuş"]
    
    def __init__(self,isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir")
            self.isim = isim
            self.cins = cins
    
    def set_cins(self,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir")
        self.cins = cins
        
boncuk = Pet("boncuk", "kedi")
mavis = Pet("mavis", "kuş")
pasa = Pet("pasa", "köpek")


print(boncuk.set_cins("balik"))
            
        
    
    