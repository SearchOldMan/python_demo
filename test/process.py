from multiprocessing import Process,Queue
import os,time,random

def write(q):
	for value in ['a','b','c']:
		print 'put %s to queue' % value
		q.put(value)
		time.sleep(random.random())

def read(p):
	while True:
		value = p.get(True)
		print 'Get %s from queue' % value

if __name__ == '__main__':
	q = Queue()
	pw = Process(target = write,args=(q,))
	qr = Pcocess(target = read,args = (q,))

	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
