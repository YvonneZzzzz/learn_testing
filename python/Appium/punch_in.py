# coding=utf-8

from appium import webdriver
# from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
import time
import os

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.alibaba.android.rimet'
desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

class Punch(unittest.TestCase):  
    # 4734接受webdriver端口，4724用于和andorid通信,4723
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(12)
    
    def isElement(self, identifyBy, c):
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
                self.driver.find_element_by_xpath(c)
                self.driver.find_element_by_xpath(c).click()    
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
                self.driver.find_element_by_name(c).click()                

            flag = True
            print("can find: ",c )
            # self.driver.find_element_by_name(c).click()
        except NoSuchElementException as e:
            flag = False
            print("can't find: %s" %c)
        finally:
            return flag

      
    def test_ding(self):
        driver = self.driver
        time.sleep(1)
        punch = Punch()       
        # driver.find_element_by_name("工作").click()        
        driver.find_element_by_name("Portal").click()                
        driver.find_element_by_name("考勤打卡").click()

        #点击打in
        # punch.isElement("xpath","//android.widget.ListView[@index='3']/android.view.View[@index='0']")
        # punch.isElement("xpath","//android.widget.ListView[@index='3']/android.view.View[@index='0']/android.view.View[@index='2']")
        # punch.isElement("xpath","//android.view.View[@index='0']/android.view.View[@content-desc='上班打卡']")

        punch.isElement("xpath","//android.widget.ListView[@index='2']/android.view.View[@index='0']/android.view.View[@index='1']")
        punch.isElement("xpath","//android.widget.ListView[@index='2']/android.view.View[@index='0']/android.view.View[@index='2']")
        punch.isElement("xpath","//android.widget.ListView[@index='2']/android.view.View[@index='0']/android.view.View[@content-desc='上班打卡']")
        punch.isElement("xpath","//android.view.View[@index='0']/android.view.View[@content-desc='上班打卡']")        
        punch.isElement("xpath","//android.view.View[@index='0']/android.view.View[@index='1']")

        driver.keyevent(4)      # 点击返回键
        driver.keyevent(4) 
        # driver.keyevent(3)      # 点击home键

        #Ding输入文字
        # driver.find_element_by_name("消息").click()
        driver.find_element_by_name("Messages").click()        
        driver.find_element_by_name("Allen").click()
        # driver.find_element_by_name("输入文字...").click()
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_sendmessage").click()

        command = ' adb shell input text "buenos_dias" '
        os.system(command)
        # driver.find_element_by_name("发送").click()
        driver.find_element_by_name("Send").click()        

        driver.keyevent(26)     # 点击电源键，锁屏


if __name__ == "__main__":
    unittest.main()
    # Punch()
