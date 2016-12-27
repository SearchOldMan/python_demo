#coding=utf-8
#!/usr/bin/env python
#Tk_hello3.py
#coding=utf-8
import Tkinter

def resize(ev=None):
    #空值label的文字大小
    label.config(font='Arial -%d bold' % scale.get())
#创建顶层窗口
topTk = Tkinter.Tk()
topTk.geometry('250x150')

label = Tkinter.Label(topTk,text='hello world',font='Arial -12 bold')
label.pack(fill=Tkinter.Y,expand=1)

scale = Tkinter.Scale(topTk,from_=10,to=40,command=resize)
scale.set(12)
scale.pack(fill=Tkinter.X,expand=1)

quit = Tkinter.Button(topTk,text="quit",command=topTk.quit,activeforeground='white',activebackground='red')
quit.pack()
Tkinter.mainloop()