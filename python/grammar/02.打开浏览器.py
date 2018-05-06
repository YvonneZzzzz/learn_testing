#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入selenium的webdiver包
from selenium import webdriver

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Ie()

#获得浏览器对象后，通过get（）方法向浏览器发送网址
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("哇哈哈")
driver.find_element_by_id("su").click()

# 退出并关闭窗口
# driver.quit()
