#coding=utf-8
'''
if name is not str,throw typeerror
else out
'''
import string
def capstr(name):
    if isinstance(name, str):
        return name.capitalize()
    else:
        raise TypeError,'not a string'


print capstr('liming')