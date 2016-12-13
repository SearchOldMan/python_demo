#coding=utf-8

import urllib
import re
from BeautifulSoup import BeautifulSoup as bs3
req = urllib.urlopen('http://money.163.com/special/pinglun/')

html = req.read()

data = dict()



e = bs3(html)



data['title'] = e.title

print data



            