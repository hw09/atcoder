x, k, d = map(int, input().split())

dx = abs(x)
y = dx // d

if k >= y:
    dx = dx - y * d
    if (k-y) % 2 == 0:
        print(dx)
    else:
        dx = abs(dx - d)
        print(dx)
elif k < y:
    dx = dx - k * d
    print(dx)
