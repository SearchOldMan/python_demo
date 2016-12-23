import urllib
from BeautifulSoup import BeautifulSoup as bs

response = urllib.urlopen('http://www.jiandan.net','r')
html = response.read()
soup = bs(html)

for a in soup('a'):
    print a

