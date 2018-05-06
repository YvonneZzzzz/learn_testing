# coding=utf-8

from appium import webdriver
# from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
import time
import os

class Punch(unittest.TestCase):  

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
    
    def isElementxia(self, identifyBy, c):
        # def main(self, identifyBy, c):  
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        # driver = self.driver
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
                self.driver.find_element_by_id(c).click()                
            elif identifyBy == "xpath":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
                self.driver.find_element_by_xpath(c).click()              
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
                self.driver.find_element_by_name(c).click()                

            flag = True
            print("can find")
            # self.driver.find_element_by_name(c).click()
        except NoSuchElementException as e:
            flag = False
            print("can't find")
        finally:
            return flag

    def isElementgeng(self, identifyBy, c):
    # def main(self, identifyBy, c):  
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        # driver = self.driver
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
                self.driver.find_element_by_id(c).click()                
            elif identifyBy == "xpath":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
                self.driver.find_element_by_xpath(c).click()   
                self.driver.find_element_by_id("android:id/button2").click()              
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
                self.driver.find_element_by_name(c).click()                

            flag = True
            print("can find", c)
            # self.driver.find_element_by_name(c).click()
        except NoSuchElementException as e:
            flag = False
            print("can't find", c)
        finally:
            return flag
      
    def test_outgeng(self):
        driver = self.driver
        driver.find_element_by_name("工作").click()
        time.sleep(2)
        driver.find_element_by_name("考勤打卡").click()
        time.sleep(2)

        punch = Punch()
        punch.isElementxia("xpth","//android.view.View[@index='0']/android.widget.ListView[@index='3']/android.view.View[@index='1']/android.view.View[@index='2']")
        punch.isElementgeng("xpath","//android.view.View[@index='5']/android.view.View[@index='0']")

        driver.keyevent(4)      # 点击返回键
        driver.keyevent(3)      # 点击home键
        # driver.keyevent(26)     # 点击电源键，锁屏


if __name__ == "__main__":
    unittest.main()

# punch = Punch()
# # punch.setUp()
# punch.isElement("name","cc")
# punch.isElement("name","ed")
# punch.test_wxdian()


