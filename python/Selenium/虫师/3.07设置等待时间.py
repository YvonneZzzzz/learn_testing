# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
#导入webDriverWait包
from selenium.webdriver.support.ui import WebDriverWait
#导入time包
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#webDriverWait()方法使用
element = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_id("kw"))
element.send_keys("selenium")
print("success webDriverWait")
    # WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    # driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
    # timeout - 最长超时时间，默认以秒为单位
    # poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
    # ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
    # until(method, message=’’)调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
    # until_not(method, message=’’)调用该方法提供的驱动程序作为一个参数，直到返回值为 False。

# 添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()
print("success implicitly_wait")

#添加固定休息时间,以秒为单位
#import time
time.sleep(5)
# time.sleep(0.5)
print("success time_sleep")
    #或者直接导入sleep()方法
    #from time import sleep
    #sleep(3)

# driver.quit()


