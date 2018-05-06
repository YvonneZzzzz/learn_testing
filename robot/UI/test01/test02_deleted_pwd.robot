*** Settings ***
Library           Selenium2Library

*** Test Cases ***
case
    Open Browser    chrome://settings/passwords    Chrome
    Sleep    4
    Click Element    xpth=.//*[@id="manageLink"]/span/a
