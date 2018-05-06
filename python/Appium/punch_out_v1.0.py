# coding=utf-8
from appium import webdriver
import time
import datetime
import os

# # 程序等待到制定时间，运行下列程序
# startTime = datetime.datetime(2017,7,19,19,41,0)
# print('program not starting yet ...')
# while datetime.datetime.now() < startTime:
#     time.sleep(1)
# print("program now start on %s" %startTime)
# print('Executing...')

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.alibaba.android.rimet'
desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(12)
# time.sleep(5)

# 通过id查找元素
# driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_highlight").click()

# 通过文本查找元素
driver.find_element_by_name("工作").click()
time.sleep(2)
driver.find_element_by_name("考勤打卡").click()

# 设定等待时间，来获取查找时间
time.sleep(2)

#  成功获取“下班打卡”元素
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='2']/android.view.View[@index='4']").click()
# driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='1']/android.view.View[@index='2']").click()    # V3.5.0-钉钉UI变化后
# driver.find_element_by_xpath("//android.view.View[@content-desc='下班打卡']").click()
# time.sleep(2)

# 更新打卡
# driver.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']").click()
# driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='1']/android.view.View[@index='5']/android.view.View[@index='1']").click()

# driver.find_element_by_xpath("//android.view.View[@index='5']/android.view.View[@index='0']").click()     
driver.find_element_by_xpath("//android.view.View[@index='1']/android.view.View[@index='5']").click()     

#点击“更新打卡”
# time.sleep(1)
driver.find_element_by_id("android:id/button2").click()       
#点击“确定”

# WebDriverWait(driver, 12).until(lambda x: x.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']")).click()
# driver.find_element_by_id("android:id/button2").click()
# #

# try:
#     geng1 = driver.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']")
#     # geng2 = driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='2']/android.view.View[@index='9']")
#     # geng3 = driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='5']/android.view.View[@index='0']")
#     geng4 = driver.find_element_by_xpath("//android.view.View[@index='1']/android.view.View[@index='5']")   
#     # 钉钉版本v3.5.0
#     # out = driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='2']/android.view.View[@index='9']")
#     # out = driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='5']/android.view.View[@index='0']")
#     if geng1.is_displayed() == True:
#         geng1.click()
#         driver.find_element_by_id("android:id/button2").click()  
#         print("geng1")
#     # elif geng2.is_displayed() == True:
#     #     geng2.click()
#     #     driver.find_element_by_id("android:id/button2").click()  
#     #     print("geng2")
#     # elif geng3.is_displayed() == True:
#     #     geng3.click()
#     #     driver.find_element_by_id("android:id/button2").click()  
#     #     print("geng3")
#     elif geng4.is_displayed() == True:
#         geng4.click()
#         driver.find_element_by_id("android:id/button2").click()  
#         print("geng4")   
#     else :
#         pass              
# except:
#     # driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='2']/android.view.View[@index='4']").click()
#     # V3.5.0-钉钉UI变化后
#     xia1 = driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='1']/android.view.View[@index='1']")
#     xia2 = driver.find_element_by_xpath("//android.view.View[@index='1']")
#     xia3 = driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='1']/android.view.View[@content-desc='下班打卡']")
#     if xia1.is_displayed() == True:
#         xia1.click()
#         print("xia1")
#     elif xia2.is_displayed() == True:
#         xia2.click()
#         print("xia2")
#     elif xia3.is_displayed() == True:
#         xia3.click()      
#         print("xia3")
#     else:
#         print("can't find")
        
        
    # 点击“我知道了”
    # driver.find_element_by_xpath("//android.widget.Button[@content-desc='我知道了']").click()
    # driver.find_element_by_content("我知道了").click()
# 点击返回键
driver.keyevent(4)
# 点击home键
driver.keyevent(3)

print("success punch out done")

driver.close_app()
driver.quit()

#  ----------微信发送OK-------

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_name('ed').click()
# 微信版本V 6.5.16
driver.find_element_by_id('com.tencent.mm:id/a71').click()


command = ' adb shell input text "punch_out" '
os.system(command)
# driver.keyevent(43)
# driver.keyevent(39)

driver.find_element_by_name('发送').click()
# 点击返回键
driver.keyevent(4)
# 点击home键
driver.keyevent(3)
# 点击电源键，锁屏
driver.keyevent(26)
driver.close_app()
driver.quit()
