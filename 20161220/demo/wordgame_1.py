#coding=utf-8
temp = input('猜测一下现在在想什么数字')
guess = int(temp)
while guess != 8:
    temp = input('猜错了，请重新输入')
    guess = int(temp)
    if guess == 8:
        print "现在的数字是8"
        print "猜对了也没有用"
    else:
        if guess > 8:
            print "太大了！"
            print "重新输入试试吧"
        else:
            print "太小了"
print "不玩了！"