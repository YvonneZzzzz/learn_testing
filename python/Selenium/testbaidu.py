#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time as t

# binary = FirefoxBinary("E:\\firefox-50.0.1.win64.sdk\\firefox-sdk\\bin\\firefox.exe")    #加入Firefox的路径
binary = FirefoxBinary("E:/firefox-50.0.1.win64.sdk/firefox-sdk/bin/firefox.exe")    #加入Firefox的路径
driver = webdriver.Firefox()

driver.get('http://www.baidu.com')
# t.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('selenium')

t.sleep(3)
driver.quit()

'''

from selenium import webdriver

# 打开百度
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 输入Selenium并点击'百度一下'按钮
driver.find_element_by_id("kw").send_keys("this is test")
driver.find_element_by_id("su").click()


# driver.close()
