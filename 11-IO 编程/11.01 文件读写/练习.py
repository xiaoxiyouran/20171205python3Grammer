
with open('src.txt',) as f:
    with open('src_replace.txt','w+') as s:
        for i in f.readlines():
            s.write(i.replace('hello','hi'))