import time, functools

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 函数赋值给变量
def now():
    print('2015-3-25')

f = now
f()
###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __name__ 属性获得函数的名字
print( now.__name__) # 'now'
print( f.__name__ )

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 不改变函数内部,代码运行期间动态增加

# 返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw): # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper  # 返回一个新的函数

@log # 装饰器是接收一个函数作为参数的
def now():
    print('2015-3-25')

now()
# 先打印日志,再运行函数
# call now():
# 2015-3-25

# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now) # 原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 装饰器本身需要传入参数
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text): # 外部是先传入自身参数
    def decorator(func): # 2-传入函数
        def wrapper(*args, **kw): # 传入函数的任意参数
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# 需要定义三层函数

@log('execute')
def now():
    print('2015-3-25')

now()
# execute now():
# 2015-3-25

# 3层嵌套的效果
now = log('execute')(now) # 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 整体:函数的嵌套包装

###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 函数对象改变
# 函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
print( now.__name__ ) # wrapper ,因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的

# import functools # 模块

# 不带参数的包装器
def log(func):
    @functools.wraps(func) # 复制__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 带参数的decorator

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# work 2
def log1(text=None):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start_time = time.time()
            print("begin call", func.__name__,round(start_time))
            # 先被调用，后被打印
            return func(*args, **kw), print("end call:{0} \nspend time: {1} s".format(round(time.time()), round(time.time() - start_time)))
        return wrapper
    return (decorate, print("text:%s" % text ))[0] if text.__str__() == text else decorate(text)

@log1
def test1():
    print( "大家好，我是test1被执行" )
    time.sleep(2)


@log1('这里是参数') # 像全局变量
def test2():
    time.sleep(3)

test1()


###=================================================================================================================
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 练习2：
def log2(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call %s():' % fn.__name__)
        fn(*args, **kw)
        print('end call %s():' % fn.__name__)
    return wrapper


@log2
def now2():
    print('2017-03-25')


now2()



def log3(text=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            if text == None:
                print("%s():" % fn.__name__)
            else:
                print("%s %s():" % (text, fn.__name__))
            return fn(*args, **kw) # 返回带有返回值的函数
        return wrapper
    return decorator

@log3('execute')
def _on():
    print('2017-12-05')

_on()

###=================================================================================================================


