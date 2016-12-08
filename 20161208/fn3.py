#coding=utf-8
def get_num(num):
    odd = []
    if isinstance(num,list):
        for i in num:
            if i % 2 == 0:
                odd.append(i)
            else:
                pass
    else:
        return u'参数不是一个列表'
    
    return odd

print get_num([1,4,5,6,7])