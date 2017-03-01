from Tkinter import *
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hellolabel = Label(self,text='hello world')
		self.hellolabel.pack()
		self.quitButton = Button(self,text='quit',command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title = 'hello'
app.mainloop()