def m_pow_n(m, n=3):
    return 1 if n == 0 else m * m_pow_n(m, n - 1)


# 匿名函数使用的是lambda表达式, lambda 参数: 返回值
# 三元运算符  A if 条件 else B  ， 1 if n == 0 else m*m_pow_n(m, n-1)
# a = lambda m, n: 1 if n == 0 else m * m_pow_n(m, n - 1)
# print("m_pow_n:", m_pow_n(2,20))
# print("a:", a(2,20))
# map 加工数据，
b = [1, 2, 3, 4, 5, 6]
print(list(map(m_pow_n, b)))
print(list(map(lambda m, n=3: 1 if n == 0 else m * m_pow_n(m, n - 1), b)))

stu = [{"seq": 1, "name": "A", "yuwen": 90, "shuxue": 80, "English": 100},
       {"seq": 2, "name": "B", "yuwen": 80, "shuxue": 90, "English": 10},
       {"seq": 3, "name": "C", "yuwen": 100, "shuxue": 80, "English": 90}]

re = sorted(stu, key=lambda x: x['yuwen'])
print(re)
