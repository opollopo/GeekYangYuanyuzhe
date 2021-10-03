from turtle import *
import time


# 1、fib数列的第n项，f(0) = 0, f(1)= 1, f(n) = f(n-1)+(n-2)
# def f(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return f(n-1)+(n-2)

def f(n):
    f0, f1 = 1, 1
    for i in range(n):
        f0, f1 = f1, f0 + f1

    return f1


print(f(0))
print(f(1))
print(f(1800) / f(1801))


# 绘制斐波那契螺旋线1，1，2，3，5，8，13
def draw_square(r):
    # penup()
    for _ in range(4):
        fd(r)
        left(90)
    # pendown()
    circle(r, 90)
    return


# s = 0.618
# r = 50
# speed()
# if __name__ == '__main__':
#     for i in range(5):
#         draw_square(r)
#         r /= s


# 2、回文字符串判断函数

def h(s: str):
    if s == s[::-1]:
        print("是")
    else:
        print("否")


# h("a1ba")


# 3、平方数列表
print(list(map(lambda x: x ** 2, range(1, 101))))

# 4、筛选列表
info = [33, 44, 55, 10, 29, 8]
re = []
for i in info:
    if i < 100 and i % 2 == 0:
        re.append(i)
print(re)
# a = filter(lambda x: x < 100 and x % 2 == 0, info)
# print(list(a))
# 5、异常的捕获
try:
    print(a)
except Exception as e:
    print(1)
else:
    print(2)
finally:
    print(3)

