'''
1.定义函数的参数类型
2.函数的处理：遍历参数，判断1-100以内的，取出偶数
'''
#coding=utf-8
l = [1,3,4,5,6,7,8,9,9,230,32,41,456,778]
new_odd = []
for i in l:
        if i>1 and i<100 and i%2 == 0:
            new_odd.append(i)
        else:
            pass
    


print type(new_odd)
print new_odd