#!usr/bin/env python
#coding=utf-8
import pickle

class MyClass(object):
    def __init__(self):
        self.data = []
    def __str__(self):
        return "custom class myclass data:%s" % str(self.data)

    def add_item(self,item):
        self.data.append(item)


myclass = MyClass()

myclass.add_item(1)
myclass.add_item(2)
myclass.add_item(3)

pickle_file_name = open('custom_class.pkl','w')
pickle.dump(myclass,pickle_file_name)
pickle_file_name.close()