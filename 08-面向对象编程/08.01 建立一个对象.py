class Student(object):
    '''
    类描述...
    '''
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
    def __init__(self, name, score): # 第一个参数永远是self，表示创建的实例本身
        self.__name = name             # 把各种属性绑定到self，因为self就指向创建的实例本身
        self.__score = score

    def print_score(self):  # 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

print( bart._Student__name ) # 有实际内存
# <__main__.Student object at 0x10657f908>
print( Student )
# <class '__main__.Student'>

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            raise ValueError('bad gender input!')
        self.__gender = gender

# 测试:
bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
###=================================================================================================================


