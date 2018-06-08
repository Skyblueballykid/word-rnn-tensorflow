import string
import os
import pandas as pd


os.chdir("C:\\Users\\tkalnik\\Desktop")

printable = set(string.printable)

with open('dirtinput.txt', 'r', encoding='utf-8') as f:
    alist = f.read()

blist = alist.encode("ascii", "ignore")


with open('input.txt', 'wb') as output:
    output.write(blist)

