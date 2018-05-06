*** Settings ***
Library               F:/Python27/Lib/site-packages/Selenium2Library

*** Test Cases ***
01.Scalar变量
        ${text}        Set Variable        2018-03-21
        ${title}        Get Title

02.Scalar使用
        ${text}        Set Variable        8866
        Run Keyword If        ${text}==8866        log        success

03.Scalar字符串
        ${text}        Set Variable        8866
        log        aaa${text}bbb

04.Scalar参与运算
        ${text}        Set Variable        8866.1
        ${t}        Evaluate        int(${text})+1
        ${t1}        Evaluate        ${text}+3
        ${random}        Evaluate        random.randint(0,sys.maxint)        random,sys

05.List变量赋值
        @{a}        Set Variable        3        2        1
        @{b}        Create List        1        2        3
        Log Many        @{a}
        #log        @{a}        加入这行会报错
        Log Many        @{b}

05.List使用
        @{qt}        Create List        bbbb        INFO
        Run Keyword And Ignore Error        log        @{qt}
        Run Keyword And Ignore Error        log        bbbb        INFO
        #不推荐使用下面的方法
        @{list}        Create List        aaaa
        log        @{list}

06.List转换成Scalar
        @{f}        Create List        a        b        c
        #fail        @{f}        这行运行会报错
        fail        ${f}

07.Scalar转换成List
        ${f}        Create List        a        b        c
        fail        ${f}

08.转换限制
        @{f}        Create List        a        b        c
        fail        ${f}

09.转换限制
        ${f}        Create List        a        b        c
        fail        @{f}

10.转换限制
        ${f}        Create List        a        b        c
        log        ${f[1]}

11.转换限制
        [Documentation]        {f}是@{f}的Scalar形式，这个也是有限制，必须是{f}没有被赋值过的情况，如果${f}被赋值过是什么情况呢？
        ${f}        Set Variable        4
        @{f}        Create list        a        b        c
        log        ${f}

12.List元素获取
        [Documentation]        一维List的例子
        @{f}        Create list        a        b        c
        log        ${f[1]}

13.List元素获取
        [Documentation]        二维List的例子
        @{a}        Create list        1        2
        @{b}        Create List        3        4
        @{c}        Create List        ${a}        ${b}        d
        #log        ${f[1][1]}
        log        ${f[1]}
