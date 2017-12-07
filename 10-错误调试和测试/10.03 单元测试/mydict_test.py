import unittest

from mydict import Dict

class TestDict(unittest.TestCase):  # 测试类继承

    def test_init(self):          # test 开头的方法会被运行
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言输出是否是我们所期望的。最常用的断言就是assertEqual()
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): # 待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): # 通过d.empty访问不存在的key时，我们期待抛出AttributeError：
            value = d.empty
    # 每个测试前运行,链接数据库?
    def setUp(self):
        print('setUp...')

    # 每个测试后运行,断开数据库?
    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest.main()

# 或者通过命令行运行
# python -m unittest mydict_test
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。