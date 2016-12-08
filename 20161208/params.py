def add(a,b=2,c=4):
    print 'a=%s'%a
    print 'b=%s'%b
    print 'c=%s'%c
    sum = 0;
    sum = a+b+c
    return sum

add(1,c=3,b=4)

print add(1,c=3,b=5) 
