#coding=utf-8
'''
url = 'http://126.com/a?py=4'
'''

import urlparse
def qs(url):
    query = urlparse.urlparse(url).query
    
    return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])

print qs('http://126.com/a?py=4')

