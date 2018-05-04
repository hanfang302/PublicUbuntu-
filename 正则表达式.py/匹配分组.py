import re

ret = re.match('[1-9]?\d$|100','78').group()
print(ret)
print('*'*50)

ret = re.match('[1-9]?\d$|100','8').group()
print(ret)
print('*'*50)

ret = re.match('[0-9]?\d$|100','100').group()
print(ret)
print('*'*50)

ret = re.match('([^-]*)-([\d+])','010-123456789')
print(ret.group(1))
print('*'*50)

ret = re.match('([^-]*)-(\d+)','010-123456789')
print(ret.group(2))
print('*'*50)

ret = re.match('<[a-z]*>\w*</[a-z]*>','<html>hh</html>')
print(ret.group())

ret = re.match(r'<([a-z]*)>\w*</\1>','<html>hh</html>')
print(ret.group())
print('*'*50)

ret = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><h1>www.baidu.com</h1></html>')
print(ret.group())
print('*'*50)

ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=ame1)>','<html><h1>www.baidu.com</h1></html>')
print(ret.group())
print('*'*50)