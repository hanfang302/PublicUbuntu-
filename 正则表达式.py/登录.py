import pymysql
#1.连接数据库
db = pymysql.connect('localhost','root','books',charset='utf8'
cursor = db.cursor()

c = str(input('请输入管理员帐号：'))
d = str(input('请输入密码：'))
sql = "SELECT * FROM guanliyuan "
try:
	#正常
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		a = row[0]
		b = row[1]
		if c != a and d == b:
			print('帐号错误')
			break
		elif c == a and d != b:
			print('密码错误')
			break
		else:
			print('登录成功')
			break

		db.commit()
except:
	print('报错')
	#错误
	db.rollback()
db.close()