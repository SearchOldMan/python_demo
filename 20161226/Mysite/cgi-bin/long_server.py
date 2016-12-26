#!/usr/bin/env python

import cgi

form =  cgi.FieldStorage()
text =  form.getvalue('text',open('data.dat').read())
f = open('data.dat','w')
f.write(text)
f.close()

print '''Content-Type=text/html\n
<html>
    <head><title>a simple demo</title></head>
    <body>
        <form action="long_server.py" method="get">
            <textarea rows="10" cols="20" name="text">%s</textarea><br>
            <input type="submit" value="submit">
        </form>
    </body>
</html>
''' % text