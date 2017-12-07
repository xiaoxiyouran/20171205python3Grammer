#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 内建的filter()函数用于过滤序列
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 删除列表中的偶数，只保留奇数部分
def is_odd( n ):
    return  n % 2 == 1

odd_left = list( filter(is_odd,range(10)) ) # [1, 3, 5, 7, 9]
print( odd_left )

# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

str_left = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 埃氏筛法 求素数
# 先构造一个从3开始的奇数序列，无穷序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列，返回的是一个惰性序列
        # print(list(it))

# 生成器先返回第一个素数2，然后，利用filter()，不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：


def is_palindrome(n):
    if isinstance(n, int):
        n = str(n)

    if len(n) == 0 or len(n) == 1: # 必须判断 len ==1 ，否则 n[1:-1] 就取不到了。
        return True
    start = n[0]
    end = n[-1]

    if start == end:
        return is_palindrome(n[1:-1])
    else:
        return  False

#
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# 注意 filter 是一种惰性运算
###=================================================================================================================
