a = "1"


# 类
# 对象
# 1  isinstance判断一个对象是否是某种类型
print(isinstance(a, (bool, int)))


# 2 callable 判断一个对象是否可以被调用
def f():
    for i in range(0, 10 ** 9):
        if (i - int(str(i)[::-1])) % 9 != 0:
            print("找到了一个反常数,你不在真实世界")
            break
    else:
        print("你在真实世界")


class A(object):
    def __call__(self, *args, **kwargs):
        pass
    def abc(self):
        pass

# 整数，字符串，列表，字典等这些类型的实例不可以被调用
print(callable(a))
# 类可以被调用
print(callable(A))
b = A()
print("类的实例b",callable(b))
# 方法可以被调用
print(callable(b.abc))

# def g(a: int):
#     return int(str(a)[::-1])


t = lambda x: int(str(x)[::-1])
# lambda函数可以被调用
print(callable(t))

# 3 help()
help(callable)
help(isinstance)

# 4 id()
u = "1"
print(id(a))
print(id(u))
y = 1
print(id(y))
w = y
print(id(w))
