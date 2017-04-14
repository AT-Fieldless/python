# -*- coding: utf-8 -*-

# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

import re
s = set()

def define():
    file = open("filtered_words.txt")
    for eachline in file:
        s.add(eachline.rstrip('\n'))

if __name__ == '__main__':
    define()
    temp = raw_input()
    for i in s:
        if(temp.count(i)>0):
            l = len(i.decode('utf-8'))
            t = ""
            for j in range(l):
                t = ''.join(('*',t))
            temp = temp.replace(i,t)
    print temp
