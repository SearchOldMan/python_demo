'''
1.���庯���Ĳ�������
2.�����Ĵ��������������ж�1-100���ڵģ�ȡ��ż��
'''
#coding=utf-8
l = [1,3,4,5,6,7,8,9,9,230,32,41,456,778]
new_odd = []
for i in l:
        if i>1 and i<100 and i%2 == 0:
            new_odd.append(i)
        else:
            pass
    


print type(new_odd)
print new_odd