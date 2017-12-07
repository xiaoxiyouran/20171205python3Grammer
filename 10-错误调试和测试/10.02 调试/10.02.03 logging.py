
import logging
logging.basicConfig(level=logging.INFO) #debug，info，warning，error等几个级别，当我们指定level=INFO时，info 后面的起作用
# 控制好输出级别
# 能输出到console或文件


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

