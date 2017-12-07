
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 可迭代
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print( isinstance([], Iterable) ) # True

print( isinstance({}, Iterable) ) # True

print( isinstance('abc', Iterable) ) # True

print(  isinstance((x for x in range(10)), Iterable) ) # 生成器

print( isinstance(100, Iterable) ) # False
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator( generator 的)
# 使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
print( isinstance((x for x in range(10)), Iterator) ) # True

print( isinstance([], Iterator) ) # False

print( isinstance({}, Iterator) ) # False

print( isinstance('abc', Iterator) ) # False

# 注：  生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 转化法
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print( isinstance(iter([]), Iterator) ) # True
print( isinstance(iter('abc'), Iterator) ) # True

# Python的for循环本质上就是通过不断调用next()函数实现的，例如
for x in [1, 2, 3, 4, 5]:
    pass

# 完全等价于
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break



###=================================================================================================================




