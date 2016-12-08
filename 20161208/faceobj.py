#coding=utf-8
'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])

定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''

class Listinfo(object):
    def __init__(self,list):
        self.list = list
    def add_key(self,keyname):
        self.keyname = keyname
        self.list.append(keyname)
        return self.list
    def get_key(self,num):
        self.num = num
        return self.list[num]
    def updata_list(self,listnew):
        self.listnew = listnew
        return self.list + self.listnew
    def del_key(self):
        return self.list.pop(len(self.list)-1) 
        
list_info = Listinfo([44,222,111,333,454,'sss','333'])
print list_info.add_key('aaa')
print list_info.get_key(3)
print list_info.updata_list([1,'heihei',2,5])
print list_info.del_key()