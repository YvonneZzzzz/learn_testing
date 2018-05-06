#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
# from selenium.webdriver import common
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# import time as t

# binary = FirefoxBinary("E:\\firefox-50.0.1.win64.sdk\\firefox-sdk\\bin\\firefox.exe")    #加入Firefox的路径
# binary = FirefoxBinary("E:/firefox-50.0.1.win64.sdk/firefox-sdk/bin/firefox.exe")    #加入Firefox的路径
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
# t.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('selenium')

t.sleep(3)
driver.quit()

