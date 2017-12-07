
print( 'a b   c'.split(' ') )
# ['a', 'b', '', '', 'c']

import  re
print( re.split(r'\s+', 'a b   c') ) # 以1 或 多个空格进行分割
# ['a', 'b', 'c']

print( re.split(r'[\s\,]+', 'a,b, c  ,d') ) # 空格或, 分割
# ['a', 'b', 'c', 'd']


print( re.split(r'[\s\,\;]+', 'a,b;; c  d') )
# ['a', 'b', 'c', 'd']