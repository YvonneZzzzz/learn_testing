*** Keywords ***
打开浏览器
    [Arguments]    ${url}
    Open Browser    ${url}    Chrome

输入搜索内容
    [Arguments]    ${search_content}
    Input Text    id=kw    ${search_content}

点击搜索
    Click Button    id=su
    Sleep    2

校验标题
    [Arguments]    ${search_content}
    ${title}    Get Title
    Should Contain    ${title}    ${search_content}

关闭浏览器
    close all browsers
