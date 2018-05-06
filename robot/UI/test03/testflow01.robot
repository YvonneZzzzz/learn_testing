*** Keywords ***
搜索测试

关键字测试
        [Arguments]        ${arg1}        @{arg2}
        ${temp}        Set Variable        ${arg1}
        ${arg1}        Set Variable        ${arg2[2]}
        log        ${arg1}===${arg2}
        [Teardown]        Set Suite Variable        ${arg1}        ${temp}
        [Return]        @{arg2}        ${arg1}        @{arg2}

关键字测试06
        [Arguments]        ${arg1}        @{arg2}
        ${temp}        Set Variable        ${arg1}
        ${arg1}        Set Variable        ${arg2[2]}
        log        ${arg1}===${arg2}
        [Teardown]        Set Suite Variable        ${arg1}        ${temp}
        [Return]        ${arg1}        ${arg2[2]}        ${arg2[1]}
