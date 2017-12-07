from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value) # 默认从1 开始计数

    # Jan = > Month.Jan, 1
    # Feb = > Month.Feb, 2
    # Mar = > Month.Mar, 3
    # Apr = > Month.Apr, 4
    # May = > Month.May, 5
    # Jun = > Month.Jun, 6
    # Jul = > Month.Jul, 7
    # Aug = > Month.Aug, 8
    # Sep = > Month.Sep, 9
    # Oct = > Month.Oct, 10
    # Nov = > Month.Nov, 11
    # Dec = > Month.Dec, 12

from enum import Enum, unique

@unique # 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(Weekday.Tue)    # Weekday.Tue
print(Weekday['Tue']) # Weekday.Tue
print(Weekday.Tue.value) # 2

print(day1 == Weekday.Mon) # True

print(Weekday(1)) # Weekday.Mon

print(day1 == Weekday(1)) # True

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        if not isinstance(gender, Gender):  # 加一个枚举类型检查就好了
            raise TypeError('gender must be enum value!')
        self.name = name
        self.gender = gender

# 测试:
lilei = Student('lilei', Gender.Male)
hanmeimei = Student("hanmeimei", Gender.Female)
if lilei.gender == Gender.Male and hanmeimei.gender == Gender.Female:
    print('测试通过!')
else:
    print('测试失败!')

###================================================================================================================

