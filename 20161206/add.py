#coding=utf-8
#a = raw_input(u'请输入整数')
def add(num1,num2):
	if isinstance(num1,int) and isinstance(num2,int):
		return num1 + num2
	else:
		return u'不是整数'


print add('sa',[12,3])