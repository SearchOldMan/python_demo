import re
str = '201-154878'
if re.match(r'^\d{3}\-\d{3,8}$',str):
	print 'ok'
else:
	print 'error'