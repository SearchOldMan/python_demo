
from wsgiref.simple_server import make_server
from web import application

httpd = make_server('',8000,application)
print 'server HTTP on port 8000'
httpd.serve_forever()