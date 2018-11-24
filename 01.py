'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 必须有pass
    pass
# 定义一个对象
mingyue = Student()

# 定义一个用来描述听python的学生类
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    # 注意
    # 1.def 缩进层级
    # 2.系统默认一个self参数
    def doHomework(self):
        print('i am doing homework.')

        # 推荐用return语句
        return None
# 实例化一个叫yueyue的学生，具体对象
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()