def pass_lens(p):
    return 8 <= len(p) <= 16
# print('1'.isdigit())
# print(''.isalpha())

def pass_char(p:str):
    # 定义3个标志，n,a,t分别表示是否包含数字，字母，特殊字符，如果值是1表示包含，否则不包含
    n,a,t = 0,0,0
    for i in p:
        if i.isdigit():
            n = 1
        elif i.isalpha():
            a = 1
        else:
            t = 1
    return n+a+t >= 3