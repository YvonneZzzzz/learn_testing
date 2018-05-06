
def fun1(name):
    print("this is %s" %name)

# fun1("edrain")
# fun1("wahh")

def fun2(act, name="AAA"):  #默认参数放最后
    # print("this is %s, I want is %s" %(name,act))
    # print("this is %s, I want is %s" %name %act)  #错误的无法执行
    print("this is %s, I want is %s" %('DDD','CCC'))   #this is DDD, I want is CCC
    
def fun3(act, name="AAA"): 
 print("this is {}, I want is {}" .format('EEE','FFF'))   #this is DDD, I want is CCC


# fun2("BBB")
fun2("aaa")
fun3('ggg')
