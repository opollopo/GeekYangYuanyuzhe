s = "hello world"
# s[开始索引:结束索引:步长]
# print(s[-1:-3:-1])
# print(s[::-1])


# 定义一个函数把整数倒叙输出
# 1、123  321
# 2、-321  -123
# 3、如果倒叙过来超过整数范围 [-2**31, 2**31-1] 返回0
def fun1(num) -> int:
    if num >= 0:
        if float(str(num)[::-1]) > 2 ** 31 - 1:
            return 0
        else:
            return int(str(num)[::-1])
    else:
        if float("-" + str(num)[1:][::-1]) < -2 ** 31:
            return 0
        else:
            return int("-" + str(num)[1:][::-1])


print(2 ** 31*-1)
print(2 ** 31 - 1)
print(fun1(-5893))
