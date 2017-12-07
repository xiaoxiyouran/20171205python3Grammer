
class Student(object):
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法, 给指定对象绑定的
s.set_age(25) # 调用实例方法
print( s.age )

# 给class 绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print( s.score )

# 但动态绑定允许我们在程序运行的过程中动态给class加上功能

# 只允许对Student实例添加name和age属性

class A(object):
    __slots__ = ()
    pass

A.set = set_score
