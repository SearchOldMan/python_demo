#coding=utf-8
'''
定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''
a = set([1,3,4,5])
class Setinfo(object):
    
    
    def add_setinfo(self,keyname):
        self.keyname = keyname
        a.add(keyname)
        return a
    def get_intersection(self,s):
        self.s = s
        return a & self.s
    def get_union(self,b):
        self.b = b
        return a | self.b

setinfo = Setinfo()
print setinfo.add_setinfo('abc')
print setinfo.get_intersection(set([3,4,1,7,12]))
print setinfo.get_union(set([1,5,'heeeello']))
    
    