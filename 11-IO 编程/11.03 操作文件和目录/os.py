import os
opration = os.name # 操作系统类型
print( opration )
# posix 系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
info = os.uname() # 操作系统的详细信息,在 Windows 上不提供
print( info )

print( os.environ ) # 环境变量

print( os.environ.get('PATH') )

# 查看当前目录的绝对路径:
dir_abs =  os.path.abspath('.')
# '/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
dir_abs_new = os.path.join( dir_abs, 'testdir')
# '/Users/michael/testdir'

# 然后创建一个目录:
# os.mkdir( dir_abs_new ) # 如果已久有目录,会报错

# 删掉一个目录:
# os.rmdir( dir_abs_new )


# 拆分路径
dir_split =  os.path.split('/Users/michael/testdir/file.txt')
print( dir_split ) # ('/Users/michael/testdir', 'file.txt')

ext_name = os.path.splitext('/path/to/file.txt') # 得到文件的扩展名
print( ext_name )   # ('/path/to/file', '.txt')


# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove

# 复制文件
import shutil;
for file in os.listdir('.'):
    if os.path.splitext(file)[1] == ".py":
        print(file )

        shutil.copy(file, "a.py") # 复制一个文件到一个文件或一个目录

# shutil.rmtree("te") # 删除整个目录
# copyfile(src, dst)
# 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException.如果当前的dst已存在的话就会被覆盖掉
# copymode(src, dst)
# 只是会复制其权限其他的东西是不会被复制的
# copystat(src, dst)
# 复制权限、最后访问时间、最后修改时间
# copy(src, dst)
# 复制一个文件到一个文件或一个目录
# copy2(src, dst)
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
# copy2(src, dst)
# 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
# copytree(olddir, newdir, True / Flase)
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接

# 列出当前目录下的所有目录
dir = [x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有的.py 文件
py_file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

import os

# def dir_l():
#     os.system('ls -l > text.txt') # 调用系统函数
#     with open('text.txt', 'r') as f:
#         f_list = f.readlines()
#     for file in f_list:
#         if file[0] == 'd':
#             print(file, end='')

