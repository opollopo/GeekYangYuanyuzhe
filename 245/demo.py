def func(num1, num2):
    try:
        res = num1 % num2
    except Exception as e:
        print("出现了错误", e)
    else:
        print("没出现错误")
    finally:
        return res
    print(3)


print(func(2, 10))
