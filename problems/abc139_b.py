a, b = map(int, input().split())

ans = 0
nouse = 1
while nouse < b:
    ans += 1
    nouse += a - 1

print(ans)
