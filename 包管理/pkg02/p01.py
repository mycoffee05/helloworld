
class Student():
    def __init__(self,name='Noname',age=18):
        self.name = name
        self.age = age
        return None
    def say(self):
        print('My name is {0}'.format(self.name))
        return None
def sayHello():
    print('hi,欢迎欢迎')