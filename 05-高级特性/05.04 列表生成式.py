#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 列表生成式，主要是生成列表的
list_generate =  list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 法一： 循环
list_generate_pow = []
for i in range(1,11):
    list_generate_pow.append( i*i ) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 法二：列表生成式
# 列表生成式则可以用一行语句代替循环生成上面的list：
list_generate_pow_by_row = [x * x for x in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
list_generate_even = [ x*x for x in range(1,11) if x % 2 == 0 ] # [4, 16, 36, 64, 100]


# 使用两层循环，可以生成全排列
list_generate_permulation = [m + n for m in 'ABC' for n in 'XYZ'] # 前面取一个，然后 依次取完后一个for
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下所有文件名和目录名
import os # 导入os模块，模块的概念后面讲到
category_file = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# ['05.01 构造一个列表.py', '05.02 切片.py', '05.03 迭代.py', '05.04 列表生成式.py']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
    print(k,'=',v)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
list_generate_vars = [k + '=' + v for k, v in d.items()] # ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L_lower = [s.lower() for s in L] # ['hello', 'world', 'ibm', 'apple']


###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 对于列表中有数字的需要排除在外，求列表的字符串变成小写后的输出
L_str_int = ['Apple','orange',12,'mother']
L_converter  = [x.lower() for x in L_str_int if isinstance(x,str) == True]
print( L_converter )

###=================================================================================================================
