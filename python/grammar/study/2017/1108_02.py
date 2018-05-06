def fetcher(obj,index):
    return obj[index]

# def fun1(x,y):
#     return x[y]

x = 'spam'
# fetcher(x, 3)
# fetcher(x, 4)

##################
try:
    fetcher(x,4)
    # fun1(x,4)
except IndexError:
    print('got exception')

################
def catcher():
    try:
        fetcher(x,4)
    except IndexError:
        print('got exception catcher')
    print('continuing')

catcher()
##################
try:
    raise IndexError
except IndexError:
    print("got exception 01")
##########################
def after():
    try:
        fetcher(x, 4)
    finally:
        print('after fetch')
    print("try?")
    
after()