#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Array module '  # 文档注释

__author__ = 'xi' # 作者


class Array(object):
    '''这是一个数组类'''
    __cls__ = 'Array'
    def __init__(self,*value):
        # a = Array(1,2,3,4)
        # exis = [1,2,3]
        # a = Array(*exis)
        if isinstance(value[0], int):  # a = Array(1,2,3,4)
            print('传入单个int')
            value = list(value)  # 不能用value[0] ??? 这里很奇怪
            #print(value)
        elif isinstance(value[0], list): # a = Arran([1,2,3])
            print('传入list')
            value = value[0]
        elif isinstance(value[0], tuple): # a = Arran((1,2,3))
            print('传入tuple')
            value = [x for x in value[0]]  # 统一用列表表示
        else:
            raise TypeError('等式右边的数据类型不对!')
        self._l = value
        self._index = 0

    def __len__(self):
        return len(self._l)

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        if self._index >= len(self._l):
            raise StopIteration()
        ret = self._l[self._index]
        self._index += 1
        return ret

    def __str__(self):
        __info = ''         # 只能返回一个字符串
        __title =  '%s object content:\n' % Array.__cls__
        __info +=__title

        __content_list = 'list: \n'
        for i in self._l:
            __content_list += '{}\t'.format(i)
        __info+=__content_list

        return __info

    __repr__ = __str__  # 打印开发者看到的字符串

    def __getitem__(self, n): #  obj[0] 能访问到指定序列的值
        if isinstance(n, int):  # n是索引
            if n < 0:
                n = len(self._l) + n
            return self._l[n]

        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            step = n.step
            if start == None and stop == None and step == None: # [:]
                print('访问所有序列码?')
                return self._l
            else:
                if start is None:
                    start = 0
                elif abs(start) > len(self._l):
                    aise
                    ValueError('start边界应为[%d,%d) 或者[%d,%d]' % (0,len(self._l),-1,-len(self._l)))
                elif start < 0:
                    #-1 : len-1 -2:len-2
                    start = len(self._l) + start

                if stop is None:
                    stop = len(self._l)
                elif abs(stop) > len(self._l) :
                    ValueError('stop边界应为[%d,%d) 或者[%d,%d]' % (0,len(self._l),-1,-len(self._l)))
                elif stop < 0:
                    stop = len(self._l) + stop

                if step is None:
                    step = 1

                ret_L = []
                cnt_step = 0

                # [1:2]
                # [1:10:3]
                # [:10]
                # [:]
                # [: : 2]
                # [1::3]
                for x in range(stop):
                    if x >= start and x == start + cnt_step * step:
                        cnt_step += 1
                        ret_L.append(self._l[x])

                return ret_L

    def __setitem__(self, key, *value):  # 传入的是([],):一个列表  ((),):单个元组  (2):单个值
        if isinstance(value[0],int):
            print('传入单个int')
            value = list(value) # 不能用value[0] ??? 这里很奇怪
            print( value )
        elif isinstance(value[0],list):
            print('传入list')
            value = value[0]
        elif isinstance(value[0],tuple):
            print('传入tuple')
            value = [x for x in value[0]] # 统一用列表表示
        else:
            raise TypeError('等式右边的数据类型不对!')

        if isinstance(key,int): # list[0] = 单个赋值
            if key < 0:
                key = len(self._l) + key
            if len(value) > 1:
                raise ValueError("等式右边只能赋一个值")
            self._l[key] = value[0] # 重新赋值
            return True

        if isinstance(key,slice): # list[1:3] = [1,2]
            start = key.start
            stop = key.stop
            step = key.step
            if start == None and stop == None and step == None:  # [:]
                print('访问所有序列')
                self._l = list(value)
                return True
            else:
                if start is None:
                    start = 0
                elif abs(start) > len(self._l):
                    raise ValueError('start边界应为[%d,%d) 或者[%d,%d]' % (0,len(self._l),-1,-len(self._l)))
                elif start < 0:
                    # -1 : len-1 -2:len-2
                    start = len(self._l) + start

                if stop is None:
                    stop = len(self._l)
                elif abs(stop) > len(self._l):
                    ValueError('stop边界应为[%d,%d) 或者[%d,%d]' % (0,len(self._l),-1,-len(self._l)))
                elif stop < 0:
                    stop = len(self._l) + stop

                if step is None:
                    step = 1

                cnt_step = 0

                # 允许a[1:] = [2] , 这种情况应该以保留原值为重要,更改的不够,则不更改原值

                # [1:2]
                # [1:10:3]
                # [:10]
                # [:]
                # [: : 2]
                # [1::3]
                list_del = []
                for x in range(stop):
                    if x >= start and x == start + cnt_step * step:
                        if len(value)>cnt_step:            #0,1,2
                            self._l[x] = value[cnt_step]
                        else: # 给的值不够
                            list_del.append(x)

                        cnt_step += 1

                new_list = []
                for i in range(len(self._l)):
                    if i in list_del:
                        continue
                    else:
                        new_list.append(self._l[i])
                self._l = new_list

                return True

    def __delitem__(self, key):
        if isinstance(key, int):  # list[0] = 删除单个元素
            if key < 0:
                key = len(self._l) + key
            return self._l.pop(key) # 返回删除元素的列表

        if isinstance(key, slice):  # list[1:3] = [1,2]
            start = key.start
            stop = key.stop
            step = key.step
            if start == None and stop == None and step == None:  # [:]
                print('删除所有序列')
                src_l = self._l
                self._l = list()
                return src_l
            else:
                if start is None:
                    start = 0
                elif abs(start) > len(self._l):
                    raise ValueError('start边界应为[%d,%d) 或者[%d,%d]' % (0, len(self._l), -1, -len(self._l)))
                elif start < 0:
                    # -1 : len-1 -2:len-2
                    start = len(self._l) + start

                if stop is None:
                    stop = len(self._l)
                elif abs(stop) > len(self._l):
                    ValueError('stop边界应为[%d,%d) 或者[%d,%d]' % (0, len(self._l), -1, -len(self._l)))
                elif stop < 0:
                    stop = len(self._l) + stop

                if step is None:
                    step = 1

                cnt_step = 0

                # 允许a[1:] = [2] , 这种情况 第1处的位置改为2,其它元素全删掉

                # [1:2]
                # [1:10:3]
                # [:10]
                # [:]
                # [: : 2]
                # [1::3]
                list_del = []
                for x in range(stop):
                    if x >= start and x == start + cnt_step * step:
                        list_del.append(x)
                        cnt_step += 1

                new_list = []
                del_list = []
                for i in range(len(self._l)):
                    if i in list_del:
                        del_list.append(self._l[i])
                        continue
                    else:
                        new_list.append(self._l[i])
                self._l = new_list
                return del_list

    def append(self,*value):
        if isinstance(value[0], int):
            print('传入单个int')
            value = list(value)  # 不能用value[0] ??? 这里很奇怪
            self._l.append(value[0])
        elif isinstance(value[0], list):
            print('传入list')
            value = value[0]
            for each in value:
                self._l.append(each)
        elif isinstance(value[0], tuple):
            print('传入tuple')
            # value = [x for x in value[0]]  # 统一用列表表示
            for each in value[0]:
                self._l.append(each)
        else:
            raise TypeError('append() 或 append([]) 或 append(())!')

        return True

    def __getattr__(self, attr):  # 当试图调用不存在的属性时会调用,默认返回的None
        raise AttributeError('\'%s\' object has no attribute \'%s\'' % (Array.__cls__,attr)) # 只响应特定几个属性

    def __call__(self):
        print('Not defined now obj().')



if __name__ == '__main__':
# -----------------------------------------------------init 测试
    # a = Array(1,2,3,4)
    # exis = [1,2,3]
    # a = Array(*exis)
    # a = Array([1,2,3])
    a = Array((1,2,3))
# -----------------------------------------------------len 测试
#     print(len(a))

#-----------------------------------------------------setitem 测试
    # a[1:] = () # 删除1 及其后面的元素
    # a[2:] = []   # 删除2 及其后面的元素
    # a[:1] = () # 删除[ : 1) 前面的元素
    # a[1:3] = [111] # 改第一个元素,剩下的元素被删除
    # a[0] = 5
    # a[::2] = [2,2]  # 没隔2个赋值
    # print(a)
    # a[1] = 2

#-----------------------------------------------------delitem 测试
    # del a[0] # 删除单个元素
    # del a[:] # 删除全部
    # del a[2:]  # [1 2]

    # del a[-2:-1] # 删除倒数第二个
    # del a[-1]    # 最后一个元素只能单个的删除

#-----------------------------------------------------append 测试
    # a.append(10)
    # a.append([1,2,3])
    # a.append((1,2,3))

    # a = [1,2,3]
    # a.append([4,5])
#-----------------------------------------------------getattr 测试
    # print( a.name )

#-----------------------------------------------------call 测试
    a()
