
#!usr/bin/env python
# -s-coding:utf-8 -s-
'a hello module'
__author__ = 'My.lai'
import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print 'hello world'
	elif len(args) == 2:
		print 'hello,%s!'%args[1]
	else:
		print 'Too many arguments!'
if __name__ == '__main__':
	test()