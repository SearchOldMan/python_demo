#coding=utf-8

#习题二:
#1 用os模块的方法完成ping www.baidu.com 操作。
#2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"。


import os

def kouzhang(dirpwd):
    
    f = open(dirpwd,'r')
    result = f.read()
    f.close()
    return result

url = 'E:\learngit\python_demo\README.md'

print kouzhang(url)
