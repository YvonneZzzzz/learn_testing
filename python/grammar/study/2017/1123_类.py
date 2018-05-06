class Person:
    # pass    #空的代码块
    def __init__(self,name):
        self.name = name


    def say_hi(self):
        print('hello',self.name)

p = Person('edrain')
p.say_hi()
# print(p)
Person('ed').say_hi()

