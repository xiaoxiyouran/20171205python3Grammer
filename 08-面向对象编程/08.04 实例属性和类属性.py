
# python是动态语言: 创建的实例可以任意绑定属性
class Student(object):
    name = 'Student'        # 类本身绑定的属性,类的所有实例都能访问到
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print( s.name )
print(Student.name) # 打印类的name属性

s.name = 'Michael'  # 给实例绑定name属性
del s.name          # 如果删除实例的name属性

# 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student2(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def __del__(self):
        Student.count += -1

Student = Student2
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            del bart
            print('Students:', Student.count)
            print('测试通过!')

#=================================================================================================================
