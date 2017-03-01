import shelve
d = shelve.open('index.txt')
d['key'] = 'some_value'
d.close()
d2 = shelve.open('index.txt')
print d2
d2.close()