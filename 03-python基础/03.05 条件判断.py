#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: if 语句
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 如果一个条件满足,就不执行剩下的语句
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 简写,只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = []
if x:
    print('True')

# 类型转换

birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

xiaoming_height = 1.75
xiaoming_weight = 80.5

xiaoming_BMI = xiaoming_weight / ( xiaoming_height * xiaoming_height )
if xiaoming_BMI < 18.5 :
    print("过轻")
elif xiaoming_BMI < 25 :
    print('正常')
elif xiaoming_BMI < 28 :
    print( '过重' )
elif xiaoming_BMI < 32 :
    print('肥胖')
else :
    print( '严重肥胖' )

print( xiaoming_BMI )
###=================================================================================================================
