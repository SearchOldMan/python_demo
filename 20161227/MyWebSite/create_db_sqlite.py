#!/usr/bin/env python
#coding=utf-8

import sqlite3

#创建数据库对象
conn = sqlite3.connect('bar.db')
#创建游标
curs = conn.cursor()
#数据库指令
curs.execute('''
create table message(
    id integer primary key autoincrement,
    subject text not null,
    sender text not null,
    reply_to int,
    text text not null
)
''')
#插入数据
sender = u'王先生'
subject = u'纪念抗战胜利'
text = u'我国今年高规格纪念抗战胜利，国家主席等常委全部出席'
query = 'insert into message (sender,subject,text) values (?,?,?)'
curs.execute(query,(sender,subject,text))

sender = u'郭先生'
subject = u'有人在这里吗？'
text = u'这是我的消息内容'
query = 'insert into message (sender,subject,text) values (?,?,?)'
curs.execute(query,(sender,subject,text))

sender = u'刘先生'
subject = u'向抗战英烈进献花篮'
text = u'国家主席等常委向英烈进献花篮'
query = 'insert into message (sender,subject,text,reply_to) values (?,?,?,1)'
curs.execute(query,(sender,subject,text))
conn.commit()
conn.close()