#!/usr/bin/env python
#coding=utf-8
#邮件内置模块
import smtplib

mail_server = 'localhost'
mail_server_port = 25
from_addr = '1161938933@qq.com'
to_addr = 'apple_username@163.com'

#要发送的头部格式
from_header = 'From:%s\r\n' % from_addr
to_header = 'To:%s\r\n\r\n' % to_addr

#要发送的标题
subject_header = 'Subject:nothing is happend!'
content = 'haha'

email_message = "%s\n%s\n%s\n\n%s" % (from_header,to_header,subject_header,content)

#创建email的对象
s = smtplib.SMTP(mail_server,mail_server_port)
s.sendmail(from_addr,to_header,email_message)