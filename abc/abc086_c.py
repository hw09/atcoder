# パリティ
ans = 'Yes'
n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    if t < x + y:
        ans = 'No'
        break
    if  t % 2 != 0 and (x - y) % 2 == 0:
        ans = 'No'
        break
    elif t % 2 == 0 and (x - y) % 2 != 0:
        ans = 'No'
        break

print(ans)
