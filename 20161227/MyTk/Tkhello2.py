#coding=utf-8
#!/usr/bin/env python
#Tk_hello2.py
#coding=utf-8
import Tkinter
#创建顶层窗口
topTk = Tkinter.Tk()
label = Tkinter.Label(topTk,text='hello world')
label.pack()

quit = Tkinter.Button(topTk,text='quit',command=topTk.quit,bg='red',fg='white')
quit.pack(fill=Tkinter.X,expand=1)
Tkinter.mainloop()