
# 如果要匹配很多字符时,可以先编译正则表达式,节约时间

import re
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$') # 该对象已经包含了正则,不用再给正则
# 使用：
print( re_telephone.match('010-12345').groups() )
# ('010', '12345')
print( re_telephone.match('010-8086').groups() )
# ('010', '8086')