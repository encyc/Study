# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:55:59 2022

@author: Administrator
"""

from wxauto import *


wx = WeChat()
print(wx.GetSessionList())

msgs = wx.GetAllMessage


msg = '这是来自程序api发送的信息~'
who = '偶滴织女'
wx.ChatWith(who)
wx.SendMsg(msg)

msg = '''你好
这是第二行
这是第三行
这是第四行'''
who = '文件传输助手'
WxUtils.SetClipboard(msg)
wx.ChatWith(who)
wx.SendClipboard()