class A(object):
    __instance = None
    def __init__(self, c):
        self.county = c
        print("init方法,初始话实例属性")

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            print("__new__方法，已经创建过一次实例，instance不为None")
            return cls.__instance
        print("__new__方法，未创建过实例，instance为None")
        cls.__instance = object.__new__(cls)
        return cls.__instance

if __name__ == '__main__':
    a = A("China")
    a.name = "John"
    print("我是", a.name, ",我来自", a.county)
    b = A("China")
    print("我来自", b.county)
    print("a的地址",id(a))
    print("b的地址",id(b))
    # 使用__new__实现单例模式

