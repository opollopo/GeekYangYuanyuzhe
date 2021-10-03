# 二分查找
import random

n = random.randrange(1, 100)
min_v = 1
max_v = 100
while min_v <= max_v:
    # mid = (max_v + min_v) / 2
    mid = min_v + (max_v - min_v) / 2
    if mid == n:
        break
    elif mid < n:
        min_v = mid
    elif mid > n:
        max_v = mid
print("随机数是：%d" % n, "最终猜到的mid是:%d" % mid)
# 时间复杂度 0(logn)