from wsgiref.simple_server import make_server
from hello import application

httped = make_server('', 8000, application)
print 'server HTTP on port 8000'
httped.serve_forever() 