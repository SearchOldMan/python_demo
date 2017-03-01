import urllib
url = 'https://www.zhihu.com/'

html = urllib.urlopen(url)

print html.read().decode('utf-8')