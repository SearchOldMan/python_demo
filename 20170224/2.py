import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print 'hello world'
		print args[0]
	elif len(args) == 2:
		print 'hello,%s'%args[1]
	else:
		print 'too many arguments'

if __name__ == '__main__':
	test()