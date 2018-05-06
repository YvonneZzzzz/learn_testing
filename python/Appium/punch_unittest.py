#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time,datetime,os,unittest, re
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException

class punch(unittest.TestCase):

    # def test_first_punch_out(self):
    #     desired_caps = {}
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '5.1.1'
    #     desired_caps['deviceName'] = '25db1664'
    #     desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    #     desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
    #     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    #     # 通过文本查找元素
    #     # time.sleep(5)
    #     # driver.find_element_by_name("工作").click()
    #     WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name("工作")).click()
    #     driver.find_element_by_name("考勤打卡").click()
    #
    #     # 设定等待时间，来获取查找时间
    #     # time.sleep(12)
    #     # 成功获取“下班打卡”元素
    #     # driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='2']/android.view.View[@index='4']").click()
    #     WebDriverWait(driver, 12).until(lambda x: x.find_element_by_xpath(
    #         "//android.widget.ListView/android.view.View[@index='2']/android.view.View[@index='4']")).click()
    #     # 更新打卡
    #     # WebDriverWait(driver, 12).until(
    #     #     lambda x: x.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']")).click()
    #     # driver.find_element_by_id("android:id/button2").click()
    #
    #     driver.keyevent(4)
    #     driver.keyevent(3)
    #     driver.keyevent(26)
    #     print("-----------------success first punch out done-------------------------")
    #     driver.close_app()
    #     driver.quit()

    def test_punch_out(self):
        startTime = datetime.datetime(2017,7,26,19,33,0)
        print('program not starting yet ...')
        while datetime.datetime.now() < startTime:
            time.sleep(1)
        print("program now start on %s" %startTime)
        print('Executing...')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '25db1664'
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        WebDriverWait(driver, 10).until(lambda x:x.find_element_by_name("工作")).click()
        driver.find_element_by_name("考勤打卡").click()

        # 更新打卡
            # driver.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']").click()
            # driver.find_element_by_id("android:id/button2").click()
        WebDriverWait(driver, 12).until(lambda x: x.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']")).click()
        driver.find_element_by_id("android:id/button2").click()

        print("------------------success punch out done--------------------")
        driver.keyevent(3)
        driver.close_app()
        driver.quit()

        #----------微信发送OK-------

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '25db1664'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        time.sleep(5)
        driver.find_element_by_name('ed').click()
        driver.find_element_by_id('com.tencent.mm:id/a5e').click()

        # command = ' adb shell input text "ok" '
        # os.system(command)
        driver.keyevent(43)
        driver.keyevent(39)

        driver.find_element_by_name('发送').click()

        driver.keyevent(4)
        driver.keyevent(3)
        driver.keyevent(26)
        driver.close_app()
        driver.quit()

    def test_punch_in(self):
        # ------------punch in----------------
        # 程序等待到制定时间，运行下列程序
        startTime = datetime.datetime(2017, 7, 27, 9, 9, 0)
        print('program not starting yet ...')
        while datetime.datetime.now() < startTime:
            time.sleep(1)
        print("program now start on %s" % startTime)
        print('Executing...')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '25db1664'
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 通过文本查找元素
        # driver.find_element_by_name("工作").click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name("工作")).click()
        driver.find_element_by_name("考勤打卡").click()

        # 成功获取“上班打卡”元素,设定等待时间，来获取查找时间
            # time.sleep(12)
            # driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='1']/android.view.View[@index='4']").click()
        WebDriverWait(driver, 12).until(lambda x: x.find_element_by_xpath(
            "//android.widget.ListView/android.view.View[@index='1']/android.view.View[@index='4']")).click()

        driver.keyevent(4)
        driver.keyevent(3)
        print("success punch in done")

        driver.close_app()
        driver.quit()

        # ----------微信发送OK-------

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '25db1664'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        time.sleep(5)
        driver.find_element_by_name('ed').click()

        driver.find_element_by_id('com.tencent.mm:id/a5e').click()

        # 在文字框内输入"OK"
        # command = ' adb shell input text "ok" '
        # os.system(command)
        driver.keyevent(43)
        driver.keyevent(39)
        driver.find_element_by_name('发送').click()

        driver.keyevent(4)
        driver.keyevent(3)
        driver.keyevent(26)
        driver.close_app()
        driver.quit()



if __name__ == "__main__":
    unittest.main()
