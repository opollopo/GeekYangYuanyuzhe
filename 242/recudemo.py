# 递归函数，直接或者间接调用自己的函数
# 阶乘 n! = n*(n-1)! , n是整数,例如: 5！ = 5x4x3x2x1
def f(n):
    # 一定要有退出条件
    if n == 0:
        return 1
    return n*f(n-1)

