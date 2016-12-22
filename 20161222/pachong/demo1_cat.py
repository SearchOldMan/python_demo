#coding=utf-8
'''
the request net is http://www.placekitten.com/g/200/300
'''
import urllib

response = urllib.urlopen('http://www.placekitten.com/g/200/300')

cat_img = response.read()

with open('E:\\learngit\\python_demo\\20161222\\cat_500_600.jpg','wb') as f:
    f.write(cat_img)

