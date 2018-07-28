# from  selenium import webdriver
# import unittest
from time import sleep

from selenium.webdriver import TouchActions
#
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement

# from .abstract_event_listener import AbstractEventListener

# def swipeDown(site):
#     # driver = self.driver
#     sleep(2)
#     button = driver.find_element_by_xpath(site)
#     sleep(3)
#     """从button元素像下滑动200元素"""
#     Action = TouchActions(driver)
#     Action.scroll_from_element(button, 0, -200).perform()
#     sleep(3)

class diaoyong(object):
    """这是某些方法的调用"""

    def __init__(self, driver):
        self.driver = driver
        # self.driver = None

    def swipeDown(self,site):
        # sleep(2)
        # button = self.driver.find_element_by_xpath(site)
        # sleep(3)
        # """从button元素像下滑动200元素"""
        # Action = TouchActions(self.driver)
        # Action.scroll_from_element(button, 0, -200).perform()
        # sleep(3)
        sleep(2)
        self.driver.find_element_by_xpath(site).click()
        print("swipe")
        # return self

