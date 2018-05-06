*** Settings ***
Library               Screenshot

*** Test Cases ***
case01
        ${a}        Set Variable        hello edrain
        ${abc}        Create List        a        666        c
        log        ${a}
        log        ${abc}

case02
        [Documentation]        Evaluate调用python
        ${a}        Evaluate        int(888)
        #${t}        Evaluate        type(${a})
        #log        ${t}
        log        ${a}

case03
        [Documentation]        Evaluate调用python
        ${a}        Evaluate        random.randint(1,888)        random
        log        ${a}

case04
        [Documentation]        robot else if 循环
        ${a}        Set Variable        88
        run keyword if        ${a}>= 90        log        good        else if        ${a}<=70        log
        ...        just so so        else if        ${a}<=60        log        too bad        else
        ...        log        game over

case05
        [Documentation]        for循环
        : FOR        ${I}        IN RANGE        11
        \        log        ${i}
        : FOR        ${k}        IN RANGE        3        8        2
        \        log        ${k}

case06
        [Documentation]        调用引用自己写的python库去实现自己想要的功能
        ...        注意转义
        Import Library        G:/Git/robot/UI/CustomLibrary\\add.py
        ${a}        Evaluate        int(4)
        ${b}        Evaluate        int(5)
        ${add}        add        ${a}        ${b}
        log        ${add}

case07
        [Documentation]        Library引入自带Screenshot库之后可以截图
        Take Screenshot
