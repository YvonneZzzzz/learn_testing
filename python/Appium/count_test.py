#coding=utf-8
from appium import webdriver

import time,datetime

#程序等待到制定时间，运行下列程序
startTime = datetime.datetime(2017,7,14,15,18,0)
print('program not starting yet ...')
while datetime.datetime.now() < startTime:
    time.sleep(1)
print("program now start on %s" %startTime)
print('Executing...')

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '76P4C16514020753'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

# driver.find_element_by_name("delete").click()
driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='减']").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

# driver.find_element_by_name("=").click()
driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='等于']").click()

# 退出该程序
driver.quit()
