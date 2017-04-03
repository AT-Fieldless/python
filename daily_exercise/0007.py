# -*- coding: utf-8 -*-

#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re

def find_answer(path):
    if not os.path.isdir(path):
        return
    temp = r'^#.*'
    file_list = os.listdir(path)
    print ("%s\t%s\t%s\t%s" % ('file', 'all_lines', 'space_lines', 'exp_lines'))
    for i in file_list:
        filename = os.path.join(path,i)
        if os.path.isfile(filename) and os.path.splitext(filename)[1] == '.py':
            with open(filename) as f:
                all_lines,space_lines,exp_lines = 0,0,0
                for j in f.readlines():
                    all_lines += 1
                    if j.strip() == "":
                        space_lines += 1
                    else:
                        result = re.findall(temp,j.strip())
                        if result:
                            exp_lines += 1
            print ("%s\t%s\t%s\t%s" % (filename,all_lines,space_lines,exp_lines))

if __name__ == '__main__':
    find_answer('.')
