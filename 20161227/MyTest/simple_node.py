#coding=utf-8

'''
http://localhost:4242
'''
from xmlrpclib import ServerProxy #服务代理
from os.path import isfile,join
from SimpleXMLRPCServer import SimpleXMLRPCServer #简单的远程方法调用服务
from urlparse import urlparse #url解析
import sys

MAX_HISTORY_LENGTH = 6 #设置最大的联系节点步骤为6步

OK = 1 #检查连接：通过
FAIL = 2 #检查链接：失败
EMPTY = '' #空值

#获取端口函数
def getPort(url):
    print url
    name = urlparse(url)[1]

    parts = name.split(':')
    return int(parts[-1])
#点对点类
class Node:
    def __init__(self,url,dirname,secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set() #创建一个已知的节点集合
    def query(self,query,history=[]):
        '''
        用于查找
        :param query:
        :param history:
        :return:
        '''
        code,data = self._handle(query)
        if code == OK:
            return code,data
        else:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH:
                return FAIL,EMPTY
            return self._broadcast(query,history)

    def hello(self,other):
        '''
        用于将传递的节点添加到已知的节点中
        :param other:
        :return:
        '''
        self.known.add(other)
        return OK

    def fetch(self,query,secret):
        '''
        用于让节点找到文件并下载
        :param query:
        :param secret:
        :return:
        '''
        if secret != self.secret:
            return FAIL
        code,data = self.query(query)
        if code == OK:
            f = open(join(self.dirname,query),'w')
            f.write(data)
            f.close()
        else:
            return FAIL
    def _start(self):
        '''
        创建一个远程服务的对象
        :return:
        '''
        s = SimpleXMLRPCServer(("",getPort(self.url)),logRequests=False)
        s.register_instance(self)#向服务器注册当前节点实例对象
        s.serve_forever()

    def _handle(self,query):
        '''
        处理请求函数
        :return:
        '''
        dir = self.dirname
        name = join(dir,query) #拼接文件的路径
        if not isfile(name):return FAIL,EMPTY
        return OK,open(name,'r').read()

    def _broadcast(self,query,history):
        '''
        当前的文件没有找到，就查询其他的
        :param query:
        :param history:
        :return:
        '''
        for other in self.known.copy():
            if other in history:continue
            try:
                s = ServerProxy(other)
                code,data = s.query(query,history)
                if code == OK:
                    return code,data
            except:
                self.known.remove(other)
        return FAIL,EMPTY

def main():
    url,directory,secret = sys.argv[1:]
    node = Node(url,directory,secret)
    node._start()

if __name__ == '__main__':main()