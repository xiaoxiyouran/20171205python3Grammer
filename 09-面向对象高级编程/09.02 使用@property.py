
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:
class Student(object):

    @property
    def score(self):  # getter 方法,把方法当成属性用
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
s.score  # OK，实际转化为s.get_score()
# s.score = 9999

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self): # 只有getter 方法,只读属性
        return 2015 - self._birth

# @property广泛应用在类的定义中
#
# ，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0

    # def __init__(self,width,height):
    #     self._width = width
    #     self._height = height


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        print('{} x {}'.format(self._width, self._height))
        return  self._width * self._height



# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
###=================================================================================================================

