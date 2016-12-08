#coding=utf-8
'''
1.判断是不是字符串
2.比较长度大小
3.输出长度较小的字符串
'''
import string
def short_str(*kr):
    #过滤非字符串
    lis = filter(lambda s:isinstance(s, str), kr)
    #获取字符串的长度列表
    lis_len = [len(x) for x in lis]
    
    try:
        length = min(lis_len)
    except ValueError:
        return None
    else:
        #获取字符串长度最短的在长度列表的索引
        return lis[lis_len.index(length)]
    
assert short_str(222,1111,'xixi','hahahah')
assert short_str(7,'name','dasere')
assert short_str(1,2,3,4)
        