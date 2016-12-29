import shelve

d = shelve.open('example.s')

d['key'] = 'some_value'

d.close()

d2 = shelve.open('example.s')

d3 = shelve.open('mutable_loss.s')
d3['key'] = []
d3['key'].append(2)
d3.close()

dm = shelve.open('mutable_loss.s')

print dm