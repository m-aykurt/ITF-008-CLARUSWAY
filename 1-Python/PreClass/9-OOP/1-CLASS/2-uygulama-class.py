# -*- coding: utf-8 -*-

class Comment:
    def __init__(self,username, text,likes=0,dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
c1 = Comment("maykurt","ne mutlu türküm diyene",215,1)
c2 = Comment("ahmet_y","güzel mac",1515,1)
c3 = Comment("hakan","kursu begenmedim",15,111)
c4 = Comment("veli","harika",125,1)
c5 = Comment("ali","daha güzel olabilirdi",15,135)


comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username} : {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")