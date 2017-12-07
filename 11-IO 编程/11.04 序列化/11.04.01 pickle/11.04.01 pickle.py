import pickle
d = dict(name='Bob', age=20, score=88)

# pickle.dumps(d) # 序列化成一个bytes

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

print( d )
