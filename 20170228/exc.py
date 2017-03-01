#coding=utf8
a = [1,3,4,5,6,7]
try:
	print a[1]
except:
	print u'出错咯'
else:
	print u'正确'
finally:
	print u'结束了'