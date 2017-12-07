
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 判断一个对象的类型
type(123)
type('str')
type(None)

# 变量指向函数或者类，也可以用type()
type(abs)
# <class 'builtin_function_or_method'>

class A:
    pass
type(A) # 类
# <class '__main__.Animal'>
###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: if 判断
type(123)==type(456)

type('abc')==str

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 判断是否是函数
import types

def fn():
    pass

type(fn) == types.FunctionType # 自定义函数
type(abs)==types.BuiltinFunctionType # 内置函数
type(lambda x: x)==types.LambdaType # 是否是lambda 函数

type((x for x in range(10)))==types.GeneratorType # 是否是生成器

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 对类的继承

a = A()
isinstance(a,A)

# isinstance(d, Dog) and isinstance(d, Animal) # 判断是子类同时是父类

# 能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)

# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
isinstance([1, 2, 3], (list, tuple))

isinstance((1, 2, 3), (list, tuple))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 获取一个对象所有属性和方法
info = dir('ABC')
print( info )
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 以下两种方法等价
str_len = len('ABC')
str_len = 'ABC'.__len__()
str_low = 'ABC'.lower() # 普通的属性和方法

# 自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print( len(dog) )



###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

    def __print__(self):
        print( "x 的值是{0:.1f}".format(self.x))

obj = MyObject()
print( hasattr(obj, 'x')  ) # 有属性'x'吗？

obj.__print__()

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:

###=================================================================================================================

