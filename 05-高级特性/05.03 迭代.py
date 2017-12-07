#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 迭代
# 通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print( key ) # a b c

# dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

# 迭代value
for value in d.values():
    print( value ) # 1 2 3

# 同时迭代key和value
for k, v in d.items():
    print(k,":",v) # a : 1 b : 2 c : 3

# 字符串也是一个可迭代对象
for ch in 'ABC':
    print( ch ) # A B C

# 只要是可迭代对象for 就能运行
# 通过collections模块的Iterable类型判断（是否是可迭代对象）
from collections import Iterable
print (isinstance('abc', Iterable) )# str是否可迭代
#True

print( isinstance([1,2,3], Iterable) ) # list是否可迭代
#True

print( isinstance(123, Iterable) )  # 整数是否可迭代
#False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 0 A
# 1 B
# 2 C

# for循环里，同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# 1 1
# 2 4
# 3 9

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    # 列表的数据类型不是这样判断的
    # if not isinstance(L, int) and (L): # 加一个类型判断
    #     raise TypeError('pls enter a list')
    if len(L) == 0:  # 如果是空列表
        return (None, None)
    else:
        min = L[0]
        max = L[-1]
        for i in L: # 只要遍历到了所有元素
            if i < min:
                min = i
            elif i > max:
                max = i
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
###=================================================================================================================
