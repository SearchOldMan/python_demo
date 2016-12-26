#coding=utf-8
import socket,asyncore
from asyncore import dispatcher
from asynchat import async_chat

port = 9992
name = 'TestChat'
class ChatSession(async_chat):
    def __init__(self):
        pass

class ChatServer(dispatcher):
    def __init__(self):
        pass

if __name__ == '__main__':
    #聊天服务实例
    s = ChatServer(port,name)
    try:
        asyncore.loop()
    except KeyboardInterrupt:print