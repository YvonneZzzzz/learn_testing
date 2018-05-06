#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://xueshu.baidu.com/")

#获得当前窗口
nowhandle = driver.current_window_handle

#打卡注册新窗口
driver.find_element_by_xpath("//*[@id='u']/a[3]").click()

#获得所有窗口
allhandles = driver.window_handles

#循环判断窗口是否为当前窗口
for handle in allhandles :
    if handle != nowhandle:
        driver.switch_to.window(handle)
        print("now register window!")
        #切换到百度首页标签
        driver.find_element_by_xpath("//*[@id='head']/div/a").click()
        time.sleep(5)
        #close()用于关闭当前窗口
        driver.close()

#回到原先的窗口
driver.switch_to.window(nowhandle)
    #多框架之间的切换
    #driver.switch_to_frame()

driver.find_element_by_id("kw").send_keys(u"返回成功")
time.sleep(3)
#quit()用于退出程序并关闭所有相关窗口
# driver.quit()
