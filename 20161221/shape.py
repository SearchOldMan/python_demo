#coding=utf-8
class Rectangle():
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            self.__dict__[name] = value

    def area(self):
        return self.width * self.height


r1 = Rectangle(13,20)
r1.square = 10
print r1.area()
