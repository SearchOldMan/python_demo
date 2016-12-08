#coding=utf-8
def cmpInt(*num):
    for i in num:
        if not isinstance(i,int):
            return 'type not Interge'
        else:
            pass
    a = sorted(num)
    return 'the max num is %s,the min num is %s'%(a[-1],a[0])

print cmpInt('a',[1,3,4],1,45)