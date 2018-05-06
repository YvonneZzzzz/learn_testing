#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coding = utf-8

# from selenium import webdriver
# import time
# import datetime

# startTime = datetime.datetime(2017,10,26,10,18,0)
# endTime = datetime.datetime(2017,10,26,11,41,0)
# while datetime.datetime.now() > startTime:


# x = 1
# while True:
#     x += 1
#     time.sleep(4)
#     print("ok")

#     # if datetime.datetime.now() >= endTime:
#     if x >= 5:
#         break

# print('finish')

# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# print(driver.title)
# driver.quit()

# for i in range(1, 10):
#     print(i)

# import smtplib
# import time, datetime
# from email.mime.text import MIMEText
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

#     msg_from = 'xxxx@163.com'  # 发送方邮箱
#     passwd = 'xxxx'  # 填入发送方邮箱的授权码
#     msg_to = 'xxxxx@139.com'  # 收件人邮箱

#     subject = "哈哈哇"  # 主题
#     content = "啦啦，test收。哈哈哈哈"  # 正文
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     msg['From'] = msg_from
#     msg['To'] = msg_to
#     try:
#         # s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#         s = smtplib.SMTP_SSL("smtp.163.com", 465)
#         # 邮件服务器及端口号
#         s.login(msg_from, passwd)
#         s.sendmail(msg_from, msg_to, msg.as_string())
#         print("发送成功")
#     except smtplib.SMTPException as e:
#         print("发送失败")
#     finally:
#         s.quit()

#     time.sleep(4)
#     # if datetime.datetime.now() > endTime:
#     if x >= 80:
#         break

# print("over")

# print(1)
# print(2)
# pass
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
