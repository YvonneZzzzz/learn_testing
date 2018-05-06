#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
#浏览器最大化
driver.maximize_window()
#登陆快播私有云
driver.find_element_by_id("user_name").send_keys("testing360")
driver.find_element_by_id("user_pwd").send_keys("198876")
driver.find_element_by_id('"dl_an_submit').click()
time.sleep(3)
#获取用户名
now_user = driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text
#用户名是否等于虫师，不等于将异常抛出
if now_user == u'虫师':
    print("登陆成功")
else:
    raise NameError('user name error')
#退出
driver.find_element_by_class_name("Usertool").click()
time.sleep(2)
driver.find_element_by_link_text("退出").click()
time.sleep(2)

