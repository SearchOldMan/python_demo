#coding=utf-8
import time as t
class T():
    def __init__(self):
        self.uint = ['年','月','日','时','分钟','秒']
        self.prompt = '未开始计时'
        self.longtime = []
        self.begin =0
        self.end = 0
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        print '计时开始'
    def stop(self):
        self.end = t.localtime()
        self._calc()
        print '计时结束'

    def _calc(self):
        self.longtime = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.longtime.append(self.end[index] - self.begin[index])
            if self.longtime[index]:

                self.prompt += str(self.longtime[index]+self.uint[index])
        print self.prompt

t1 = T()
t1.start()

t1.stop()
