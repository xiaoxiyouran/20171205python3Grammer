def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' # 条件不满足,执行后面的,抛出AssertionError
    return 10 / n

def main():
    foo('0')


if __name__ == '__main__':
    main()
# python -O err.py 使用-O 偶 关闭断言,所有当做pass
