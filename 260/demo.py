class Master(object):
    def __init__(self):
        self.kongfu = "古法的煎饼果子配方"

    def make_cake(self):
        print(self.kongfu + "的方式制作了一个煎饼果子")


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print(self.kongfu + "的方式制作了一个煎饼果子")


class Prentice(School, Master):
    pass


if __name__ == '__main__':
    damao = Prentice()
    print(damao.kongfu)
    damao.make_cake()
