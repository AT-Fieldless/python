# -*- coding: utf-8 -*-

#使用 Python 生成类似于下图中的字母验证码图片

import string
import random
from PIL import Image,ImageDraw,ImageFilter,ImageFont

def rndchar():
    return random.choice(string.letters)

def rndcolour():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndcolour2():
    return (random.randint(1,127),random.randint(1,127),random.randint(1,127))

def solve():
    width = 60*4
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('/Users/apple/anaconda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf',36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndcolour())
    for i in range(4):
        draw.text((60*i+10,10),rndchar(),font=font,fill=rndcolour2())
    image = image.filter(ImageFilter.BLUR)
    image.save('0010.jpg','jpeg')

if __name__=='__main__':
    solve()