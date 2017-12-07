

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __str__ 打印字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael')) # 用户看到的字符串
s = Student('Michael')
print( s )

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__  # 打印开发者看到的字符串

s = Student('hah')
print( s )
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __iter__  可迭代对象

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __getitem__
class Fib(object):
    # def __init__(self):
    #     self.a, self.b = 0, 1  # 初始化两个计数器a，b
    #
    # def __iter__(self):
    #     return self  # 实例本身就是迭代对象，故返回自己
    #
    # def __next__(self):
    #     self.a, self.b = self.b, self.a + self.b  # 计算下一个值
    #     if self.a > 100000:  # 退出循环的条件
    #         raise StopIteration()
    #     return self.a  # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print( f[0] )

print( f[1] )

print( f[2] )

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 切片
print( list(range(100))[5:10] )

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])
print( f[:10] )

# 对step 和 负数进行处理
# __getitem__()的参数也可能是一个可以作key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __getattr__
# 避免找不到某个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):  # 当试图调用不存在的属性时会调用,默认返回的None
        if attr=='score':
            return 99

        if attr == 'age':
            return lambda :25    # 返回一个无参函数

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) # 只响应特定几个属性

s = Student()
print(  s.name )
print( s.score )

print( s.age() )

# __getattr__ 可以任意动态的调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list) # /status/user/timeline/list
# 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
# GET /users/:user/repos
# Chain().users('michael').repos  # 调用时完成替换
###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: __call__  将对象作为方法调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()  # self参数不要传入

# 判断是否可作为函数调用
print( callable(Student('me')) ) # True
print( callable( max ) )    # True

###=================================================================================================================

class Chain(object):
    def __init__(self, ch=''):
        self._ch = ch
    def __getattr__(self,ch=''):
        return Chain('%s/%s'%(self._ch,ch)) # 返回的是一个新的对象
    def __call__(self,*c):                  # 如果是() 就是对象调用
        s=''
        for i in c:
            s+=':'+i
        return self.__getattr__(s)
    def __str__(self):
        return self._ch
    __repr__=__str__

print('++++华丽丽的分割符号++++')
print(Chain().status.user.timeline.list)
print('++++华丽丽的分割符号++++')
print(Chain().users('michael').repos)
print('++++华丽丽的分割符号++++')
print(Chain().users('michael','zhangsan').repos.lession('math').teacher('qin'))



