from selenium import webdriver
import time
import unittest

class Baidu(unittest.TestCase):
    def setUp(self):
        # driver = self.driver
        # # self.driver = driver
        # # driver = webdriver.Firefox()
        # # driver = webdriver.Ie()
        # driver = webdriver.Chrome()
        # driver.get("http://www.baidu.com")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test01(self):
        driver = self.driver
        # driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("www")
       
    
    def test02(self):
        driver = self.driver
        # driver.get(self.base_url + "/")
        # driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("aaaa")
        # print("aaaaa")

    
if __name__ == "__main__":
    
    unittest.main()