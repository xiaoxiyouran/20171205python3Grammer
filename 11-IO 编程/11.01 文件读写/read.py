try:
    f = open('/path/to/file', 'r')
    print(f.read())
except FileNotFoundError as e:
    print('文件不存在',e)

else:  # 没有异常时才执行
    if f:
        f.close()

# 一次读取所有内容
with open('./onlyread.txt', 'r') as f: # 调用完会自动关闭
    print(f.read())

# 如果文件过大,反复调用read(size) 方法,'\n' 也占一字节
with open('./onlyread.txt', 'r') as f:
    print(f.read(10))


# 如果读取配置文件
with open('./onlyread.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

# 读取图片或视频等二进制文件
f = open('./test.jpg', 'rb')
print( f.read() )

# 取非UTF-8编码的文本文件
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

# 有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
