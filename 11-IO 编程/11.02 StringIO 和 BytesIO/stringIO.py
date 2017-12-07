from io import StringIO
# 在内存中读写

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) # str

f = StringIO('Hello!\nHi!\nGoodbye!') # 可用一个str初始化
while True:
    s = f.readline()
    if s == '':
        break
    print( s.strip() )

# 使用f.seek()回到开始处
from io import StringIO
f = StringIO("1\n2\n3\n")
print( 'tell',f.tell() ) # 这儿指针不会移动
# f.write(f.getvalue())
print( 'tell',f.tell() ) # 这儿指针不会移动


f.write("4\n 5\n 6")  # 一写,前面就读不到
print( 'tell',f.tell() )
f.seek(0)
print( 'tell',f.tell() )

while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())