#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: list 的使用
classmates = ['Michael', 'Bob', 'Tracy']

# 获取列表的长度
classmates_len = len(classmates) # 3

# 访问最后一个元素
classmates_last = classmates[classmates_len - 1] # 正序范围【 0，3 ）
classmates_last = classmates[-1]

classmates_first = classmates[-classmates_len]    # 负序范围 [ -1,-3 ]

# 把元素插入到指定位置
classmates.insert(1, 'Jack') # ['Michael', 'Jack', 'Bob', 'Tracy']


# 删除末尾的元素，并返回
classmates_last = classmates.pop() # 'Tracy'

# 删除指定位置的元素
classmates_1 = classmates.pop(1)

# 将某个位置的元素替换
classmates[1] = 'Sarah'         #  ['Michael', 'Sarah']

# list 里面的元素的数据类型也可以不同
list_type = ['Apple', 123, True]

# list 嵌套, 可以看成是一个二维数组
list_nest = ['python', 'java', ['asp', 'php'], 'scheme']
list_nest_len = len(list_nest) # 4

# 也可以拆开写
nest = ['asp', 'php']
list_nest = ['python', 'java', nest, 'scheme']

# 拿到 'php'
list_nest_21 = list_nest[2][1]

# 空 list
list_empty = []
list_empty_len = len(list_empty) # 0
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: tuple 一旦初始化就不能被修改
tuple_classmates = ('Michael', 'Bob', 'Tracy')

# 可以索引,但不能再赋值 classmates[0]，classmates[-1]

# tuple不可变，所以代码更安全
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
tuple_elements = (1, 2)
tuple_empty = ()
tuple_one = (1,) # 区分数学公式中的 ()

# tuple 中含有列表，列表可变. 因为tuple 只保证指向不变而已
t_list = ('a', 'b', ['A', 'B'])
t_list[2][0] = 'X'
t_list[2][1] = 'Y'

print(t_list)
###=================================================================================================================


###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印'Apple'
print( L[0][0] )

# 打印'Python'
print( L[1][1] )

# 打印'Lisa'
print( L[2][2] )
###=================================================================================================================
