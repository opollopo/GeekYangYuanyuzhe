class Master(object):
    def __init__(self):
        self.kongfu = "古法的煎饼果子配方"

    def make_cake(self):
        print(self.kongfu + "的方式制作了一个煎饼果子")

    def dayandai(self):
        print('大')


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print(self.kongfu + "的方式制作了一个煎饼果子")

    def xiaoyandai(self):
        print('小')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫式煎饼果子配方"

    def make_cake(self):
        print(self.kongfu + "的方式制作了一个煎饼果子")


if __name__ == '__main__':
    damao = Prentice()
    print(damao.kongfu)
    damao.make_cake()
    damao.dayandai()
    damao.xiaoyandai()
    # 每一个子类都有这个魔法属性，叫做方法查找顺序
    print(Prentice.__mro__)
