import re

ret = re.match(r'\d+','9999,10000')
print(ret.group())
print('*'*50)

ret = re.findall(r'\d+','python=9999,c=10000,a=55555')
print(ret)
print('*'*50)

#数据进行替换
ret = re.sub(r'\d+','9998','c=10000')
print(ret)
print('*'*50)