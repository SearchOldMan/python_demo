class Student(object):

	def __init__(self,name,age,args):
		self.name = name
		self.age = age
		self.args = args

	def get_name(self):
		return self.name
	def get_age(self):
		return self.age

	def get_course(self):
		
		return max(self.args)

zm = Student('zhangming',20,[69,88,100])
print zm.get_name()
print zm.get_age()
print zm.get_course()


