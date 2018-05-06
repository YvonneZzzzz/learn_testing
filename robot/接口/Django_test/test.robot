
*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
#GET请求的查询发布会接口测试用例
test_get_event_list
    ${payload}=    Create Dictionary    eid=1
    Create Session    event    http://127.0.0.1:8000/api
    ${r}=    Get Request    event    /get_event_list/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    Log    ${r.json()}
    ${dict}    Set Variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}

#POST请求的嘉宾签到接口测试用例
test_user_sign_success
    Create Session    sign    http://127.0.0.1:8000/api
    &{headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    &{payload}    Create Dictionary    eid=1    phone=11111
    ${r}    Post Request    sign    /user_sign/    data=${payload}    headers=${headers}
    Should Be Equal As Strings    ${r.status_code}    200
    Log    ${r.json()}
    ${dict}    Set Variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    sign success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}