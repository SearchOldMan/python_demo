#coding=utf-8

import urllib

from BeautifulSoup import BeautifulSoup

with open('demo.html') as html:
    soup = BeautifulSoup(html)
    content = soup.find(id='secondaryconsumers')
    print content.li.div.string
    