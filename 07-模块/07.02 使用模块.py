#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' # 任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao'

import sys
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python3 hello.py获得的sys.argv就是['hello.py']

# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
def test():  # 外部调用该函数就是 filename.test()
    args = sys.argv # 获取程序运行的参数列表
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()
    print( sys.path ) # 系统的模块
    # 方法一：
    # sys.path.append('自定义模块路径')
    # 方法二：
    # .2.把自定义模块放到工作目录下，就可以直接在代码中导入了。
    # .3.在python交互命令行下导入模块: 刚试了下，也是路径的问题。在自定义模块所在目录下进入交互命令行，就可以导入使用了。（我用的是
    # win7系统，linux 应该也是如此）