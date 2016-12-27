#coding=utf-8
#!/usr/bin/env python

import os
from Tkinter import *
from time import sleep

class DirList:

    def __init__(self,initdir=None):
        self.top = Tk() #tk顶层窗口
        self.label = Label(self.top,text='Directory Lister'+'v1.1')
        self.label.pack()

        self.cwd = StringVar(self.top) #自动刷新的字符串变量
        #标题标签
        self.dirp = Label(self.top,font='Helvetica 12 bold',fg='blue')
        self.dirp.pack()

        #显示文件的列表
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT,fill=Y)
        self.dirs = Listbox(self.dirfm,height=15,width=50,yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>',self.setdirandgo)  #文件列表双击时的事件
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT,fill=BOTH)
        self.dirfm.pack()

        #单行的文本框
        self.dirn = Entry(self.top,width=50,textvariable=self.cwd)

        self.dirn.bind('<Return>',self.dols)
        self.dirn.pack()

        # 框架按钮
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm,text='Clear',command=self.clrdir,activeforeground='white',activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.dols, activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)

        if initdir:
            self.cwd.set(os.curdir)
            self.dols()

    def clrdir(self,ev=None):
        self.cwd.set('')

    def setdirandgo(self,ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.dols()

    def dols(self,ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:tdir = os.curdir

        if not os.path.exists(tdir):
            error  = tdir + ':not such file'
        elif not os.path.isdir(tdir):
            error = tdir + ':not a dir'

        if error:  #出错了就显示错误信息
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self,'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selecbackground='LightSkyBlue')
            self.top.update()
