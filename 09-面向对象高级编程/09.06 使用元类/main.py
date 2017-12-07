from hello import Hello
h = Hello()
h.hello()

print( type(Hello) ) # 类的类型 <class 'type'>
print(type(h))       # 实例的类型 <class 'hello.Hello'>

# class 动态创建的方式是使用type() 函数

# type()函数既可以返回一个对象的类型，又可以创建出新的类型

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 使用metaclass 创造类
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
# type 函数依次传入三个名称:class的名称；
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
h = Hello()
h.hello()

###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: metaclass 是类的类
# 先定义metaclass，就可以创建类，最后创建实例
# 类是metaclass 的实例
# metaclass是类的模板，所以必须从`type`类型派生：

class ListMetaclass(type): # 元类默认以 Metaclass 结尾
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

# ListMetaclass.__new__()来创建:

# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。
L = MyList()
L.add(1)
print(L) # [1]



###=================================================================================================================
