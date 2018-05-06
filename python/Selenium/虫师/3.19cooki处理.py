#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

##3.19.1打印cookie信息
# #获得cookie信息
# cookie = driver.get_cookies()
# #将获得的cookie信息打印
# print(cookie)
# print("success")

#3.19.2对cookie操作

#向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbb'})
#遍历cookies中的name和value信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" %(cookie['name'],cookie['value']))

##下面可以通过两种方式删除cookie
#删除一个特定的cooki
driver.delete_cookie("CookieName")
#删除所有cookie
driver.delete_all_cookies()


# driver.quit()

