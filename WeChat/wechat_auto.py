# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:55:59 2022

@author: Administrator
"""

from wxauto import *


wx = WeChat()
print(wx.GetSessionList())

msgs = wx.GetAllMessage


msg = '快去恰饭~'
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


import schedule
import time
def job():
    print("I'm working...")
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

import time
from schedule import every, repeat, run_pending
@repeat(every().second)
def job():
    print('working...')
while True:
    run_pending()
    time.sleep(1)

print('\n'.join([''.join([('lovelovelove'[(x-y)%12]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))