*** Settings ***
Resource          testflow03.robot
Resource          rescourse03.robot
Library           Selenium2Library

*** Test Cases ***
case01
    搜索测试    https://www.baidu.com/    好好学习
