*** Keywords ***
搜索测试
    [Arguments]    ${url}    ${search_content}
    打开浏览器    ${url}
    输入搜索内容    ${search_content}
    点击搜索
    校验标题    ${search_content}
    关闭浏览器
