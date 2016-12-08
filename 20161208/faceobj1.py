#coding=utf-8
'''
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99
'''
import itertools
class student(object):
    def __init__(self,name,age,**kr):
        self.name = name
        self.age = age
        self.score = kr
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_course(self):
        #迭代里面的分数
        score = self.score
        max_score_list = []
        for value in score.itervalues():
            max_score_list.append(value)
        max_score = max(max_score_list)
        return max_score
stu = student('zhangsan',13,chinese=80,math=30,english=90)

print stu.get_name()
print stu.get_age()
print stu.get_course()
        
            
    
    