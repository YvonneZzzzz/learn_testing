#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from appium import webdriver
# import time,datetime
import subprocess
import os
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.1'
# desired_caps['deviceName'] = '25db1664'
# # desired_caps['appPackage'] = 'com.alibaba.android.rimet'
# # desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'

# #4734接受webdriver端口，4724用于和andorid通信,4723
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.keyevent(26)

returncode = subprocess.call('adb shell reboot -p')
print(returncode)

# command = 'adb shell reboot -p'
# os.system(command)