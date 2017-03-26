#coding=utf-8
#第 0001 题：使用 Python 如何生成 200 个激活码（或者优惠券）？

import random,string
f = open("0001.txt",'wb')

choice = string.letters+string.digits
result = ""

for i in range(200):
    temp = ""
    for j in range(20):
        temp = temp+random.choice(choice)
    result = result+temp+"\n"

f.write(result)
f.close()