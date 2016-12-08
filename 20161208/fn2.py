#coding=utf-8
def cmpStr(*sen):
    for i in sen:
        if isinstance(i, str):
            pass
        else:
            return u'输入的必须是字符串'
    a = sorted(sen,key = lambda k : len(k))
    
    return a

print cmpStr(12,{'bane':12},'github')