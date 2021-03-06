#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 递归，求一个数的阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# print( fact(1000) )

# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 尾递归
def fact_wei(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# fact_wei(1000)

# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
# fact(5)对应的fact_iter(5, 1)的调用如下：
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n, a, b, c):
    if n == 1:
        print(a,n,'-->', c,n)
    else :
        move(n-1,a,c,b); # 先将a上的n-1块通过c移到b
        move(1,a,b,c);   # 将a的下面的第一块从a移到c
        move(n-1,b,a,c); # 将b上的n-1块从b移到c
move(2,'A','B','C')

###=================================================================================================================
