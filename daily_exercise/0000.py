#在一张图片的右上角加一个数字
from PIL import Image,ImageDraw,ImageFont

import random

def rndColor():
    return(random.randint(32,127),random.randint(32,127),random.randint(32,127))

image = Image.open("0000.jpg")
w,h = image.size
image.thumbnail((w/4,h/4))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Arial.ttf',36)

draw.text((w/4-100,60),'1',font = font,fill = rndColor())
image.save('after_0000.jpg','jpeg')

