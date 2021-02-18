from tkinter import *

import core


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self, width=90,  xscrollcommand=1, textvariable='请输入式子')
        self.nameInput.pack(fill=BOTH)
        self.alertButton = Button(self, text='Run', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or '0'
        msg = core.core(name)
        self.printanswer = Label(self, text=msg)
        self.printanswer.pack()


app = Application()
app.master.title('laji calculator by zsdcxd')
app.mainloop()

