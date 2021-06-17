# -*- coding: utf-8 -*-
"""
f = open("msg.txt")
print(f)
print(f.read())

print(f.read())
print(f.read())
print(f.readline())

print(f.close())
print(f.read())
"""
# with komutu 
"""
with open("msg.txt") as file:
    print(file.read())
    print(file.tell())
    print(file.read(10))
    print(file.read())
    
with open("msg.txt") as file:
    for i in file:
        print(i,end=(""))
"""

# geleneksel yöntem
"""
sea = open("fishes.txt","r")

print(sea.read())
sea.seek(0)
print(sea.readlines())
sea.seek(0)
sea.close()

sea = open("fishes.txt","r")
print(sea.read(33))
print(sea.read(12))
print(sea.tell())
print(sea.seek(0))
print(sea.read(2))
"""
"""
rumi = open("rumi.txt","r")
print(rumi.read())
rumi.close()
"""
"""
rumi = open("rumi.txt","r")
print(rumi.readline())
print(rumi.readline())
print(rumi.tell())
"""

"""
rumi = open("rumi.txt","r")
print(rumi.read(35))
print(rumi.read(13))
print(rumi.tell())
rumi.seek(15)
print(rumi.read(21))
rumi.seek(0)
print(rumi.readline())
print(rumi.readline())
print(rumi.readline())
print(rumi.readline())
rumi.seek(0)
print(rumi.readline(13))
print(rumi.readline(13))
print(rumi.readline(13))
print(rumi.readline(13))
rumi.close()

sea = open("fishes.txt","r")
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
sea.close()


rumi = open("rumi.txt","r")
print(rumi.readline())
print(rumi.readline())
print(rumi.readline(3))

rumi.close()
rumi = open("rumi.txt","r")
print(rumi.readline(100))

rumi.close()

rumi = open("rumi.txt","r")
print(rumi.readlines())

for line in rumi.readlines():
    print(line)


rumi = open("rumi.txt","r")
for line in rumi:
    print(line)

rumi.seek(0)
print(rumi.tell())

for line in rumi.readlines():
    print(line)
"""
# with kullanımı
"""
with open("fishes.txt","r") as sea:
    print(sea.read())
    sea.seek(0)
    print(sea.read(45))
"""
