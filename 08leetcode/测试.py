f = {4: 3, 3: 3}


def find(x):
    f.setdefault(x, x)
    print(f[x])
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]
find(4)
