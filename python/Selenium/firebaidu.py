#coding=utf-8
from selenium import webdriver
# from selenium.webdriver import common
# from time import sleep
import time
# import datetime

# 程序等待到制定时间，运行下列程序
# startTime = datetime.datetime(2017,7,14,10,10,0)
# print('program not starting yet ...')
# while datetime.datetime.now() < startTime:
#     time.sleep(1)
# print("program now start on %s" %startTime)
# print('Executing...')

driver = webdriver.Chrome()
# driver = webdriver.Safari()
# driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

# t.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
# driver.find_element_by_name('wd').send_keys('selenium')

print("success")
time.sleep(3)
driver.close()
# driver.quit()
