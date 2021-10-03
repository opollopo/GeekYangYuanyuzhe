class Hero(object):
    c = ""

    def __init__(self, h_name: str):
        self.name = h_name

    def __str__(self):
        return "我叫"+self.name

    def __del__(self):
        print("调用了删除方法")

    def b(self):
        pass


p = Hero("诸葛亮")
p.name
p.age = 27
p.b()
q = Hero("赵云")
print(p)
print(q)
del p


def a():
    pass


