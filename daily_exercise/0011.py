# -*- coding: utf-8 -*-

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

s = set()

def define():
    file = open("filtered_words.txt")
    for eachline in file:
        s.add(eachline.rstrip('\n'))

if __name__ == '__main__':
    define()
    temp = raw_input()
    if temp in s:
        print 'Freedom'
    else:
        print 'Human Rights'
