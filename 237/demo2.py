# 列表推到式，[输出表达式 for i in 来源列表 筛选条件]
li = [55, 60, 70]
d = {'k1': [i for i in li if i > 66], 'k2': [i for i in li if i < 66]}
print(d)
