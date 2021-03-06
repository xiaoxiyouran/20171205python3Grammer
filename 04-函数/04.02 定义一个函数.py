#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 定义一个函数
# 带参数类型检查的
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type') # 会抛出异常的
    if x >= 0:
        return x
    else:
        return -x

# print( my_abs('A') )
###=================================================================================================================



###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 空函数
# 现在还没想好函数的功能
def nop():
    pass
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 函数可以返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6) # 同时获得返回值
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100, 100, 60, math.pi / 6)
print( r ) # (151.96152422706632, 70.0)

###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
#
# 的两个解。
#
# 提示：计算平方根可以调用math.sqrt()函数：

def quadratic(a, b, c):
    x1 = ( -b + math.sqrt( b*b - 4*a*c ) ) / (2*a);
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a);
    return x1,x2

res = quadratic(1,2,1)
print(res)
###=================================================================================================================
