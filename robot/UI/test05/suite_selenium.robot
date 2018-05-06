*** Settings ***
Library               F:/Python27/Lib/site-packages/Selenium2Library

*** Test Cases ***
case01
        [Documentation]        xpth=//*[@id=kw]
        ...        css=#id
        ...        用例中断言是必须的，tiitle
        Open Browser        https://www.baidu.com        chrome
        Input Text        id=kw        edrain
        Click Button        css=#su
        sleep        2
        #Get Title
        log        Get Title
        Close All Browsers

case02
        [Documentation]        xpth=//*[@id=kw]
        ...        css=#id
        ...        用例中断言是必须的，tiitle
        Open Browser        https://www.baidu.com        chrome
        Input Text        id=kw        edrain
        Click Button        css=#su
        sleep        2
        ${title}        Get Title
        log        ${title}
        Close All Browsers

case03
        [Documentation]        xpth=//*[@id=kw]
        ...        css=#id
        ...        用例中断言是必须的，tiitle
        Open Browser        https://www.baidu.com        chrome
        Input Text        id=kw        edrain
        Click Button        css=#su
        sleep        2
        ${title}        Get Title
        Should Contain        ${title}        this is title
        Close All Browsers
        Close Browser

case04
        [Documentation]        xpth=//*[@id=kw]
        ...        css=#id
        ...        用例中断言是必须的，tiitle
        searchkeyword        root        boot

*** Keywords ***
searchkeyword
        [Arguments]        ${search keyword}        ${assert}
        Open Browser        https://www.baidu.com        chrome
        Input Text        id=kw        ${search keyword}
        Click Button        css=#su
        sleep        2
        ${title}        Get Title
        Should Contain        ${title}        ${assert}
        Close All Browsers
        Close Browser
