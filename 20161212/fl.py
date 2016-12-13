#coding = utf-8


def add(max):
    a,b,n = 0,1,0
    if n < max:
        yield b
        a,b = b,a+b
        

f = add(10)

print f.next()
print f.next()
    
    
    