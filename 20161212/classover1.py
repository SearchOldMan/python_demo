#coding = utf-8

#1.1 用time模块获取当前的时间戳.
#1.2 用datetime获取当前的日期，例如：2013-03-29
#1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27

import time
from datetime import date
t1 = time.time()
print t1

t2 = date.today()
print t2


