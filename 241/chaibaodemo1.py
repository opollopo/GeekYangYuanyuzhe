# 拆包,列表[]，元组()，字典{},集合{}
a = (1, 2, 3)
b1, b2, b3 = a
print(b1, b2, b3)


# 返回多个变量时
def f():
    return "John", 25, "female"


c1, c2, c3 = f()


# 装包
def p(*args):
    # 拆包
    d1, d2, d3 = args
    print(d1, d2, d3)


p(1, 2, 3)


# 交换两个变量的值
a = 3
b = 5
b, a = a, b

