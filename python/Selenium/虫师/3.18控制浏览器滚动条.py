#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将滚动条移动到页面的底部
# Firefox
# js = "var q=document.documentElement.scrollTop=100000"
#通过Chrome使用
js = "var q=document.body.scrollTop=10000"
driver.execute_script(js)
print("success button")
time.sleep(3)

#将滚动条移动到页面的顶部
# js_ = "var q = document.documentElement.scrollTop=0"
js_ = "var q=document.body.scrollTop=0"
driver.execute_script(js_)
print("success top")
time.sleep(3)

# driver.quit()

#用于标识滚动条位置的代码
# <body onload = "document.body.scrollTop=0"> 顶部
# <body onload = "document.body.scrollTop=100000"> 底部

#为何滚动不在界面上显示出来。
# 浏览器不同，调用js的滚动条不一样
