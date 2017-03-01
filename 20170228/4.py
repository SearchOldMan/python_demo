import cgi
form = cgi.FieldStorage()
if 'name' not in form or 'addr' not in form:
	print '<h1>Error</h1>'
	print 'Please fill in the name and addr'
	
print "<p>name:", form["name"].value
print "<p>addr:", form["addr"].value 