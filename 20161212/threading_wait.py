import threading

def show(p):
    print p,

ths = []
for i in xrange(0,15):
    th = threading.Thread(target=show,args=[i])
    ths.append(th)
    
for each in ths:
    each.start()
    


print 'thread is end'