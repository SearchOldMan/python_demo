#coding=utf-8

import urllib

f = urllib.urlopen('https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90%20%E7%94%B7&enc=utf-8&suggest=1.def.0.T05&wq=xie&pvid=inamcowi.lg6z3e')

content = f.read()

w = open('E:/learngit/python_demo/20161214/index.html','w')

w.write(content)

w.close()


