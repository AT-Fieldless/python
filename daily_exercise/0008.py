# -*- coding: utf-8 -*-

#第 0008 题：一个HTML文件，找出里面的正文。

import urllib2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "http://beautifulsoup.readthedocs.io/zh_CN/latest/#name"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    print(soup.body.text.encode('GBK', 'ignore').decode('GBK'))
