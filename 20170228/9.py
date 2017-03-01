#coding=utf8

class with_as_f(object):
	def __init__(self,name):
		self.name = name
	def __enter__(self):
		print u'haha'
		return self.name
	def __exit__(self,type,value,traceback):
		print u'退出'


we = with_as_f('zhangsan')
with we as f:
	print f
