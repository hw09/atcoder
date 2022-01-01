i = int(input())
a = [int(x) for x in input().split()]

color = [False]*8
top = 0

for i in a:
    if i <= 399:
        color[0] = True
    elif i <= 799:
        color[1] = True
    elif i <= 1199:
        color[2] = True
    elif i <= 1599:
        color[3] = True
    elif i <= 1999:
        color[4] = True
    elif i <= 2399:
        color[5] = True
    elif i <= 2799:
        color[6] = True
    elif i <= 3199:
        color[7] = True
    else:
        top += 1

mx = color.count(True) + top
mi = color.count(True)
if mi == 0 and top > 0:
    mi = 1
print('{} {}'.format(mi, mx))