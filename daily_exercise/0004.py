#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

ddict = {}
reobject = '\b?([a-zA-Z]+)\b?'

f = open('0004.txt','r')
fout = open('result_0004.txt','w')
result = re.findall(reobject, f.read())

for word in result:
    if not ddict.has_key(word.lower()):
        ddict[word.lower()] = max(result.count(word.lower()+word.upper()),result.count(word))
    else:
        ddict[word.lower()] = max(ddict[word.lower()],result.count(word.lower()+word.upper()),result.count(word))

for key in ddict:
    fout.write(key+':%s\n'%ddict[key])

f.close()
fout.close()