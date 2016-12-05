# # 导入mysql的驱动
# import mysql.connector
# # 创建连接
# conn = mysql.connector.connect(user='root', password='root', database='test', use_unicode=True)
# cursor = conn.cursor()
# # 创建表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行数据
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# 1
# # 提交业务
# conn.commit()
# cursor.close()
# # 查询
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()


import mysql.connector
conn = mysql.connector.connect(user='root',password='root',use_unicode=True)
cursor = conn.cursor()
cursor.execute('create tables user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into (id,name) values (%s,%s)',('1','laowang'))
cursor.rowcount
cursor.commit()
cursor.close()

conn = mysql.connector.connect(uesr='root',password='root',use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from user where id=%s',('1',))
value = cursor.fetchall()
