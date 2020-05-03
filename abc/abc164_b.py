a, b, c, d = map(int, input().split())

for i in range(1000):
    if c <= 0:
        print('Yes')
        break
    else:
        c -= b
    if a <= 0:
        print('No')
        break
    else:
        a -= d
