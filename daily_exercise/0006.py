# -*- coding: utf-8 -*-
#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os
import re

def getfile(path):
    filepath = os.listdir(path)
    files = []
    for i in filepath:
        fpath = path+'/'+i
        if(os.path.isfile(i) and i.endswith('.txt')):
            files.append(fpath)
        elif(os.path.isdir(i)):
            files += getfile(fpath)
    return files

def find_result(files):
    worddict = {}
    for i in files:
        f = open(i)
        s = f.read()
        temp = r'[a-zA-Z0-9]+'
        result = re.findall(temp,s)
        for j in result:
            worddict[j] = worddict[j]+1 if j in worddict else 1
        f.close()
    worddict = sorted(worddict.items(), key=lambda e: e[1], reverse=True)
    return worddict

if __name__ == '__main__':
    files = getfile('.')
    result =find_result(files)
    maxium = 1
    for i in range(len(result)-1):
        if result[i][1] == result[i+1][1]:
            maxium += 1
        else:
            break

    for i in range(maxium):
        print result[i]