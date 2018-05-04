import re

m = 'c:\\a\\b\\c'
print(m)
print('*'*50)

ret = re.match('c:\\\\', m).group()
print(ret)
print('*'*50)

ret = re.match('c:\\\\a', m).group()
print(ret)
print('*'*50)

ret = re.match(r'c:\\a', m).group()
print(ret)
print('*'*50)