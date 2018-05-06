# coding=utf-8

from appium import webdriver
# from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
import time
import os


# class punch(unittest.TestCase):
# class Punch:
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '25db1664'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


class Punch(unittest.TestCase):  

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)

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
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
                self.driver.find_element_by_xpath(c).click()                
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
                self.driver.find_element_by_name(c).click()                
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)

            flag = True
            print("can find", c)
            # self.driver.find_element_by_name(c).click()
        except NoSuchElementException as e:
            flag = False
            print("can't find",c)
        finally:
            return flag
      
    def test_wxdian(self):
        driver = self.driver
        punch = Punch()
        punch.isElement("name","cd")
        punch.isElement("name","ed")
        punch.isElement("name","aa")
        

        # driver.isElement("name","ed")
        # isElement("name","ed")
        driver.find_element_by_id('com.tencent.mm:id/a71').click()
        command = ' adb shell input text "test" '
        os.system(command)
        driver.find_element_by_name('发送').click()
        # driver.keyevent(4)      # 点击返回键
        # driver.keyevent(3)      # 点击home键
        driver.keyevent(26)     # 点击电源键，锁屏



# punch = Punch()
# # punch.setUp()
# punch.isElement("name","cc")
# punch.isElement("name","ed")
# punch.test_wxdian()



# punch = Punch()
# punch.isElement("name","cc")
# punch.isElement("name","ed")

 # driver.find_element_by_id('com.tencent.mm:id/a71').click()
# command = ' adb shell input text "test" '
# os.system(command)




    
    # driver.find_element_by_id('com.tencent.mm:id/a71').click()
# 
if __name__ == "__main__":
    unittest.main()
#     # isElement(self, identifyBy, c)
#     # main()



    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1.1'
    # desired_caps['deviceName'] = '25db1664'
    # desired_caps['appPackage'] = 'com.tencent.mm'
    # desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # driver.implicitly_wait(10)

    # def isElement(self, identifyBy, c):
    # # def main(self, identifyBy, c):  
    #     '''
    #     Determine whether elements exist
    #     Usage:
    #     isElement(By.XPATH,"//a")
    #     '''
    #     # driver = self.driver
    #     time.sleep(1)
    #     flag = None
    #     try:
    #         if identifyBy == "id":
    #             #self.driver.implicitly_wait(60)
    #             self.driver.find_element_by_id(c)
    #             self.driver.find_element_by_id(c).click()                
    #         elif identifyBy == "xpath":
    #             #self.driver.implicitly_wait(60)
    #             self.driver.find_element_by_xpath(c)
    #             self.driver.find_element_by_xpath(c).click()                
    #         elif identifyBy == "name":
    #             self.driver.find_element_by_name(c)
    #             self.driver.find_element_by_name(c).click()               
    #         flag = True
    #         print("can find")
    #         # self.driver.find_element_by_name(c).click()
    #     except NoSuchElementException as e:
    #         flag = False
    #         print("can't find")
    #     finally:
    #         return flag
      
    # def test_wxdian(self):
    #     driver = self.driver
    #     punch = Punch()
    #     punch.isElementxia("name","cd")
    #     punch.isElementxia("name","ed")
    #     # driver.isElement("name","ed")
    #     # isElement("name","ed")
    #     driver.find_element_by_id('com.tencent.mm:id/a71').click()
    #     command = ' adb shell input text "test" '
    #     os.system(command)
    #     # driver.find_element_by_name('发送').click()
    #     driver.keyevent(4)      # 点击返回键
    #     driver.keyevent(3)      # 点击home键
    #     driver.keyevent(26)     # 点击电源键，锁屏

