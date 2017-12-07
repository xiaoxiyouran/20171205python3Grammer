def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise  # ZeroDivisionError('0 除错误') # 将错误向上抛出的过程中转换为另一种类型

# bar()

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
from functools import reduce

def str2num(s):
    try:
        s = int(s)
    except ValueError as e:
        print("Not Integer,Will Be Convert To Float:", e)
    else:
        print( 'no error' )
    finally:
        s = float(s)
    return s

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

###=================================================================================================================
