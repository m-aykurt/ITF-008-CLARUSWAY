
# -*- coding: utf-8 -*-

import termcolor

#sonuc = dir(termcolor)
#sonuc = help(termcolor)
sonuc =termcolor.colored("merhaba ",color=("green"),on_color = "on_yellow")
sonuc =termcolor.colored("merhaba ben murat ",color=("green"),on_color = "on_yellow",attrs=["bold"])

print(sonuc)