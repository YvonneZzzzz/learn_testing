#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

# # 发送邮箱服务器
# smtpserver = 'smtp.163.com'
# # 发送邮箱用户名/密码
# user = 'xxx@163.com'
# password = 'xxxxx'
# # 发送邮箱
# sender = 'xxxx@163.com'
# # 接收邮箱
# recevier = 'xxxx@139.com'
# # 发送邮件主题
# subject = 'python email test'
#
# # 编写HTML类型的邮件正文
# msg =  MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')
#
# # 连接发送邮件
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()

##########################################
# coding=utf-8

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
for i in range(0,200):
    msg_from = 'xxxxx@163.com'  # 发送方邮箱
    passwd = 'xxxx'  # 填入发送方邮箱的授权码
    msg_to = 'xxxxxx@outlook.com'  # 收件人邮箱

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

    time.sleep(1)
    # if datetime.datetime.now() > endTime:
    # if x >= 2:
    #     break

print("over")

# import time
# def sleeptime(hour,min,sec):
#     return hour*3600 + min*60 + sec;
# second = sleeptime(0,0,20);
# while 1==1:
#     time.sleep(second);
#     print 'do action'
# #这是隔20秒执行一次
# while(True):
#    fun1
#    time.sleep(1)

#####################################################
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = input('xxx@163.com ')
# password = input('xxx@163.com')
# to_addr = input('xxx@qq.com')
# smtp_server = input('SMTP server: ')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
#####################################################
