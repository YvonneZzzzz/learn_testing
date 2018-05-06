#coding=utf-8
from appium import webdriver
import time,datetime,os

#程序等待到制定时间，运行下列程序
# startTime = datetime.datetime(2017,7,20,9,12,0)
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

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

# time.sleep(3)

    #通过id查找元素
    # driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_highlight").click()

#通过文本查找元素
driver.find_element_by_name("工作").click()
time.sleep(2)
driver.find_element_by_name("考勤打卡").click()

#设定等待时间，来获取查找时间
time.sleep(3)

#成功获取“上班打卡”元素
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='1']/android.view.View[@index='4']").click()
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='0']/android.view.View[@index='1']").click()
# driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='0']/android.view.View[@index='1']").click()
# driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='0']/android.view.View[@index='2']").click()   #点击时间，V3.4.0成功
# driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='0']").click()   
#点击时间，V3.4.0成功
# driver.find_element_by_xpath("//android.view.View[@index='0']/android.view.View[@content-desc='上班打卡']").click()



# driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='0']/android.view.View[@index='1']").click()

# driver.find_element_by_xpath("//android.view.View[@content-desc='上班打卡']").click()

# try:
#     # inn = driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='1']/android.view.View[@index='4']")   #V3.5.0
#     # inn = driver.find_element_by_xpath("//android.widget.ListView[@index='3']/android.view.View[@index='0']/android.view.View[@index='1']") #V3.4.0
#     inn = driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='0']/android.view.View[@index='1']") #V3.4.0
    
#     if inn.is_displayed() == True:
#         inn.click()
# except:
#     driver.find_element_by_xpath("//android.view.View[@content-desc='上班打卡']").click()


    #点击“我知道了”
    # 更新打卡
    # driver.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']").click()
    # driver.find_element_by_id("android:id/button2").click()

#点击“我知道了”
# driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.Button[@index='4']").click()
    # driver.find_element_by_xpath("//android.widget.Button[@content-desc='我知道了'").click()
    # driver.find_element_by_content("我知道了").click()


#点击返回键
driver.keyevent(4)
#点击home键
driver.keyevent(3)

# time.sleep(3)

#点击电源键
# driver.keyevent(26)

# action =  TouchAction(driver)
# action.press(driver.keyevent(26)).waitAction(3000)
# action.perform()

# driver.long_press_keycode(26).wait_activity(3000).perform()
# driver.long_press_keycode(26).wait(3000).perform()
# driver.keyevent(26).wait()

# action2 = TouchAction(driver)
# el = driver.keyevent(26)
# action2.long_press(el).wait(3000).perform()

print("success punch in done")

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

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.find_element_by_name('ed').click()
# 微信版本V 6.5.16
driver.find_element_by_id('com.tencent.mm:id/a71').click()



command = ' adb shell input text "punch_in" '
os.system(command)
# driver.keyevent(43)
# driver.keyevent(39)

# driver.find_element_by_name('发送').click()
#点击返回键
driver.keyevent(4)
#点击home键
driver.keyevent(3)
# 点击电源键，锁屏
driver.keyevent(26)
driver.close_app()
driver.quit()
