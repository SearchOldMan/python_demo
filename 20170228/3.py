#coding=utf-8

class boy(object):
	genous = 1
	def __init__(self,name):
		self.name = name

class girl(object):
	genous = 0
	def __init__(self,name):
		self.name = name

class love():
	def __init__(self,first,second):
		self.first = first
		self.second = second

	def meet(self):
		return '这是%s和%s的恋爱'%(self.first.name,self.second.name)

class normal_love(love):
	def __init__(self,first,second):
		if 1 != first.genous + second.genous:
			print '对象引入错误'
		else:
			love.__init__(self,first, second)

class gay_love(love):
	def __init__(self,first,second):
		if 2 != first.genous + second.genous:
			print '对象引入错误'
		else:
			love.__init__(self,first, second)

class girl_love(love):
	def __init__(self,first,second):
		if 0 != first.genous + second.genous:
			print '对象引入错误'
		else:
			love.__init__(self,first, second)

xiaoming = boy('小明')
xiaohong = girl('小红')

normal = normal_love(xiaoming, xiaohong)
print normal.meet()
