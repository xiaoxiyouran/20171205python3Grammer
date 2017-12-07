filename = 'src.txt'
with open(filename, "r") as f:
    x = f.readlines()   # 读取原文件并存储于x,要保证内存足够..
    with open(filename, "w"): pass  # 清空原文件
    for i in x:
        s = i.replace('hello', 'hi') # 将每一行中的字符替换
        with open(filename, "a") as f:
            f.write(s)