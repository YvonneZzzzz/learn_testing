#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

"""设置手机的大小"""

driver = webdriver.Chrome()
driver.get('http://m.test.90dichan.com')
driver.maximize_window()

"""定位操作元素"""
time.sleep(2)
button = driver.find_element_by_xpath('//*[@id="pullrefresh"]/div[2]/ul/li[2]/a/div[2]/span')
time.sleep(3)

"""从button元素像下滑动200元素"""
Action = TouchActions(driver)
Action.scroll_from_element(button, 0, -200).perform()
time.sleep(3)
driver.close()