#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a ORM module '  # 文档注释

__author__ = 'xi' # 作者
# 把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# ORM全称“Object Relational Mapping”

import  inspect
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 保存数据库的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        print('_' * 40, 'Field 被调用end')

        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 进一步定义各种字段类型
class StringField(Field):
    def __init__(self, name):
        print('_' * 40, 'StringField 被调用end')
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        print('_' * 40, 'IntegerField 被调用end')
        super(IntegerField, self).__init__(name, 'bigint')



###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 编写metaclass
# User -- > Model --> ModelMetaclass 一直找到元类,进行创建
class ModelMetaclass(type):
    print('_'*40,'ModelMetaclass 被调用begin')


    def __new__(cls, name, bases, attrs):
        print('cls:',cls)

        if name=='Model': # 排除掉对Model类的修改, 从User --> Model --> ModelMetaclass
            return type.__new__(cls, name, bases, attrs)


        print('Found model: %s' % name)
        # 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field): # 排除掉__main__模块和User
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        print('mappings',mappings)

        print('attrs1',attrs)
        for k in mappings.keys():
            print('k',k)

            attrs.pop(k)

        print('attrs2',attrs)

        attrs['__mappings__'] = mappings # 保存属性和列的映射关系, 放到该字段里
        print('attrs3', attrs)

        attrs['__table__'] = name        # 把表名保存到__table__中，这里简化为表名默认为类名

        print('_' * 40, 'ModelMetaclass 被调用end')

        return type.__new__(cls, name, bases, attrs)

###=================================================================================================================

# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等
###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO: 基类
class Model(dict, metaclass=ModelMetaclass):
    print('_'*40,'Model 被调用begin')

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 实现了save()
    # 方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name) # 一个个对象的名字
            params.append('?')
            args.append(getattr(self, k, None)) # id=1, name='Michael', email='test@orm.org', password='my-pwd' 获取这些字段对应的值
        # 连接数据库驱动即可真正连接
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def delete(self):  # 删
        # 连接数据库驱动即可真正连接
        sql = "delete from %s" % self.__table__
        print('SQL: %s' % sql)

    def update(self):  # 改
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        # 连接数据库驱动即可真正连接
        sql = "update %s set %s=%s" % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def find(self):  # 查
        # 连接数据库驱动即可真正连接
        sql = "select * from %s" % self.__table__
        print('SQL: %s' % sql)

    print('_'*40,'Model 被调用 end')


###=================================================================================================================

###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:
class User(Model):
    # 定义类的属性到列的映射
    print('_'*40,'User 被调用begin')

    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    print('_' * 40, 'User 被调用end')

if __name__ == '__main__':
    # 创建一个实例：
    u = User(id=1, name='Michael', email='test@orm.org', password='my-pwd')

    # 增删改查
    u.save()
    print('-' * 30)
    u.delete()
    print('-' * 30)
    u.update()
    print('-' * 30)
    u.find()
    print('-' * 15, "调用顺序如下", '-' * 15)
    print(inspect.getmro(User))


# 元类就是最终创造类的地方,其它继承它的类,把里面的方法, 属性 都放在attr 里面,会进行扫描的
###=================================================================================================================


###-----------------------------------------------------------------------------------------------------------------  class(begin)
### TODO:


###=================================================================================================================
