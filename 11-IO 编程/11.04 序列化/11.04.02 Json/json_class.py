import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
# print(json.dumps(s))

# 定一个转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict)) # 先将对象转成一个字典

# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__)) # 可以偷懒,把任意实例变成字典
s_dump = json.dumps(s, default=lambda obj: obj.__dict__)

# 反序列化,将字典转成类实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))