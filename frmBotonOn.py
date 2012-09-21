#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Wed Sep 12 15:16:03 2012

import wx

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.button_1 = wx.ToggleButton(self, -1, "ON")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOGGLEBUTTON, self.evento, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Encendido")
        self.button_1.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.button_1.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.button_1, 0, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def evento(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.button_1.Value == 0:
            self.button_1.SetBackgroundColour(wx.Colour(0, 255, 255))
            self.button_1.SetValue(1)
        elif self.button_1.Value == 1:
            self.button_1.SetBackgroundColour(wx.Colour(0, 255, 0))
            self.button_1.SetValue(0)

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()