# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import core


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"计算器", pos=wx.DefaultPosition, size=wx.Size(775, 613),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_statusBar2 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.inputbox = wx.TextCtrl(self, wx.ID_ANY, u"请输入计算式", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        bSizer1.Add(self.inputbox, 0, wx.ALL | wx.EXPAND, 5)

        self.calculate = wx.Button(self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.calculate, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.outputbox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_CENTER | wx.TE_READONLY)
        bSizer1.Add(self.outputbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.bugbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer1.Add( self.bugbox, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.inputbox.Bind(wx.EVT_TEXT_ENTER, self.cal)
        self.calculate.Bind(wx.EVT_BUTTON, self.cal)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cal(self, event):
        value = self.inputbox.GetValue()
        output = core.core(value)
        bug = core.inf(value)
        self.outputbox.SetValue(output)
        self.bugbox.AppendText('\n')
        self.bugbox.AppendText(bug)
        self.inputbox.Clear()
        event.Skip()
