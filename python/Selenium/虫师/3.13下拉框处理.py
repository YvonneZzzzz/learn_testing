#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('3.13drop_down.html')
driver.get(file_path)
time.sleep(2)

#先定位到下拉框
m = driver.find_element_by_id('ShippingMethod')
# m = driver.find_element_by_id('ShippingMethod').click()
time.sleep(2)

#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
# m.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
# 不对m.find_element_by_css_selector("#ShippingMethod > option:nth-child(6)").click()
time.sleep(2)

# driver.quit()