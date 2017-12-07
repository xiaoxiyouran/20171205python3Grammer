
# 对函数fact(n)编写doctest并执行：

import logging



def fact(n):
    '''
    >>> fact(5)
    120
    >>> fact(1)
    1
    >>> fact(-1)
    Traceback (most recent call last):
            ...
    ValueError
    >>> fact(1001)
    '''

    if n == 1:
        return 1
    if n < 1:
        raise ValueError()
    elif n >1000:
        logging.error('value is too large')
        return
    return n * fact(n - 1)
if __name__ == "__main__":
    import doctest
    logging.basicConfig(level=logging.ERROR)
    doctest.testmod()
