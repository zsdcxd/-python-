import wx
# import the newly created GUI file
import noname


class CalcFrame(noname.MyFrame2):
    def __init__(self, parent):
        noname.MyFrame2.__init__(self, parent)


app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
