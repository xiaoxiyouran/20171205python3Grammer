#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 1、变量可以指向函数
f = abs
print( f(-10) )


###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 2、函数名也是变量
# abs = 10
# abs(-10) # 无法使用该函数
# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 3、将函数作为参数传入函数
def add(x, y, f):
    return f(x) + f(y) # 具体的什么操作，由传入的参数决定

x = -5
y = 6
f = abs
print( add(x,y,f) )

###=================================================================================================================

