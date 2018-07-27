# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

WIDTH = 375
HEIGHT = 812
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('http://m.baidu.com')
# driver.get('http://www.taobao.com')
# driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[1]/div/div[6]/div[1]/div').click()

sleep(3)
# driver.close()