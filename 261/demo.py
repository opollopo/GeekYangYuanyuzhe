# dir()

if __name__ == '__main__':
    # dir()
    print(dir())
    s = ""
    print(dir(s))
    # help()
    help(s.index)
    # locals()
    def f(p):
        u = 5
        print(locals())
        print(globals())
    f(8)
    # globals()
