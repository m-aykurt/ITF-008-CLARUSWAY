# -*- coding: utf-8 -*-

#with open("markalar.txt","a") as file:
#    file.write("6-bmw \n")

#with open("markalar.txt","r+",encoding=("utf-8")) as file:
#    markalar = file.read()
#    markalar = "1-toyota\n"+markalar
#    file.seek(0)
#    file.write(markalar)
 
with open("markalar.txt","r+",encoding=("utf-8")) as file:
    markalar = file.readlines()
    markalar.insert(2, "3-renault\n")
    file.seek(0)
    file.writelines(markalar)   
with open("markalar.txt") as file:
    print(file.read())