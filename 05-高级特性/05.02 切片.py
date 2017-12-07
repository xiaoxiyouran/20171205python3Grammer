#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 取一个列表的前n个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 方法一： 用循环
r = []
n = 3
for i in range(n) :
    r.append( L[i] )

print( r )

# 方法二： 用切片
print( L[0:3] ) # [0,3)
print( L[:3] )

# 倒数切片
print( L[-2:] ) # 取最后两个元素
print( L[-2:-1] ) # L[-2:-1) # 取的是倒数第2个元素

# 创建一个0-99的数列
L = list(range(100))
L_10 = L[:10] # 0-9 取出前10个元素
L_last_10 = L[-10:] # 取出最后10个元素

# 前11-20个数
L_11_20 = L[10:20]

# 前10个中每2个取一个
print( L[:10:2] ) # [0, 2, 4, 6, 8]

# 所有数，每5个取一个：
print( L[::5] ) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 原样复制一个列表
L_copy = L[:]
print( L_copy ) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

###=================================================================================================================


###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: tuple 的切片（不可变的列表）
print( (0, 1, 2, 3, 4, 5)[:3] ) # (0, 1, 2)

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 字符串也可以看成是一种list
print( 'ABCDEFG'[:3] ) # ABC
print( 'ABCDEFG'[::2] ) # ACEG

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(string):
    # 数据类型检查
    if not isinstance(string, (str)):
        print('输入数据错误')
        return string

    # 定义起始值
    start = 0
    # 从左至右遍历字符串，求start值
    for i in range(len(string)):
        if string[i] == ' ':
            start += 1
        else:
            break

    # 检查字符串内容是否全部是空格
    if start == len(string):
        return ''

    # 若不全是空格，从右遍历字符串，求last值
    else:
        # 定义尾部值
        last = -1
        # 当尾部没有空格的情况时
        if string[last] != ' ':
            return string[start:]
        # 当尾部有空格的情况时
        else:
            while string[last] == ' ':
                last -= 1
            return string[start:last + 1]

# 方法二：用递归
def trim_recursion(s):
    if (len(s) == 0 or (s[0] != ' ' and s[-1] != ' ')): # 判断长度是否为0， 或者首尾为非空
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

trim = trim_recursion;
# 测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

