# -*- coding: utf-8 -*-



# estimate coronavirus


age = int(input("what is your age: "))
chronic = input("do you have a chronic ills: ").lower()
immune = input("is your immune system too weak: ").lower()

if (age>75):
    if (chronic == "yes"):
        if (immune == "yes"):
            print("You are in high risky group for coronavirus BE CAREFUL.")
        else:
            print("you should be careful")
    else:
        print("you are in risky group")
else:
    print("you are in lower risky group")
        
