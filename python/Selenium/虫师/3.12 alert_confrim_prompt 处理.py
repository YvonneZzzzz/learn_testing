#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#点击打开搜索设置
driver.find_element_by_xpath("//*[@id='u1']/a[8]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
time.sleep(2)

#点击保存设置
driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()

time.sleep(2)
# #获取网页上的警告信息
# # alert = driver.switch_to.alert.accept()
# alert = driver.switch_to_alert()
# #接受警告信息
# alert.accept()

# #接受警告信息
# alert = driver.switch_to_alert()
# alert.accept()

# #得到文本信息并打印
# alert = driver.switch_to_alert()
# print (alert.text)

# # 取消对话框（如果有的话）
# alert = driver.switch_to_alert()
# alert.dismiss()
#
# #输入值（如果有的话）
# alert = driver.switch_to_alert()
# alert.send_keys("xxx")

