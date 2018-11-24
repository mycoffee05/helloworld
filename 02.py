class A():
    name = 'dana'
    age = 18

    # 注意参数self
    def say(self):
        self.name = 'aaa'
        self.age = 20
# 此案例说明
# 类实例的属性和其对象实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量
# A为类实例
print(A.name)
print(A.age)

print('*'*20)
# id可以鉴别出一个变量是不是同一个变量
print(id(A.name))
print(id(A.age))

a = A()

print(a.name)
print(a.age)
print(id(a.age))
print(id(a.name))

class Teacher():
    name = 'dada'
    age = 19
    def say(self):
        self.name = 'ss'
        self.age = 22
        print('My name is {0}'.format(self.name))
        # 调用类的成员变量需要用__class__
        print('My age is {0}'.format(self.age))
    def sayAgain():
        # 绑定类访问成员
        print(__class__.name)
        print(__class__.age)
        print('hello again')
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()
