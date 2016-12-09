#coding=utf-8
'''
定义两个人的恋爱、婚姻、生育

男女
男男
女女

最小的节：男  女
'''

class Gender(object):
    #构造函数
    def __init__(self,person1,person2):
        self.person1 = person1
        self.person2 = person2
    #恋爱函数
    def love(self):
        return u'这是%s和%s的恋爱'%(self.person1.name,self.person2.name)
    #婚姻函数
    def marry(self):
        return u'这是%s和%s的婚姻'%(self.person1.name,self.person2.name)    
    #生育函数
    def children(self):
        return u'这是%s和%s的孩子'%(self.person1.name,self.person2.name)
#正常男女交往    
class Man_Woman(Gender):
    def __init__(self, person1, person2):
        if 1 != person1.gender + person2.gender:
            print '对象输入错误'
        else:
            Gender.__init__(self, person1, person2)
    
#男男交往    
class Man_Man(Gender):
    def __init__(self, person1, person2):
        if 2 != person1.gender + person2.gender:
            print '对象输入错误'
        else:
            Gender.__init__(self, person1, person2)


#女女交往    
class Woman_Woman(Gender):
    def __init__(self, person1, person2):
        if 0 != person1.gender + person2.gender:
            print '对象输入错误'
        else:
            Gender.__init__(self, person1, person2)

class boy(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
class girl(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


p1 = boy('老王', 1)
p2 = girl('凤姐', 0)

mw = Man_Woman(p1, p2)

print mw.love()
print mw.marry()
print mw.children()