#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
# from selenium import webdriver
import time,os
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# #4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


# if driver.find_element_by_name('aa').is_displayed() == True:
#     driver.find_element_by_name('aa').click()
# else :
#     driver.find_element_by_name('ed').click()

# try:
#     ed = driver.find_element_by_name('aa')
#     if ed.is_displayed():
#         ed.click()
# except:
#     driver.find_element_by_name('ed').click()

# 识别微信文字框
# driver.find_element_by_id('com.tencent.mm:id/bw3').click()
# driver.find_element_by_id('com.tencent.mm:id/bw3').send_keys('ok')

# driver.find_element_by_id('com.tencent.mm:id/a5e').send_keys('ok')
# driver.find_element_by_id('com.tencent.mm:id/a5e').click()
# driver.find_element_by_id('com.tencent.mm:id/a6g').click()
# driver.find_element_by_id('com.tencent.mm:id/a6h').click()
# 微信版本V 6.5.16
driver.find_element_by_name('ed').click()
driver.find_element_by_id('com.tencent.mm:id/a71').send_keys(u"哇哈哈")
# TouchAction(driver).press(x=0,y=300).release()ACTION.perform()
# action = TouchAction(driver)
# action.press(driver.find_element_by_name('ed')).release().perform()
# action.press(driver.find_element_by_id('com.tencent.mm:id/a71')).release().perform()
# action.press(x=42,y=243).release().perform()
# action.long_press(x=186,y=387).release().perform() #长按


# driver.find_element_by_id('com.tencent.mm:id/a5g').click()
# driver.find_element_by_xpath("//android.widget.GridView/android.widget.FrameLayout[@index='0']/com.tencent.mm.ui.MMImageView[@index='0']")


# command = ' adb shell input text "punch_out" '
# os.system(command)

#
# driver.find_element_by_name('发送').click()

print('success')
