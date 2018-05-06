#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()