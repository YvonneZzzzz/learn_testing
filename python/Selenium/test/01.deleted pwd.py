# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


# driverOptions = webdriver.ChromeOptions()
# # r代表后面的字符串斜杠不转义,''表示python识别空格
# # driverOptions.add_argument(r"user-data-dir=C:\Users\a\AppData\Local\Google\Chrome\User Data\Default\Login Data")
# driverOptions.add_argument(r"user-data-dir=C:\Users\a\AppData\Local\Google\Chrome\User''Data\Default\Login''Data")
# # driver = webdriver.Chrome(executable_path=r"F:\broswerdrvier\chromedriver.exe",0,driverOptions)
# driver = webdriver.Chrome(executable_path=r"F:\broswerdrvier\chromedriver.exe",port=0,chrome_options=driverOptions)
# # driver.get("http://www.baidu.com")



driver = webdriver.Chrome()
# 还是没有找到这个元素，这是为什么呢。。。同样的格式，其它网站都可以找到
driver.get('chrome://settings/passwords')
driver.implicitly_wait(10)
# driver.find_element_by_xpath("//[@id='manageLink']/span/a").click()
driver.find_element_by_css_selector("#shadow-root > #manageLink > span > a").click()
# driver.find_element_by_partial_link_text('passwords')
# driver.find_element_by_link_text('passwords.google.com')


# driver.get('https://www.google.com/search?q=selenium+%E9%93%BE%E6%8E%A5+%E5%AE%9A%E4%BD%8D&oq=selenium+%E9%93%BE%E6%8E%A5+%E5%AE%9A%E4%BD%8D&aqs=chrome..69i57j69i60j69i61l2.407j0j4&sourceid=chrome&ie=UTF-8')
# driver.implicitly_wait(10)
# # driver.find_element_by_link_text("4. 查找元素— Selenium-Python中文文档2 documentation").click()
# # driver.find_element_by_xpath("//*[@id='rso']/div/div/div[3]/div/div/h3/a").click()
# driver.find_element_by_css_selector("#rso > div > div > div:nth-child(2) > div > div > h3 > a").click()

print("success")

 


