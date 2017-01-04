## 零、开发的软件：Wingide
+ 解决python的中文编码乱码问题：
1.点击debug
2.点击右边出现的扳手形状的按钮
3.新出现的窗口中间的option点击
4.选择utf-8编码。endoce('utf-8')把其他编码转成utf8的格式；decode（'utf-8'）是把utf8解码成其他编码格式
## 一、第一个python程序：
    >>> 100+200
    >>> print 'hello world'
## 二、输入
    name = raw_input()
## 三、转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
## 四、指令：
+ 1.list:一个有序的集合，下标从0开始，list[-1]最后一个元素。增删改全部跟js一样.-----------列表
```
    a.list[0],list[1]....  //查
    b.len(list)  //长度
    c.list.append(new);  //增（追加）
    d.list.insert([index],new);  //增（前加）
    e.list.pop([index]);  //删除
    f.list[index] = 'new';  //改
    g.list2.extend(list)  //在原有的基础上追加，不创建新的列表
    h.del list:删除列表对象的引用
    i.del [:]:产出列表的元素
```
+ 2.tuple：也是一个有序的数据，格式是(),一旦初始化，就不可以改变，除了没有append,insert,其他跟list一样 ------元组
```
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```
+ 3.判断语句
```
if num>10
    print xxx;
    print x
```
用elif带替else if.range(num)按照顺序生成有序的数组。特别注意一点：python更多的使用：代替{}
+ 4.dict:格式跟定义json一样，采用key-value的形式。访问：dict[key];dict的key必须是不可变的参数 ------字典
```
student = {'aa':12,'vv',2344}
student[aa]
```
#### dict的操作
##### a. del student[a] #删除某个元素
##### b. student.clear() #清空所有的元素
##### c. student.pop('aa') #返回键对应的值。注意：pop操作的列表是最原始的列表
##### d. student.get('aa') #返回的是键的值
e. student.keys() #返回的是student的key列表
+ 5.set:要创建一个set，需要提供一个list作为输入集合:创建一个key不重复的集合  -------集合
```
>>> s = set([1, 2, 3])
>>> s
set([1, 2, 3])
```
    a.  s.add(4)   //增加元素
    b.  s.remove(key)  //删除元素
    c.s1 & s2,s1 | s2
    d.in  成员关系  
    >>>1 in a
    >>>True
+ 6.字符串的替换：
a.replace方法

b.maketrans('old','new') #翻译表
```
import string
a = '1234456'
g = string.maketrans('123','qwe')
a.translate(g) #'qwe4456'
```
## 4.2 字符串拼接
+ +:'str1'+'str2'
+ %s:占位符
```
s = 'my name is %s,i love %s',%('python','apple')
```
+ format()
```
'mu name is {0},i love {1}'.format('apple','python')
```
+ join:
```
''.join('abc','heha')
```
+ 7.python的内置方法：
###### a.len('str')
###### b.max(list)
###### c.min(turple)
###### d.sum(list)
###### e.sorted(list)
###### f.enumerate(list) #枚举
###### g.list(turple)
###### h.turple(list)
###### i.zip(list1,list2) #对应组合
五、函数
+ 函数由函数名和变量组成;
```
abs(10)  ---> 10
abs(-10)  ---> 10
cmp(1,2)  ---> -1

```
+ python提供了数据类型转换的方法
```
int('12')  --> 12
float('1.23')  ---> 1.23
bool('aa')  ---> true
bool('') ---> false
```
+ 函数可以设置默认参数，减少函数调用时的复杂度。
```
def main(name,sex,age=4,city="beijing"):
    print 'name',name;
    print 'sex',sex

main('zhangsan','男')
```
+ 函数参数匹配：使用以下几种匹配方式：
##### 1.常规参数的顺序匹配
##### 2.默认参数的顺序匹配,调用函数时如果未传入参数，就按照默认参数的值
##### 3.**,*之类的参数匹配，要在对应的位置传入实参
+ 递归函数：如果我们在使用递归时可能出现栈内存泄漏的问题，我们使用尾递归处理
```
def fact(n):
	return fact_ater(n,1)
def fact_ater(num,result):
	if num == 1:
		return result
	else:
```
+ **,*的用法：**表示dict;*表示元组
```
def test(**kr):
    return kr

text(name='zhagsan',age=12,score=78)

{name:'zhangsan',age:12,score:78}
```
*表示元组
```
def text(*z):
    return z
test(12,36,6):
    
(12,36,6)
```
## 六、高级特性:
+ 切片：
```
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
```
```
L[:10:2]  //前十个数，每两个取一个
L[::4]  //所有的数，每4个取一个
```
+ 迭代：for ... in ... 遍历dirc。
```
d = {'a':1,'v':2,'e':3}
for k in d:
print k;


for value in d.itervalues:   //得到value
print value;

for k,v in d.iteritems:    //得到key和value
print k,v
```
a.判断一个对象是不是可迭代对象：
```
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```
b.如果要把一个list对象也像dirc一样迭代，python提供了一个方法enumerate
```
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print i, value
...
0 A
1 B
2 C
```
c.列表生成式：实际上就是在合理的应用for循环
```
[(x,y) for x in range(3) for y in range(3) if x%2==0 and y%2==0]
>>>[(0,0),(0,2),(2,0),(2,2)]
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


```
d.生成器：如果把列表生成式中的[]换成()，就是一个generator.如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator.send('')当yield里面没有返回值时，send函数就会把里面的东西替代yield要返回的内容
```
>>> g = (x * x for x in range(10))
>>>g
0,1,4,9...

>>> def odd():
...     print 'step 1'
...     yield 1
...     print 'step 2'
...     yield 3
...     print 'step 3'
...     yield 5
...
>>> o = odd()
>>> o.next()
step 1
1
>>> o.next()
step 2
3
>>> o.next()
step 3
5
```
##  七、高阶函数：可以在一个自定义函数中调用另外一个函数
```
def my_abs(x,y,f):
    return f(x)+f(y)
    
my_abs(10,-10,abs)

```
a.map(fn,list[]):fn函数作用于list列表的每个元素，生成一个新的list
```
def f(x):
    return x*x;
map(f,[1,2,3....])
```

b.reduce(fn,[x1,x2,x3])调用函数多次，把第一次的计算的结果当做参数传进去当做第二次的参数.

c.filter:和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

d.sorted:对list或者str排序，可以传入自定义的函数，实现排序规则
```
def reverse(x,y):
    if x<y:
        return 1
    elif x=y:
        return 0
    else:
        return -1
sorted([12,32,56,33,3],reverse)
```
## 八、匿名函数：没有函数名的函数:
```
>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
+ 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
## 九、偏函数：就是把一个函数的默认参数改掉，以便我们下次调用时方便，不用再设置参数
```
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```
## 十、模块：
+ python的内置模块，我们在命名模块时不能与其同名。[点击这里](https://docs.python.org/2/library/functions.html)
+ 自定义模块：
```
#!usr/bin/env python
# -s-coding:utf-8 -s-
'a hello module'
__author__ = 'My.lai'
import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print 'hello world'
	elif len(args) == 2:
		print 'hello,%s!'%args[1]
	else:
		print 'Too many arguments!'
if __name__ == '__main__':
	test()
```
+ 添加第三方模块：如：Python Imaging Library处理图形的模块
```
pip install PIL
```
## 十一、面向对象编程
+ 面向对象的三大特征：封装、继承、多态
+ 格式:
```
class Student(object):   //object是类继承哪个类
    def __init__(self,name,score):  //参数self是固定的参数，指向类本身
        self.name = name;
        slef.score = score;

student = Student()  //实例化
```
+ 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
```
class Student(object):   //object是类继承哪个类
    def __init__(self,name,score):  //参数self是固定的参数，指向类本身
        self.__name = name;
        slef.__score = score;

student = Student()  //实例化

>>> self.__name   //私有变量，访问不到
```
+ 析构函数：释放变量占用的内存
```
def __del__:
    del self.name
    del self.age
```
+ isinstance('animal',str)判断animal是不是str类型
+ type()获取对象类型,phthon提供了一个获取类型的模块
```
>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True
```
+ dir()获取对象的属性和方法，接着配合hasattr(),setattr(),getattr()对属性操作
```
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```
## 十二、高级面向对象编程
+ 面向对象可以给子类实例添加方法，但是对后来的实例对象是无效的。
```
def set_score(score):
    return score
class Student(object):
    pass
s = Student()
form types import MethodType
s.set_score = MethodType(set_score,s,Student)
s.set_score(23)
>>>23
```
+ __slots__:定义实例化对象可以赋值的属性
```
class Student(object):
    __slots__:('name','age')
s = Student()
s.name = 'kangkang'
s.age = 12
s.score = 34
>>>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```
+ __init__(self):#构造方法
+ __repr__(self):#自定yi实例的输出
```
class Student():
    def __repr__(self):
        print 'cuo'
s = Student()
>>> s
>>> cuo
```
+ @property负责把一个方法变成属性来使用
```
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```
+ 多继承：就是让子类有多个父类，同时拥有多个父类的方法和属性：
```
class Animal(object):
    pass
class FlyableMixin(object):
    pass
class Dog(Animal,FlyableMixin):
    pass
```
+ __fn__(self,....):类似这种两个_的函数在python是不能随便乱用的
```
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
```
*通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。*
```
>>> callable(Student())
true
>>> callbale(max)
true
>>> callable('none)
false
>>> callable('string')
false
```
## 十三、错误、调试和测试
+ 错误：我们使用try...except...finally来处理错误，如果try代码运行时出现错误，被except捕捉到那就执行except的代码，再执行finally代码
```
try:
    print 'try...'
    r = 10/0
    print 'result:',r
except ZeroDivisionError, e:
    print 'except...',e
finally:
    print 'finally'
print 'end'
```
+ 调试：一个比较常见和好用的方式：在执行py文件时，开启pdb调试
```
python -m pdb err.py
>>> l  //显示代码
>>> n  //单步执行代码
>>> p 参数  //查看变量的值
```
*我们可以在可能会出错的地方设置pdb.set_trace()，实际上就是断点，c继续运行*

## 十四、读写文件
```
f = open('dirs/user/demo.txt','r')
f.read()
f.close()
```
+ 使用with代替close来关闭文件
```
with open('/path/to/file', 'r') as f:
    print f.read() 
```
+ 文件编码：python提供了一个自动帮我们读取文件编码的模块
```
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'
```
+ 写文件：与读文件类型，区别在传入参数'w',或者''wb'
```
f = open('dirs/path/user/demo/index.html','w')
```

```
b.操作文件目录
import os
+ os.path.abspath('.')   //当前文件所在的决对路径
+ os.mkdir('')  //创建文件
+ os.rmdir('')  //删除文件
+ os.path.join('','')  //拼接文件路径
```
c.python对象转化成json对象
```
import json
f = dirc(name='zhagsan',age=12,score=90)
json.dumps(f)
{"name":"zhagsan","age":12,"score":90}
```
d.把一个json对象反序列化成python对象
```
json_str = '{"name":"zhagsan","age":12,"score":90}'
json.load(json_str)
{u'age': 20, u'score': 88, u'name': u'Bob'}
```
e.类的实例化对象json序列化

```
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
```
#### 在外面函数就对s的参数进行json格式的定义
## 十五、进程和线程
+ 进程间的通信：
```
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```
## 十六、正则表达式
+ .表示匹配任何字符
+ *表示匹配任何个数的字符，包括0个
+ +表示匹配至少一个字符
+ ?表示0个或1个字符
+ {n}表示匹配n个
+ {n,m}表示匹配n-m个字符
+ \s空格,\d数字,\w数字或者字母
+ []表示范围
```
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
```
+ ^表示行的开头，^\d表示必须以数字开头。
+ $表示行的结束，\d$表示必须以数字结束。
+ 使用Python的r前缀，就不用考虑转义的问题了：
```
s = r'ABC\-001' # Python的字符串
```
+ re.match()测试正则表达式是否可以匹配上
```
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'
```
+ 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group)
```
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object at 0x1026fb3e8>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
```
## 十七、常见內建模块
### 1.collections
+ namedtuple 定义各种各样的类，告诉解释器这是什么
```
from collections import namedtuple
Point = namedtuple('Point',['x','y'])  //定义了一个类
point = Point(1,30)  //类的实例化
point.x   //1
point.y  //30
```
+ deque 是对list列表增加和删除元素，非常适合对列和栈
```
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q = deque(['y','a','b','c','x'])
```
+ defaultdict:使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
+ OrderedDict:使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
+ counter:Counter是一个简单的计数器，例如，统计字符出现的个数：
```
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```
#### 2.itertools:用于操作迭代对象的模块
+ itertools.count(1) //无线计数
```
import itertools
natural =  itertools.count(1)
for n in natural:
    print n
```
+ itertools.cycle()会把传入的一个序列无限重复下去:
```
>>> import itertools
>>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
>>> for c in cs:
...     print c
...
'A'
'B'
'C'
'A'
'B'
'C'
```
+ itertools.repeat('a',10)  //重复打印传入的字符，传入第二个参数就限定了次数
```
>>> ns = itertools.repeat('A', 10)
>>> for n in ns:
...     print n
...
打印10次'A'
```
+ chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
```
for c in itertools.chain('ABC', 'XYZ'):
    print c
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
```
+ imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
```
>>> for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
...     print x
...
10
40
90
```
## 十八、常用的第三方模块
+ PIL模块windows平台需要到官方网站下载exe
```
import Image
# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('/Users/michael/test.jpg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/michael/thumbnail.jpg', 'jpeg')
```
## 十九、图形界面
#### 使用python内置的Tkinter图形界面
```
from Tkinter import * //从Tkinter包的所有内容
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()   //把Widget加入到父容器中
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')  //标签
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)  //按钮
        self.quitButton.pack()
# 实例化
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
```
```
from Tkinter import *
# tkMessageBox模块
import tkMessageBox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text = 'hello',command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message','Hello,%s'%name)

app = Application()

app.master.title('Hello World')

app.mainloop()
```
## 二十、网络编程
#### TCP编程
```
# 服务端
import socket
# 建立基于ipv4和TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建端口号
s.bind(('127.0.0.1',9000))
# 监听端口,参数规定每次传入的个数
s.listen(5)
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
# 客户端
import socket
#建立socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建议链接
s.connect(('127.0.0.1',9000))
#发送数据
print s.recv(1024)
for data in ['Michael','Tracy','Sarch']:
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()
```
#### UDP编程
```
# 服务端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9000))
print 'Bind UDP on 9000'
while True:
	data,addr = s.recvfrom(1024)
	print 'Recived from %s:%s'%addr
	s.send('Hello,%s!' %data)
# 客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['kangkang','zhangsan','Mick']:
	s.sendto(data,('127.0.0.1',9000))
	print s.recv(1024)
s.close()
```
## 二十一、电子邮件
## 二十二、使用内置的数据库
+ python 有一套内置的数据库sqlite3
```
import sqlite3
#连接到数据库
conn = sqlite3.connect('test.db')
# 创建游标
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20)')
# 执行一条SQL语句，插入一条数据
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
>>> cursor.rowcount
1
# 关闭Cursor:
>>> cursor.close()
# 提交事务:
>>> conn.commit()
# 关闭Connection:
>>> conn.close()


# 查询插入的数据
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
# 执行查询语句:
>>> cursor.execute('select * from user where id=?', ('1',))
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor.fetchall()
>>> values
[(u'1', u'Michael')]
>>> cursor.close()
>>> conn.close()
```
+ 使用MySQL
调用我们自己的数据库时，我们要先安装mysql的驱动，两个任选一个都可以
```
easy_install mysql-connector-python
easy_install MySQL-python
```
下面就以mysql-connnecot为例
```
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))
>>> values = cursor.fetchall()
>>> values
[(u'1', u'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()
```
## 二十三、Web开发
+ python内置了一个比较简单的WSGI服务器，python完全可以忽略底层怎么实现http请求的代码，专注于返回什么就行了
```
def application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>')

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()
```
+ 处理不同的url地址，使用web的框架会比较简单
```
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
```
+ 常见的Python Web框架还有：

1.Django：全能型Web框架；

2.web.py：一个小巧的Web框架；

3.Bottle：和Flask类似的Web框架；

4.Tornado：Facebook的开源异步Web框架。
+ mvc实现web框架
```
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
```
除了Jinja2，常见的模板还有：

Mako：用<% ... %>和${xxx}的一个模板；

Cheetah：也是用<% ... %>和${xxx}的一个模板；

Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
## 二十四、python的语句
+ print:基本的输出语句
```
print 'a',
print 'b',#逗号是为了让输出不换行

f =  open('test.txt','w')
print >>f,'adaer'  #>>往文件里面写入内容
```
+ global关键字：定义全局的变量

## 二十五、python一些内置的模块：
### 1.urllib:操作地址栏地址的模块：
        quote_plus(s, safe='')
        Quote the query fragment of a URL; replacing ' ' with '+'
    
    splitattr(url)
        splitattr('/path;attr1=value1;attr2=value2;...') ->
        '/path', ['attr1=value1', 'attr2=value2', ...].
    
    splithost(url)
        splithost('//host[:port]/path') --> 'host[:port]', '/path'.
    
    splitnport(host, defport=-1)
        Split host and port, returning numeric port.
        Return given default port if no ':' found; defaults to -1.
        Return numerical port if a valid number are found after ':'.
        Return None if ':' but not a valid number.
    
    splitpasswd(user)
        splitpasswd('user:passwd') -> 'user', 'passwd'.
    
    splitport(host)
        splitport('host:port') --> 'host', 'port'.
    
    splitquery(url)
        splitquery('/path?query') --> '/path', 'query'.
    
    splittag(url)
        splittag('/path#tag') --> '/path', 'tag'.
    
    splittype(url)
        splittype('type:opaquestring') --> 'type', 'opaquestring'.
    
    splituser(host)
        splituser('user[:passwd]@host[:port]') --> 'user[:passwd]', 'host[:port]'.
    
    splitvalue(attr)
        splitvalue('attr=value') --> 'attr', 'value'.
    
    thishost()
        Return the IP address of the current host.
    
    unquote(s)
        unquote('abc%20def') -> 'abc def'.
    
    unquote_plus(s)
        unquote('%7e/abc+def') -> '~/abc def'
    
    unwrap(url)
        unwrap('<URL:type://host/path>') --> 'type://host/path'.
    
    url2pathname(url)
        OS-specific conversion from a relative URL of the 'file' scheme
        to a file system path; not recommended for general use.
    
    urlcleanup()
    
    urlencode(query, doseq=0)
        Encode a sequence of two-element tuples or dictionary into a URL query string.
        
        If any values in the query arg are sequences and doseq is true, each
        sequence element is converted to a separate parameter.
        
        If the query arg is a sequence of two-element tuples, the order of the
        parameters in the output will match the order of parameters in the
        input.
    
    urlopen(url, data=None, head=None,proxies=None, context=None)
        Create a file-like object for the specified URL to read from.
     reporthook=None, data=None, context=None)
        head 是访问页面是请求的对象：网页还是程序
### 2.urlparse:
    FUNCTIONS
        parse_qs(qs, keep_blank_values=0, strict_parsing=0)
        Parse a query given as a string argument.
        
        Arguments:
        
        qs: percent-encoded query string to be parsed
        
        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.
            A true value indicates that blanks should be retained as
            blank strings.  The default false value indicates that
            blank values are to be ignored and treated as if they were
            not included.
        
        strict_parsing: flag indicating what to do with parsing errors.
            If false (the default), errors are silently ignored.
            If true, errors raise a ValueError exception.
    
    parse_qsl(qs, keep_blank_values=0, strict_parsing=0)
        Parse a query given as a string argument.
        
        Arguments:
        
        qs: percent-encoded query string to be parsed
        
        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.  A
            true value indicates that blanks should be retained as blank
            strings.  The default false value indicates that blank values
            are to be ignored and treated as if they were  not included.
        
        strict_parsing: flag indicating what to do with parsing errors. If
            false (the default), errors are silently ignored. If true,
            errors raise a ValueError exception.
        
        Returns a list, as G-d intended.
    
    urldefrag(url)
        Removes any existing fragment from URL.
        
        Returns a tuple of the defragmented URL and the fragment.  If
        the URL contained no fragments, the second element is the
        empty string.
    
    urljoin(base, url, allow_fragments=True)
        Join a base URL and a possibly relative URL to form an absolute
        interpretation of the latter.
    
    urlparse(url, scheme='', allow_fragments=True)
        Parse a URL into 6 components:
        <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
        Note that we don't break the components up in smaller bits
        (e.g. netloc is a single string) and we don't expand % escapes.
    
    urlsplit(url, scheme='', allow_fragments=True)
        Parse a URL into 5 components:
        <scheme>://<netloc>/<path>?<query>#<fragment>
        Return a 5-tuple: (scheme, netloc, path, query, fragment).
        Note that we don't break the components up in smaller bits
        (e.g. netloc is a single string) and we don't expand % escapes.
    
    urlunparse(data)
        Put a parsed URL back together again.  This may result in a
        slightly different, but equivalent URL, if the URL that was parsed
        originally had redundant delimiters, e.g. a ? with an empty query
        (the draft states that these are equivalent).
    
    urlunsplit(data)
        Combine the elements of a tuple as returned by urlsplit() into a
        complete URL as a string. The data argument can be any five-item iterable.
        This may result in a slightly different, but equivalent URL, if the URL that
        was parsed originally had unnecessary delimiters (for example, a ? with an
        empty query; the RFC states that these are equivalent).
        
### 3.time,datetime #时间
### 4.sys #系统有关
### 5.logging #日志
### 6.json #序列化
### 7.pickle #以二进制的编码方式写入文件
### 8.os #操作与文件夹相关和不同操作系统
### 9.fileinput #文件的每一行
### 10.random #随机数
### 11.shelve #往硬盘里面写入文件
### 12.re #正则表达式
```
compile(pattern, flags=0)
        Compile a regular expression pattern, returning a pattern object.
    
    escape(pattern)
        Escape all non-alphanumeric characters in pattern.
    
    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.
        
        If one or more groups are present in the pattern, return a
        list of groups; this will be a list of tuples if the pattern
        has more than one group.
        
        Empty matches are included in the result.
    
    finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a match object.
        
        Empty matches are included in the result.
    
    match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning
        a match object, or None if no match was found.
    
    purge()
        Clear the regular expression cache
    
    search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning
        a match object, or None if no match was found.
    
    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.
    
    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.
    
    subn(pattern, repl, string, count=0, flags=0)
        Return a 2-tuple containing (new_string, number).
        new_string is the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in the source
        string by the replacement repl.  number is the number of
        substitutions that were made. repl can be either a string or a
        callable; if a string, backslash escapes in it are processed.
        If it is a callable, it's passed the match object and must
        return a replacement string to be used.
    
    template(pattern, flags=0)
        Compile a template pattern, returning a pattern object
```

### 13.cgi #编写动态网页
    ++详细请查看官方文档++
+ 1.我们自定义的模块要放在python.exe的根目录下
2.  a.import   模块名 b.from 模块名 import 函数名  c.import 模块名 as 新名字
3.  定义包名：在python的运行环境下新建一个包（文件夹），然后把模块文件、新建的一个__init__.py放进包里面，__init__里面定义__all__来限制哪些模块的文件可以进出。最后通过import 包名.模块名导入
### 14.数据的永久性存储，序列化 ----pickle
```
#写入
import pickle
my_list = [1,2,(3,4),{'name':'zhangsan'}]
pickle_file = open(path,'wb')
pickle.dump(my_list,pick)_file)
#读取
pickle_file = open(path.'rb')
pickle.load(pickle_file)
```
### 15.shelve
```
import shelve
d = shelve.open('example.s')
d['key'] = 'some_value'
d.close()
d2 = shelve.open('example.s')
print d2
```
## 二十六、Django
+ 使用eclipse[推荐下载网址](https://www.eclipse.org/downloads/)
+ 新建项目的时候必须要django-admin.py拷贝到要新建文件夹的父级目录下，也就是跟即将新建的目录在同一文件夹下
+ django1.9版本的已经将使用模块新建表的命令从python manage.py syncdb改成python  manage.py migrate
+ 新建管理数据库的用户：
```
pythion manage.py createsuperuser
```
+ setting.py文件里面需要配置模板的路径、项目实例的名字

