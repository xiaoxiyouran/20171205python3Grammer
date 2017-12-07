#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 一边循环一边计算的机制，称为生成器：generator
g = (x * x for x in range(10)) # 将列表的[]  -- > （）
# for n in g:
#     print(n)  # 列表生成器的遍历

###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 斐波拉切数列像generator，后面的元素是一个个的推出来的

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(6)

# 如果函数中包含yield，就不再是普通的函数，而是generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# generator 是每次遇到上次的yield 就返回，并沿着下面继续执行
for n in fib_generator(6):
    print(n)

# 用for 循环拿不到generator的返回值

g = fib_generator(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:  # 用异常捕获返回的值
        print('Generator return value:', e.value)
        break

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
#  输出杨辉三角
def triangles(n):
    L = [1]
    while len(L) < n+1 :
        yield list(L)
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 10
results = []
for t in triangles(n):
    print(t)
    results.append(t)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')