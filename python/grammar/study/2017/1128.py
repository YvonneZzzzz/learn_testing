class Student():

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{} is {}'.format(self.name, self.score))
    
bart = Student("bart Sip", 99)
bart.print_score()