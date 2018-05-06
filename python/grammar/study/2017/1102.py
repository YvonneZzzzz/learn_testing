# coding=utf-8

from appium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
import time

# class punch(unittest.TestCase):
class Punch():   
# class Punch:   
    # def fun1():
    #     a = 1
    #     b = 0
    #     c = 4
    #     try:
    #         if c == a - b:
    #             print("a/b = ",c)
    #         # elif c == a + b + 1:
    #         #     print("+",c)
    #         # else:
    #         #     return False
    #     except:
    #         if c == a * b:
    #             print("*",c)
    #         elif c == a + b:
    #             print("+",c)
    #         else:
    #             print("wa")
    #         # pass
    # fun1()

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


    def isElement(self, identifyBy, c):
    # def main(self, identifyBy, c):   
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
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

            # if identifyBy == "aa":
            #     self.driver.find_element_by_name(c)
            # elif identifyBy == "bb":
            #     self.driver.find_element_by_name(c)
            # elif identifyBy == "ed":
            #     self.driver.find_element_by_name(c)
            flag = True
            print("can find")
            self.driver.find_element_by_name(c).click()
        except NoSuchElementException as e:
            flag = False
            print("can't find")
        finally:
            return flag
    
    # driver.find_element_by_id('com.tencent.mm:id/a71').click()

# if __name__ == '__main__':
#     # isElement(self, identifyBy, c)
#     # main()
#     unittest.main()

punch = Punch()
punch.isElement("name","cc")

punch.isElement("name","ed")
