# coding=utf-8

import logging
import traceback

def fun1():
    T = 1
    try:
        if T == 2 :
            print("2")
    # except Exception:
    #     if T == 3:
    #         print("3")
    # except：
    #     if T == 5：
    #         print("5")
    except EnvironmentError as e:
        logging.error(e)
        return 0

def fun2():
    a = 1
    b = 0
    c = 1
    try:
        if c == a*b :
            # print("result",c)
            print(c)
        # elif c == a + b :
        #     print("a+b",c)
        #     return 0
        #     # pass
    except Exception :#as e:  #输出错误的内容
        if c == a/b :
             print("a+b",c)
            # return 0
            # print("can't ",e)
        elif c == a + b:
            print("a+b",c)
            pass
    except BaseException as e:
        logging.error(e.args[0]) #错误码
        return 0
    except BaseException as e:
        logging.error(e.args[1]) #错误信息
        return 0
    # except:
    #     traceback.print_exc()

def fun3():
    a = 1
    b = 0
    c = 1
    if c == a*b:
        print("a/b",c)
    elif c == a+b:
        print("a+b",c)
    else:
        pass

# fun1()
fun2()
fun3()
