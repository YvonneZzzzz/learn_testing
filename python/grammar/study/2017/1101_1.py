# coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import datetime
import os

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

# try:
#     name1 = driver.find_element_by_name('aa')
#     name2 = driver.find_element_by_name('ed')
#     if name.is_displayed == True:
#         name1.click()
#         print("aa")
#     elif name2.is_displayed == True:
#         name2.click()
#         print("ed")
#     else:
#         pass
# except Exception as e:
#     name3 = driver.find_element_by_name("cc")
#     if name3.is_displayed == True:
#         print("aa")
#     else :
#         pass
##############################################
# name1 = driver.find_element_by_name('aa')
# name2 = driver.find_element_by_name('ed')
# try:
#     if driver.find_element_by_name('aa') == True:
#         driver.find_element_by_name('aa').click()
#         print("aa")
#     elif driver.find_element_by_name('ed') == True:
#         driver.find_element_by_name('ed').click()
#         print("ed")
#     # elif:
#     #     print("aaaa")     
#     else:
#         # pass
#         print("lala")
# except:
#     if driver.find_element_by_name('aa').is_displayed():
#         driver.find_element_by_name('aa').click()
#         print("aa")
#     elif driver.find_element_by_name('ed').is_displayed():
#         driver.find_element_by_name('ed').click()
#         print("ed")
#     # elif:
#     #     print("aaaa")     
#     else:
#         # pass
#         print("lala")
#     pass
try:
    driver.find_element_by_name("aa").click()
    print("aa")
# except NoSuchElementException:
# except NoSuchElementException:
except :
    driver.find_element_by_name('cc').click()
    print("cc")
# finally:
else:
    driver.find_element_by_name('dd').click()

    print("cc")
# except:
#     print("can't")

# 微信版本V 6.5.16
driver.find_element_by_id('com.tencent.mm:id/a71').click()


command = ' adb shell input text "punch_out" '
os.system(command)
# driver.keyevent(43)
# driver.keyevent(39)

# driver.find_element_by_name('发送').click()
# 点击返回键
driver.keyevent(4)
# 点击home键
driver.keyevent(3)
# 点击电源键，锁屏
driver.keyevent(26)
driver.close_app()
driver.quit()
