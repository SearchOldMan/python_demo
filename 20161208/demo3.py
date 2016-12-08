#coding=utf-8
'''

'''
def detail(name=None,**kar):
    data = []
    for x,y in kar.items():
        # [',','year',':',12]
        data.extend([',',str(x),':',str(y)])              
    info = ''.join(data)
    return '%s%s'%(name,info)

print detail('lilei',years=4)

print detail('lilei')

