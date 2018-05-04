import pymysql
db = pymysql.connect("localhost","root","bc123","BFA",charset='utf8' )
def luntan():
    while True:
        print("欢迎来到博鳌亚洲论坛\n管理员请选择1,\n用户请选择2,\n退出界面请选择3")
        print('*'*25)
        p2 = int(input("请输入你要选择的序号："))
        print('+'*25)
        if p2 == 1:
            root()
        elif p2 == 2:
            user()
        else:
            break
    db.close()
    print('*'*25)
def root():
    cursor = db.cursor()
    params = input("请输入管理员账号:")
    sql = "SELECT * from root where rootname='%s'"%params
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id_name = row[0]
            rootname = row[1]
            passwords = row[2]
            print('*'*25)
        while True:
            
            if rootname == params:
                rpwd = int(input("请输入管理员密码："))
                if passwords == rpwd:
                    print("管理员登录成功")
                    print('*'*25)
                    while True:
                        print("管理员界面请选1,\n用户管理界面请选2,\n退出请选其他")
                        p1 = int(input('请输入你要选择的序号：'))
                        print('+'*25)
                        if p1 == 1:
                            while True:
                                print('注册管理员帐号请选1,\n删除管理员帐号请选2,\n修改管理员帐号请选3,\n查询管理员帐号请选4,\n退出管理员界面请选5.')
                                p = int(input('请输入你要选择的序号:'))

                                print('*'*25)
                                if p == 1:
                                    root_a()
                                elif p == 2:
                                    root_b()
                                elif p ==3:
                                    root_c()
                                elif p == 4:
                                    root_d()
                                elif p == 5:
                                    break
                        elif p1 == 2:
                            while True:
                                print('注册用户帐号请选1,\n删除用户帐号请选2,\n修改用户帐号请选3,\n查询用户帐号请选4,\n退出用户管理界面请选5.')
                                p = int(input('请输入你要选择的序号:'))
                                print('*'*25)
                                if p == 1:
                                    user_a()
                                elif p == 2:
                                    user_b()
                                elif p ==3:
                                    user_c()
                                elif p == 4:
                                    user_d()
                                elif p == 5:
                                    break
                        else:
                            break
                elif passwords == None:
                    print("管理员密码输入为空，请重新输入。")
                else:
                    print("管理员密码输入错误，请重新输入。")
            elif rootname == None:
                print("管理员帐号输入为空，请重新输入。")
            else:
                print("管理员帐号输入错误，请重新输入。")
            break
            print('*'*25)
    except Exception as e:
        print("Error: 无法获取数据")
        print('*'*25)
def root_a():
    cursor = db.cursor()
    a = str(input("请输入名字："))
    c = int(input('请输入密码：'))
    params = [a,c]
    sql = "INSERT INTO root values(%s,%d);"%params
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def root_b():
    cursor = db.cursor()
    params = input("请输入你要删除的名字：")
    sql = "delete from root where rootname='%s'"%params
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def root_c():
    cursor = db.cursor()
    a = input("请输入你要修改的名字：")
    b = input("请输入你的新名字：")
    params = [b,a]
    sql = "update roots set rootname=%s where rootname=%s;"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def root_d():
    cursor = db.cursor()
    params = str(input("请输入你要查询的名字："))
    sql = "SELECT * from root where rootname='%s'"%params
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            a = row[1]
            b = row[2]
            print('帐号=%s,密码=%s'%(a,b))
            print('*'*25)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)   
        print('*'*25)     
def user_a():
    cursor = db.cursor()
    a = str(input("请输入名字："))
    b = int(input("请输入邮箱："))
    c = int(input('请输入密码：'))
    d = int(input('请输入生日：'))
    e = str(input('请输入性别：'))
    params = [a,b,c,d,e]
    sql = "INSERT INTO user values(%s,%d,%d,%d,%s);"%params
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def user_b():
    cursor = db.cursor()
    params = str(input("请输入你要删除的名字："))
    sql = "delete from user where username='%s'"%params
    try:    
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def user_c():
    cursor = db.cursor()
    a = str(input("请输入你要修改的名字："))
    b = str(input("请输入你的新名字："))
    params = [b,a]
    sql = "update user set username=%s where username=%s;"
    try:
        count2 = cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def user_d():
    cursor = db.cursor()
    a = str(input("请输入你要查询的名字："))
    sql = "SELECT * from user where username='%s'"%a
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            #uid = row[0]
            username = row[0]
            email = row[1]
            password = row[2]
            birt = row[3]
            sex = row[4]
            
       # 打印结果
            print("名字=%s,邮箱=%d,密码=%d,生日=%d,性别=%s"%(username,email,password,birt,sex))

        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def user():
    cursor = db.cursor()
    sql = "SELECT * from user;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            username = row[0]
            password = row[2]
        while True:
            params = str(input("请输入用户账户:"))
            if username == None:
                print("用户帐号输入为空，请重新输入。")
            elif username == params:
                rpassword = int(input("请输入用户密码："))
                if rpassword == None:
                    print("用户密码输入为空，请重新输入。")
                elif rpassword == password:
                    print("用户登录成功")
                    print('*'*25)
                    while True:
                        print("账户管理请选1\n信息管理请选2\n退出请选择其他")
                        p3 = int(input("请输入你要选择的序号："))
                        print('+'*25)
                        if p3 == 1:
                            while True:
                                print('注册用户帐号请选1,\n删除用户帐号请选2,\n修改用户帐号请选3,\n查询用户账号请选4,\n退出请选择其他')
                                p = int(input('请输入你要选择的序号:'))
                                print('+'*25)
                                if p == 1:
                                    user_a()
                                elif p == 2:
                                    user_b()
                                elif p ==3:
                                    user_c()
                                elif p == 4:
                                    user_d()
                                else:
                                	break
                        elif p3 == 2:
                            while True:
                                print("增加信息请选1,\n删除信息请选2，\n修改信息请选3,\n查询信息请选4,\n退出请选择其他")
                                p4 = int(input("请输入你要选择的序号:"))
                                print('+'*25)
                                if p4 == 1:
                                    center_a()
                                elif p4 == 2:
                                    center_b()
                                elif p4 == 3:
                                    center_c()
                                elif p4 == 4:
                                    center_d()
                                else:
                                    break
                        else:
                            break
                        break
                else:
                    print("用户密码输入错误，请重新输入。")
            else:
                print("用户帐号输入错误，请重新输入。")
            break
            print('*'*25)
    except Exception as e:
        print("Error: 无法获取数据")
        print('*'*25)
def center_a():
    cursor = db.cursor()
    a = str(input("请输信息标题："))
    b = str(input("请输入信息内容："))
    params = [a,b]
    sql = "INSERT INTO center values(0,%s,%s)"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def center_b():
    cursor1 = db.cursor()
    params = str(input("请输入你要删除的信息标题："))
    sql = "delete from center where name=%s;"
    try:    
        cursor1.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def center_c():
    cursor = db.cursor()
    a = str(input("请输入你要修改的信息标题："))
    b = str(input("请输入你新的信息标题："))
    params = [b,a]
    sql = "update center set name=%s where name=%s;"
    try:
        count2 = cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)  
        print('*'*25)  
def center_d():
    cursor = db.cursor()
    a = str(input("请输入你要查询的信息标题："))
    sql = "SELECT * from center where name='%s'"%a
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            name = row[1]
            news = row[2]
        
            print("信息标题=%s,信息内容=%s"%\
                (name,news))
            print('*'*25)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def main():
    luntan()


if __name__ == '__main__':
    main()
