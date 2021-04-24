from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import ctypes
import core

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)


class main(object):
    def __init__(self, father_window=None):
        self.main = father_window
        self.window()

    def window(self):
        self.main.title('挺垃圾的python计算器')
        screenwidth = self.main.winfo_screenwidth()
        screenheight = self.main.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (400, 550, (screenwidth - 400) / 2, (screenheight - 550) / 2)
        self.main.geometry(alignstr)
        self.main.resizable(width=False, height=False)
        self.main.iconbitmap("icon.ico")
        self.main['bg'] = 'pink'
        self.main.attributes('-alpha', 0.85)
        self.Formula_label = Label(self.main, text='请输入式子')
        self.Formula_label.pack(side='top', anchor='nw')

        self.Formula_text = Entry(self.main)
        self.Formula_text.pack(side='top', fill='x')

        self.calculate_Button = Button(text='计算', command=self.cal)
        self.calculate_Button.pack()

        self.Result_label = Label(self.main, text='输出结果')
        self.Result_label.pack(anchor='n', side='right')

    def cal(self):
        formula_text = self.Formula_text.get() or '0'
        answer = core.core(formula_text)
        self.printans = Label(self, Text=answer)
        self.printans.pack()


father = Tk()
s = main(father)
father.mainloop()
