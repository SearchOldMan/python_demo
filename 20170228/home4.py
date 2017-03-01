class Dictclass(object):
	def __init__(self,krags):
		self.krags = krags

	def del_dict(self,key):
		del self.krags[key]
		return self.krags
	def get_dict(self,key):
		if key in self.krags.keys():
			return self.krags[key]
		else:
			return 'not found'

dict = Dictclass({'a':1,'b':2,'c':5,'f':3})
print dict

print dict.del_dict('a')

print dict.get_dict('f')