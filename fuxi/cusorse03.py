# 判断语句，值是Fasle有：0，0.0，“”，[],(),{},None
#
count = 50
while count > 0:
    score = int(input("(1-5)成绩:"))
    if 2 < score <= 5:
        print("及格")
    elif 0 <= score <= 2:
        print("不及格")
        continue
    else:
        print("输入错误")
        break
    print("恭喜你，取得好成绩")
    count -= 1
else:
    # 循环全部执行完了
    print("成绩查询完毕")
