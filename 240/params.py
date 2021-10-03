# 缺省参数，或者叫默认值参数
def e(a=5):
    print(a)


e()


# 不定长参数
def f(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


def g(m, n, o=9, *args):
    print("m=", m)
    print("n=", n)
    print("o=", o)
    print("args=", args)


g(5, 2, 2, 9, 8, 4)
