# f = open('/Users/michael/test.txt', 'w')
# f.write('Hello, world!')
# f.close()

# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open('./write.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!')