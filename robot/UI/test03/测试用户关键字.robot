*** Settings ***
Resource              testflow01.robot
Resource              res01.robot

*** Test Cases ***
case01
        关键字测试        111        222        333        444
        log        ${arg1}

case02
        ${arg5}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}

case03
        ${arg5}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}

case04
        @{arg5}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}

case05
        ${arg5}        ${arg6}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}
        log        ${arg6}

case06
        ${arg5}        @{arg6}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}
        log        ${arg6}

case07
        ${arg5}        关键字测试        111        222        333        444
        log        ${arg1}
        log        ${arg5}
