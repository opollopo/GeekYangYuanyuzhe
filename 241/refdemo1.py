# 引用 reference
# 不可变类型：数字，字符串，元组
c = 100
d = c
print(id(c), id(d))
c = 200
print(id(c))
print(d)

# 可变类型：列表，字典，集合
a = ["1111", "b"]
b = a
print(id(a), id(b))
a.append("5")
print(id(a))
print(b)
