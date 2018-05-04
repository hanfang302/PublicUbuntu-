import re
ret = re.match('[A-Z][a-z]*', 'Mmfgdsvdsdaf').group()
print(ret)
print('*'*50)

ret = re.match('h+', 'hhhello python').group()
print(ret)
print('*'*50)

ret = re.match('h?', 'hhhhhhello python').group()
print(ret)
print('*'*50)

ret = re.match('[a-z\d]{7}', 'fh12fsdofj5hfj26').group()
print(ret)
print('*'*50)

ret = re.match('[a-z0-9]{4,15}', 'fh12fsdofj5hfj26').group()
print(ret)
print('*'*50)

ret = re.match('[\w]{4,20}@163\.com', 'hello@163.com').group()
print(ret)
print('*'*50)

ret = re.match('[^f]', 'h12fsdofj5hfj26').group()
print(ret)
print('*'*50)

ret = re.match('^[f]', 'fh12fsdofj5hfj26').group()
print(ret)
print('*'*50)

ret = re.match('[\w]{4,20}@163.com$', 'hello@163.com').group()
print(ret)
print('*'*50)

a = 'ho ver abc'
s = r'.*c\b'
ret = re.match(s, a).group()
print(ret)
print('*'*50)

a = 'ho verbavc '
s = r'.*ver\B'
ret = re.match(s, a).group()
print(ret)
print('*'*50)

a = 'hoverbavc '
s = r'.*\Bver\B'
ret = re.match(s, a).group()
print(ret)
print('*'*50)