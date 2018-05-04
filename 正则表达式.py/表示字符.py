import re

ret = re.match('.','a')
print(ret.group())
print('*'*50)

ret = re.match('天宫\d号', '天宫2号')
print(ret.group())
print('*'*50)

ret = re.match('[hH]','hello python')
print(ret.group())
print('*'*50)

ret = re.match('[hH]','Hello python')
print(ret.group())
print('*'*50)

ret = re.match('[0123456789]','8Hello python')
print(ret.group())
print('*'*50)

ret = re.match('\w','Q1f23456')
print(ret.group())
print('*'*50)

ret = re.match('\W','1f23456')
print(ret.group())
print('*'*50)

ret = re.match('\s',' hellopython')
print(ret.group())
print('*'*50)

