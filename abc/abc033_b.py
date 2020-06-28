n = int(input())
sump = 0
sp = []
for i in range(n):
    x, y = input().split()
    sp.append([x, y])
    sump += int(y)

ans = 'atcoder'
for y in range(n):
    if int(sp[y][1]) > (int(sump/2)):
        ans = sp[y][0]
        break

print(ans)