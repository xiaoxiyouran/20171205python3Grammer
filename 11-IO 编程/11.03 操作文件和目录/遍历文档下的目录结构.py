# -*- coding: utf-8 -*-
'''''
仿Linux命令tree生成树形目录结构，
并汇总当前目录下文件总算

Author: xi
Date: 2015-09-18

'''

from sys import argv
import os


def fileCntIn(currPath):
    '''''汇总当前目录下文件数'''
    return sum([len(files) for root, dirs, files in os.walk(currPath)])


def dirsTree(startPath,f):
    '''''树形打印出目录结构'''
    for root, dirs, files in os.walk(startPath): # 递归遍历当前目录,下一个目录
        # 获取当前目录下文件数
        fileCount = fileCntIn(root)
        # 获取当前目录相对输入目录的层级关系,整数类型
        level = root.replace(startPath, '').count(os.sep)
        # 树形结构显示关键语句
        # 根据目录的层级关系，重复显示'| '间隔符，
        # 第一层 '| '
        # 第二层 '| | '
        # 第三层 '| | | '
        # 依此类推...
        # 在每一层结束时，合并输出 '|____'
        indent = '|    ' * 1 * level + '|----'
        f.write( '%s%s  -r:%s\n' % (indent, os.path.split(root)[1], fileCount) )
        for file in files:
            indent = '|    ' * 1 * (level + 1) + '|----'
            f.write( '%s%s\n' % (indent, file) )


if __name__ == '__main__':
    # path = u"D:\\影像备份\\照片"
    # path = argv[1]
    path = '/Users/cookie/Downloads/20171205python3Grammer/'
    filename = 'outinfo.txt'
    f = open( filename, 'w', encoding='utf-8')
    dirsTree(path,f)
    f.close()
    print('输出结束!')