#coding=utf-8
from selenium import webdriver
# from selenium.webdriver import common
from time import sleep

driver = webdriver.Chrome()
# driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

# t.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('selenium')

sleep(3)
driver.quit()