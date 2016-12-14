#coding=utf-8
def application(environ,start_response):
    from StringIO import StringIO
    stdout = StringIO()
    print environ
    print >>stdout,'hello,%s'%environ['PATH_INFO'][1:]
    
    start_response('200 OK',[('Content-Type','text/html')])
    
    return [stdout.getvalue()]