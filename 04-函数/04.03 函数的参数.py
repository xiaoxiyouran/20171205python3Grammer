#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 计算x^n
# 函数带默认参数,默认参数应该在列表的最后面
def power( x, n=2 ):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 不按顺序提供部分参数,必须带上参数名
enroll('Adam', 'M', city='Tianjin')

# 默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L

s = add_end([1, 2, 3])
print( s ) # [1, 2, 3, 'END']

add_end() # ['END', 'END']
add_end() # ['END', 'END', 'END'] # 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 无论调用多少次都不会有问题
print(  add_end() ) # ['END']
print( add_end() ) # ['END']

# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 可变参数
# 参数的个数可变
def calc(*numbers): # 在内部是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc() # 可以传入 0 个参数

# 如果已经有了个list 或 tuple
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print( calc(*nums) )

###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Miachel',12) # 只传必须参数
person('Bob', 35, city='Beijing') # 也可以传入任意个数的关键字参数：

# 可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 简化写法
person('Jack', 24, **extra) # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 命名关键字参数
def person_check(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person_only(name, age, *, city, job): # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)

person_only('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person_must(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

# person_must('Jack', 24, 'Beijing', 'Engineer')   # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

# 带默认参数带，city 参数可不填
def person_default(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 命名关键字参数city具有默认值，调用时，可不传入city参数：
person_default('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person_lack(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

###=================================================================================================================


###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1, 2)  # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)  # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b') # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None) # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


# 通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}


# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。



###=================================================================================================================
