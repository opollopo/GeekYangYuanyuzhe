import matplotlib.pyplot as plt
import numpy as np


# 输出1-100，自身与逆序数差再对9做除法
def nixushu(n: int):
    return int(str(n)[::-1])


x = np.arange(0, 10000, 10)
y = list(map(lambda i: (i - nixushu(i) / 9), x))
plt.plot(x, y)
plt.show()
