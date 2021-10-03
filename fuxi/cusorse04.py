# for in 放一个可迭代对象，字符串，列表，字典，range(n)
import time
import turtle as tu

# for i in range(4):
#     tu.forward(100)
#     tu.right(90)
# time.sleep(2)
# s = "hello world"
# for i in s:
#     print(i)

# 冒泡排序
lt = [150, 153, 148, 129, 160]
n = len(lt)
for i in range(n - 1):
    for j in range(n - i - 1):
        if lt[j] > lt[j + 1]:
            lt[j], lt[j + 1] = lt[j + 1], lt[j]
print(lt)

# 选择排序
lt = [150, 153, 148, 129, 160]
