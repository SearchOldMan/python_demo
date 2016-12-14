#coding=utf-8

from wsgiref.simple_server import make_server
from helloworld import application

httpd = make_server('', 8000, application)

print 'http server post is in 8000'
httpd.serve_forever()