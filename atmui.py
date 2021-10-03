desc = '''
***********ATM***********
1、login
2、logon
3、exit
请输入：
'''
f = open("user.txt", 'r')
t = f.read()
f.close()
# [{"username":"Jack","password":"23456","balance":9000},...]
user_list = eval(t)


# 登录
def log_in():
    u = input("username:")
    p = input("password:")
    for i in user_list:
        if i["username"] == u:
            if i["password"] == p:
                print("success", i["balance"])
                break
            else:
                print("密码错误")
    else:
        print("用户名不存在，请注册")


# 注册
def log_on():
    u = input("username:")
    p = input("password:")
    b = input("balance:")
    d = {"username": u, "password": p, "balance": b}
    user_list.append(d)
    f1 = open("user.txt", 'w')
    f1.write(str(user_list))
    f1.close()


if __name__ == "__main__":
    while 1:
        k = input(desc)
        if k == "1":
            log_in()
        elif k == "2":
            log_on()
        elif k == "3":
            exit(2)
        else:
            print("输入错误")
