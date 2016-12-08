#coding=utf-8
import urllib
def get_page(url):
    try:
        f = urllib.urlopen(url)
        s = f.read()
        f.close()
    except typeError:
        return 'error'
    finally:
        return s

print get_page('http://www.sina.com.cn/')