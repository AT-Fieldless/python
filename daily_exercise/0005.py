#-*- coding: utf-8 -*-
'''
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''

import os
from PIL import Image

def change_resolution(path):
    for picname in os.listdir(path):
        picfile = os.path.join(path,picname)
        if picfile.split('.')[1] == 'jpg':
            with Image.open(picfile) as pic:
                w,h = pic.size
                n = w/1136 if (w/1136)>=(h/640) else h/640
                pic.thumbnail((w/n,h/n))
                pic.save('0005_'+picname.split('.')[0]+'.jpg','jpeg')

if __name__ == '__main__':
    change_resolution('/Users/apple/Documents/python/daily_exercise')
