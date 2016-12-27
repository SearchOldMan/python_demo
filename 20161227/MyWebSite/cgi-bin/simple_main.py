#!/usr/bin/env python
#coding=utf-8
print '''Content-Type=text/html\n'''

import cgitb;cgitb.enable()
import sqlite3,sys

conn = sqlite3.connect('bar.db')
conn.text_factory = str
curs = conn.cursor()
type = sys.getfilesystemencoding()

print '''
<html>
    <head><title>The Border Attention</title></head>
    <body>
        <h1>The Border Messsage list</h1>
</html>
'''
curs.execute('''
select * from message
''')
#使用游标的description得到每个人的元组
names = [d[0] for d in curs.description]
rows = [dict(zip(names,row)) for row in curs.fetchall()]

toplevel = [] #顶层公告列表容器
children = {} #子回复容器

for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:#顶层的公告
        toplevel.append(row)
    else:#子回复
       children.setdefault(parent_id,[]).append(row)

#缩进
def format(row):
    strcontent = row['subject']
    print (strcontent.decode('utf-8').encode(type))
    try:kids = children[row['id']]
    except KeyError:pass
    else:
        print '<blockquote>'
        for kid in kids:
            format(kid)
        print '</blockquote>'

print '<p>'
for row in toplevel:
    format(row)

print '''
    </p>
    </body>
</html>
'''