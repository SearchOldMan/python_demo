#coding=utf-8
f = open('E:\\learngit\\python_demo\\20161221\\file.txt')
boy = []
girl = []
for each_line in f:
    (person,content) = each_line.split(':',1)
    if person == '问':
        boy.append(content)
    else:
        girl.append(content)

boy_file = open('E:\\learngit\\python_demo\\file_name_boy','w')
boy_file.writelines(boy)
f.close()
boy_file.close()