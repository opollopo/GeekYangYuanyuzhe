# 集合,1、不重复，2、无序，3、元素确定（元素是不可变类型）


s0 = {1, 2, 3}
s1 = {"a", "b"}
s2 = {(), (1,), (1, 2)}
s3 = {1, "a", ()}

# 交集，两个集合共同的元素
print(s0 & s3)
print(s0 | s3)
# A减B的差集，A中去掉B的元素
print(s0 - s3)
print(s3 - s0)
# 等差差集,
print(s0 ^ s3)

s = set()
s.add(1)
print(s)
try:
    s.remove(2)
except KeyError as e:
    print("元素不存在")
# s1.clear()
print("s1=", s1)
s4 = s2.copy()
print(s2, "==", s4)

bloodCart = ['A', 'B', 'O', 'A1', 'A']

