import turtle

turs = []
for i in range(5):
    turs.append(turtle.Turtle(shape="turtle"))


def draw_square(r, t: turtle.Turtle):
    t.penup()
    for _ in range(4):
        t.fd(r)
        t.left(90)
    t.pendown()
    t.circle(r, 90)
    return


s = 0.618
# 设置小海龟初始角度
turs[0].left(0)
turs[1].left(70)
turs[2].left(140)
turs[3].left(210)
turs[4].left(280)
if __name__ == '__main__':
    for j in range(5):
        turs[j].speed()
        r = 50
        for i in range(5):
            draw_square(r, turs[j])
            r /= s
    turtle.done()
