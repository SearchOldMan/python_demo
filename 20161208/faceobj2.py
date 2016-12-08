#coding=utf-8
'''
定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})



'''

class dictclass(object):
    def __init__(self,**dic):
        self.dictory = dic
    def del_dict(self,key):
        self.key = key
        del self.dictory[key]
        return self.dictory
    def get_dict(self,key):
        if key in self.dictory:
            return self.dictory[key]
        else:
            return 'not found'
    def get_key(self):
        return self.dictory.keys()
    
dict = dictclass(name='zhangsan',key1='value1',key2='value2')

print dict.del_dict('name')

print dict.get_dict('name')

print dict.get_dict('key1')

print dict.get_key()
