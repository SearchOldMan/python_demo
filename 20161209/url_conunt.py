#coding=utf-8
'''
计算url里面有多少个链接
'''
import urllib
def url_a_count(url):
    try:
        u = urllib.urlopen(url)
    except Exception as e:
        return u'该网页无法读取'
    else:
        r = u.read()
        
    return len(r.split('<a href='))-1

print u'该网页有%s个链接'%url_a_count('http://www.baidu.com')