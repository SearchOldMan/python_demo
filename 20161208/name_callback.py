#coding=utf-8
import string
def name_callback(name,callback=None):
    
    if callback == 'string.lower':
        return name.lower()
    elif callback == 'string.upper':
        return name.upper()
    else:
        return name.capitalize()


print name_callback('zhangsan')
print name_callback('lisi',callback='string.lower')
print name_callback('wangwu',callback='string.upper')

        