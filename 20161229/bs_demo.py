#!/usr/bin/env python
#coding=utf-8

import BeautifulSoup
import urllib

response = urllib.urlopen('http://www.baidu.com')
html = response.read()

a_list = BeautifulSoup.BeautifulSoup.findAll()
print a_list