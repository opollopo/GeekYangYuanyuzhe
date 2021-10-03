#   [156, 140,150,140,157,158,170]
c = 0
def quick_sort(a):
    global c
    if len(a) < 2:
        return a
    p = a[0]
    left = []
    right = []
    a.remove(p)
    for i in a:
        c += 1
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [p] + quick_sort(right)


b = [156, 140, 150, 140, 157, 158, 170]
print(quick_sort(b))
print(c)