import urllib
from HTMLParser import HTMLParser
class Scraper(HTMLParser):
    flag = False
    def handle_starttag(self,tag,attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.flag = True
            self.chunks = []
            self.url = attrs['href']
    def handle_endtag(self,tag):
        if tag == 'a' and self.flag:
            print '%s (%s)' % (''.join(self.chunks),self.url)
            self.flag = False
    def handle_data(self,data):
        if self.flag:
            self.chunks.append(data)

response = urllib.urlopen('http://www.iqiyi.com','r')
html = response.read()

s = Scraper()
s.feed(html)