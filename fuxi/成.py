# 输出1-100，自身与逆序数差再对9做除法
def nixushu(n: int):
    return int(str(n)[::-1])


for i in range(10):
    ret = (i - nixushu(i)) / 9
    print(i, nixushu(i), ret)
