# -*- coding: utf-8 -*-

#第 0009 题：一个HTML文件，找出里面的链接

from bs4 import BeautifulSoup
import urllib2

if __name__=='__main__':
    url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find-all"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    result = soup.find_all('a')
    for i in result:
        print i
