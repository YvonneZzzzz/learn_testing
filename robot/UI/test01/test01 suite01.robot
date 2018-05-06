*** Settings ***
Library           F:/Python27/Lib/site-packages/Selenium2Library
Library           Selenium2Library

*** Test Cases ***
case01
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    robot framwrok
    Sleep    2
    Click Button    id=su
    Close Browser

case02
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    robot
    Click Button    id=su
    Sleep    2
    ${title}    Get Title
    Should Contain    ${title}    bot
    Close Browser
