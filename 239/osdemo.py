import os
import shutil

# 不能重命名文件夹
# os.rename("fuxi", "yufayifuxi")
# 重命名文件,绝对路径
# os.rename("C:/Users/Administrator/PycharmProjects/pythonProject1/杨原宇喆/atm.py", "C:/Users/Administrator/PycharmProjects/pythonProject1/杨原宇喆/atmui.py")
# os.rename("a.py", "b.py")
# ./ 当前目录， ../ 表示父级目录
# os.rename("./cong.py", "./b.py")

# 删除
# os.remove("b.py")

# 新建文件
# f = open("a.py",'w')
# f.close()

# 新建文件夹
# os.mkdir("new")

# 删除文件夹，必须是空文件夹
# os.rmdir("new")


# 递归删除
# shutil.rmtree("new")

# 获取当前路径
p = os.getcwd()
print(p)

# 获取某路径下所有文件
# pa = "C:/Users/Administrator/PycharmProjects/pythonProject1"
# r = os.listdir(pa)
#
# print(r)

# 扫描某路径下所有文件及文件大小
p = "C:/"


def scan(pa="C:/"):
    r = os.listdir(pa)
    for i in r:
        # 判断是文件还是文件夹
        temp_path = pa + "/" + i
        if os.path.isdir(temp_path):
            try:
                scan(temp_path)
            except (PermissionError, FileNotFoundError):
                continue
        file_info = os.stat(temp_path)
        num = file_info.st_size / 1024 / 1024
        if num > 50:
            print("文件名：%s,大小为%0.2f %s" % (temp_path, num, "MB"))


# scan(p)
scan(p)
a = input("扫描结束:")
