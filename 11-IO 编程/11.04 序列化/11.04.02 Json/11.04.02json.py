import json
d = dict(name='Bob', age=20, score=88)

serial_json = json.dumps(d)
# print( serial_json ) # {"name": "Bob", "age": 20, "score": 88}
with open('json.txt','w') as f :
    json.dump(d,f)


ver_sertial_json = json.loads( serial_json )
print( ver_sertial_json )

# json.loads是在内存中操作，不会写入硬盘
# json.load序列化后，写入硬盘

# 如果是写入文件json.dump(d,f)

