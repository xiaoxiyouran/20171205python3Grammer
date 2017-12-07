import  re

res = re.match(r'^(\d+)(0*)$', '102300').groups() # 默认是贪婪匹配,\d+ 把后面的0都匹配了

print( res )
# ('102300', '')

# 加个?  让它尽可能少的匹配
print( re.match(r'^(\d+?)(0*)$', '102300').groups() )