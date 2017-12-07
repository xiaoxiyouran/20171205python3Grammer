import os
def findpath(s,path1='.'):
    for x in os.listdir(path1):
        if os.path.isfile(os.path.join(path1,x)):
            if s in x:
                finalpath = os.path.join(path1,x)
                print(os.path.abspath(finalpath))
        elif os.path.isdir(os.path.join(path1,x)):
            findpath(s,os.path.join(path1,x))

def printStruct(empty = 0,path = '.'):
    empty += 1
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path,x)):
            print('  '*empty,'-',x)
        elif os.path.isdir(os.path.join(path,x)):
            print('   '*empty, x)
            printStruct(empty,os.path.join(path,x))


# 统一用绝对地址
# def disTree(startPath = './', path='./'):
#     for root, dirs, files in os.walk(path):
#         level = root.replace(startPath, '').count(os.sep)
#         for dir in dirs:
#
#             disTree(startPath,os.path.join(startPath,dir)) # 是文件夹,传到下一级
#         print(level)
#     print(indent)


if __name__ == '__main__':
    findpath('te')
    # printStruct(0,'/Users/cookie')
    level = 3
    indent = '|  ' * 1 * level + '|----'
    startPath = './'
