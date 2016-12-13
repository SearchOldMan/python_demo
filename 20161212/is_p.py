#coding=utf-8
'''
判断是不是素数
只能被1和本身整除的数
1不是素数
'''
def is_p(num):
    if num == 1:
        return u'1不是素数'
    elif num == 2:
        return u'2是素数'
    else:
        for i in xrange(2,num):
            if num % i == 0:
                return u'%s不是素数'%num
        
        return u'%s是素数'%num
    

print is_p(8)