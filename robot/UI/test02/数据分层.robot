*** Settings ***
Resource          testflow.robot
Resource          res.robot
Library           Selenium2Library

*** Test Cases ***
case01
    搜索测试    ${testURL}    ${searchText}
