#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import os
from time import sleep

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('3.08checkbox.html')
driver.get(file_path)

# #选择页面上所有的tag_name为input的元素
# inputs = driver.find_elements_by_tag_name('input')
# # inputs = driver.find_element_by_tag_name('input') 这个不行
# #然后从中过滤出type为checkbox的元素，单击勾选
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
#         print("success %s" %input)

#选择所有的type为checkbox的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector("input[type=checkbox]")
for checkboxe in checkboxes:
    checkboxe.click()
sleep(2)
#打印当前页面上type为checkbox的个数
#len()用于返回一个对象的长度（或个数）
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))
#把页面上最后1个checkbox的勾去掉
#pop()用于删除指定位置的元素，为空默认选择最后一个元素
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
sleep(2)


# driver.quit()
