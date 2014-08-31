# -*- coding: utf-8 -*-
# 窗体
import xbmcplugin
import xbmcgui
__author__ = 'hexpang'

class XWindow(xbmcgui.WindowDialog):
    def __init__(self):
        self.addControl(xbmcgui.ControlImage(x=0, y=0, width=150, height=150, filename="http://staticlive.douyutv.com/upload/game_cate/bf21a79139fc499aff52adecd702207b.jpg"))
