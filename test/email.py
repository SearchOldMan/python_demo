import re

re_email = re.compile(r'\d+@[a-zA-Z]+\.com$')
if(re_email.match('1161938933@qq.com')):
	print 'ok'
else:
	print 'error'