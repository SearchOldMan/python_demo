#coding=utf-8
'''
读取url的内容，保存到path_folder文件夹下
'''
import urllib
import os
import random
def url_content(url,path_folder=None):
    try:
        u = urllib.urlopen(url)
    except Exception as e:
        return u'无法读取该网页'
    else:
        content = u.read()
    
    #判断是不是文件夹
    if not os.path.isdir(path_folder):
        return u'path_folder不是文件夹'
    else:
        random_filename = 'test_%s'%random.randint(1,1000)
        file_path = os.path.join(path_folder,random_filename)
        
        #写入
        w = open(file_path,'w')
        w.write(content)
        w.close()
        return file_path

print url_content('http://www.baidu.com', '/tmp')