
# 面向对象的三个特性：封装，继承，多态
# class是用于定义类型
# def是用于定义方法
# 属性通常是指类中的变量，
# object是基类
# self 当前实例
class Bird(object):
    name = 'flamingo'

    def fly(self):
        print(self.name+'飞了')


# 创建一个鸟的实际的例子，实例
a = Bird()
a.name = '大雁'
a.fly()
w = Bird()
w.name = '鹈鹕'
w.fly()






class ChildBird(Bird):
    name = '幼鸟'

class Duck(object):
    name = 'Download'
    def fly(self):
        print('鸭子飞了')


def f(a):
    a.fly()
    print(a.name)



#
# d = Duck()
# f(a)


