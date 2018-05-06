#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s="中文"

# if isinstance(s, unicode):
#     #s=u"中文"
#     print (s.encode('gb2312'))
# else:
#     #s="中文"
#     print (s.decode('utf-8').encode('gb2312'))

'''
#----------微信发送OK-------
#coding=utf-8
from appium import webdriver
import time,datetime,os

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.find_element_by_name('ed').click()
# driver.find_element_by_id('com.tencent.mm:id/a6h').click()
driver.find_element_by_id('com.tencent.mm:id/a71').click()


command = ' adb shell input text "punch_in" '
os.system(command)
# driver.keyevent(43)
# driver.keyevent(39)

driver.find_element_by_name('发送').click()
#点击返回键
driver.keyevent(4)
#点击home键
driver.keyevent(3)
# 点击电源键，锁屏
driver.keyevent(26)
driver.close_app()
driver.quit()
'''

'''
# 发送邮件
import smtplib
import time, datetime
from email.mime.text import MIMEText

# x = 1
# while True:
    # x += 1
    #x=x+1
    # startTime = datetime.datetime(2017,10,26,10,18,0)
    # endTime = datetime.datetime(2017,10,26,11,17,0)
    # while datetime.datetime.now() > startTime:

i = 0
for i in range(0,500):
    msg_from = 'm18716228224@163.com'  # 发送方邮箱
    passwd = '168520'  # 填入发送方邮箱的授权码
    msg_to = 'test199422@outlook.com'  # 收件人邮箱

    subject = "哈哈哇"  # 主题
    content = "啦啦，test。范姐收"  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        # s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s = smtplib.SMTP_SSL("smtp.163.com", 465)
        # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        # print("发送成功 ",i)
        print("发送成功 {}" .format(i))
        
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()

    # time.sleep(1)
    # if datetime.datetime.now() > endTime:
    # if x >= 2:
    #     break

print("over")
'''

print ("hello test environment")
