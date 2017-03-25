# coding=utf-8
# 爬取天气数据
import urllib
import re
page = urllib.urlopen('http://www.weather.com.cn/weather/101020100.shtml')
html = page.read()
page.close()

tianqi = '<p class="tem">(.)*<i>(.*)℃</i>'
html = str(html)
result = re.search(tianqi,result,re.S).group(0)
print result
