import threading
def show(i):
	print i

ts = []

for i in xrange(0,10):

	th = threading.Thread(target=show,args=[i])
	th.start()
	ts.append(th)

for i in ts:
	i.join()

print 'end'