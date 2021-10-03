from threading import Thread

num = 0


def f1():
    global num
    num += 1
    print("f1", num)


def f2():
    global num
    num += 2
    print("f2", num)


# f1()
# f2()
# 1000人同时点赞，多线程成并发执行
#
# for i in range(1000):
#     p = Thread(target=f1)
#     p.start()
#     q = Thread(target=f2)
#     q.start()
# print(num)


# 闭包
def f3():
    n = 5

    def f4():
        print(n)

    return f4


a = f3()
a()


# 返回多个值
def f5():
    return 1, 2, 3, 4


t = f5()
# 拆包
t1, t2, t3, t4 = f5()
print(t)
