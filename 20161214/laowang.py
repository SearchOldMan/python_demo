#coding=utf-8
'''
url = 'http://www.cnpythoner.com/post/319.html'
'''

import urllib
import re
#避免贪婪模式
r = re.compile(r'href="(http://www\.cnpythoner\.com.+?)"')
def get_url_from_laowang(url):
    try:
        
        opener = urllib.urlopen(url)
        content = opener.read()
        g = r.findall(content)
        opener.close()
        return g
    
    except:
        return []
    

def save_content_from_url(url):
    opener = urllib.urlopen(url)
    content = opener.read()
    opener.close()
    
    #建立文件
    filename = url.replace('http://','')
    filename = filename.replace('.','_')
    filename = filename.replace('/','|')
    
    #打开文件
    f = open('E:/learngit/python_demo/20161214/%s'%filename,'w')
    f.write(content)
    f.close()
    return

def get_and_save_content(url,data_cache,i):
    save_content_from_url(url)
    urls = get_url_from_laowang(url)
    for url in urls:
        if url not in data_cache:
            data_cache.append(url)
        else:
            continue
        i += 1
        get_and_save_content(url, data_cache, i)
    print u'urls长度是：%s'%len(urls)
    #return len(data_cache)
    return data_cache
    
if __name__ == "__main__":
    data_cache = []
    i = 0
    get_and_save_content('http://www.cnpythoner.com',data_cache, i)
        