#coding=utf-8
def tuzi(n):
    if n<1:
        print '输入错误'
        return -1
    if n ==1 or n ==2:
        return 1
    else:
        return tuzi(n-1) + tuzi(n-2)

result = input('请输入：')
if tuzi(result) != -1:
    print "有%d对兔子"%tuzi(result)