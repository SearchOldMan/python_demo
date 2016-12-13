#coding=utf-8
#定义一个生成器函数，函数里只能用yield，要求输出结果：

#step 1
#step 2 x=haha
#step 3 y=haha   
def display():
    print 'step 1'
    
    print 'step 2'
    yield 'x=haha'
    print 'step 3'
    yield 'y=haha'
    

a = display()
print a.next()
print a.next()