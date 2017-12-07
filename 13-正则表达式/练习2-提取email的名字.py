import  re
re_name=re.compile(r'\<*([\w\s]*?)\>*\s*([0-9a-zA-Z.]+)@([0-9a-zA-Z]+)[.]([a-zA-Z]{0,3}$)')

def name_of_email(addr):
    print( re_name.match(addr).groups() )
    if re_name.match(addr).group(1): # 如果无<> 第一个匹配会为空,('', 'tom', 'voyager', 'org')
        print((re_name.match(addr).group(1)))
    else:
        print((re_name.match(addr).group(2)))

test ='<Tom Paris> tom@voyager.org'
test = 'tom@voyager.org'
name_of_email(test)