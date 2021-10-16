# 密码验证程序
# 1、长度范围8-16
# 2、至少包含三类字符（数字，字母，特殊字符）
# 3、字符不能连续重复3次及以上
def pass_lens(p):
    return 8 <= len(p) <= 16
# print('1'.isdigit())
# print(''.isalpha())

def pass_char(p:str):
    # 定义3个标志，n,a,t分别表示是否包含数字，字母，特殊字符，如果值是1表示包含，否则不包含
    n,a,t = 0,0,0
    for i in p:



