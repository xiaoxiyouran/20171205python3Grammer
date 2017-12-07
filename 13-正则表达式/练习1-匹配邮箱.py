import  re
# 正则
def is_valid_email(addr):
    mail_reg = re.compile(r'([0-9a-zA-z_.]+)@([0-9a-zA-Z]+)\.(\w{0,3})')
    res = mail_reg.match(addr)
    if res:
        print(res.groups())
        return True
    else:
        return False


# ('someone', 'gmail', 'com')
# ('bill.gates', 'microsoft', 'com')
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')