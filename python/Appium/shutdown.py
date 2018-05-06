#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time,datetime
import os
import subprocess
from selenium.webdriver.support.wait import WebDriverWait

# ------------punch out---------------
# 程序等待到制定时间，运行下列程序



#----------微信发送OK-------

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.find_element_by_name('ed').click()
driver.find_element_by_id('com.tencent.mm:id/a5e').click()

# command = ' adb shell input text "ok" '
# os.system(command)
driver.keyevent(43)
driver.keyevent(39)

driver.find_element_by_name('发送').click()
#点击返回键
driver.keyevent(4)
#点击home键
driver.keyevent(3)

# ------------周五手机关机----------------

returncode = subprocess.call('adb shell reboot -p')
print(returncode)

driver.close_app()
driver.quit()





