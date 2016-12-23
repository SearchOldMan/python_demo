import sqlite3
def get_value(value):
    if value.startswith('?'):
        return value.strip('?')
    if not value:
        value = '0'
    return str(value)

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute('''create table form3 (id int primary key,name text,age int,sex text)''')
query = 'insert into data values(?,?,?,?)'
for line in open('file.txt'):
    details = line.split(',')
    vals = [get_value(v) for v in details[:4]]
    print vals
    cur.execute(query,vals)
conn.commit()
conn.close()