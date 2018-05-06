def format():
    age = 22
    name = 'edrain'

    print('{0} is {1} age'.format(name,age)) 
    print('{0} is {1} age {2}'.format(age,name,age))
    print('{} is {} age'.format(name,age)) 
    # 对于浮点数 '0.333' 保留小数点(.)后三位
    print('{0:.3f}'.format(1.0/3))
    # 使用下划线填充文本，并保持文字处于中间位置
    # 使用 (^) 定义 '___hello___'字符串长度为 11
    print('{0:_^11}'.format('hello'))
    # 基于关键词输出 'Swaroop wrote A Byte of Python'
    print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
    print('a',end=' ')
    # print('b',end='\n')
    print('b',end=' ')    
    print('c')

def calculate():
    a = 2
    a = a * 3
    b = 2
    b *= 3
    print(a)
    print(b)


def iftest():
    number = 23
    guess = int(input('Enter an integer : '))
    if guess == number:
        # 新块从这里开始
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
        # 新块在这里结束
    elif guess < number:
        # 另一代码块
        print('No, it is a little higher than that')
        # 你可以在此做任何你希望在该代码块内进行的事情
    else:
        print('No, it is a little lower than that')
        # 你必须通过猜测一个大于（>）设置数的数字来到达这里。

    print('Done')
    # 这最后一句语句将在
    # if 语句执行完毕后执行。


def whiletest():
    number = 23
    running = True

    while running:
        guess = int(input('Enter an integer : '))

        if guess == number:
            print('Congratulations, you guessed it.')
            # 这将导致 while 循环中止
            running = False
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    else:
        print('The while loop is over.')
        # 在这里你可以做你想做的任何事

    print('Done')

def fortest():
    # 将会输出1，2，3，4。不会输出 5
    # for i in range(1,5):
    # 将会输出1，3。 
    for i in range(1,5,2):       
        print(i)
    else:
        print('The for loop is over')


def breaktest():
    while True:
        s = input('Enter something : ')
        if s == 'quit':
            break
        print('Length of the string is', len(s))
    print('Done')


def continuetest():
    while True:
        s = input('Enter something : ')
        if s == 'quit':
            break
        if len(s) < 3:
            print('Too small')
            continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理


# format()
# calculate()
# iftest()
# whiletest()
# fortest()
# breaktest()
# continuetest()