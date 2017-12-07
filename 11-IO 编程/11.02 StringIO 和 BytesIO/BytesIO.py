from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())  # 写入的不是str，而是经过UTF-8编码的bytes。


# 用一个Bytes初始化

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read() # 像文件一样读取

print( f.getvalue().decode('utf-8') )
# 中文