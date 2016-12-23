import sqlite3,sys

conn = sqlite3.connect('test.db')

curs = conn.cursor()

query = 'select * from form3 where %s' % sys.argv[0]
curs.execute(query)
print curs.description
conn.commit()
conn.close()