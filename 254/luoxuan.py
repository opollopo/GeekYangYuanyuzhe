from turtle import *
# 绘制斐波那契螺旋线1，1，2，3，5，8，13
def draw_square(r):
    penup()
    for _ in range(4):
        fd(r)
        left(90)
    pendown()
    circle(r, 90)
    return

s = 0.618
r = 50
speed()
if __name__ == '__main__':
    for i in range(5):
        draw_square(r)
        r /= s
    done()
