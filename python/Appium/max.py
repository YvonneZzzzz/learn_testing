#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# #3.1.1
# driver.get("http://www.baidu.com")
# print("浏览器最大化")
# driver.maximize_window()

# #3.1.2
# driver.get("http://www.baidu.com")
# print("设置浏览器宽480，高800显示")
# driver.set_window_size(480, 800)

#3.1.3
#访问百度首页
first_url = "http://www.baidu.com"
#python3.x
print ("now access %s" %first_url)
#python2.x
# print("now access %s") %(first_url)
driver.get(first_url)
#访问新闻页面
second_url = "http://news.baidu.com"
print ("now access %s" %second_url)
driver.get(second_url)
#返回（后退）到百度首页
print ("back to %s" %first_url)
driver.back()
#设定延时时间
time.sleep(3)
#前进到新闻页
print ("forward to %s" %second_url)
driver.forward()


# driver.quit()
